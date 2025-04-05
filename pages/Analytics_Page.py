import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# Page Config
st.set_page_config(
    page_title="Mumbai Property Analytics",
    page_icon="🏠",
    layout="wide"
)

# Title
st.title("📊 Mumbai Property Price Analysis")
st.markdown("Explore trends and insights into Mumbai's real estate market.")

# Tabs
map_tab, trend_tab, wordcloud_tab, sunburst_tab, radial_tab = st.tabs([
    "📍 Map View",
    "📈 Price Trend",
    "🛋️ Amenities Word Cloud",
    "🧭 BHK Distribution",
    "🎯 Facing vs Price"
])

# Load Aggregated Group Data
@st.cache_data
def load_group_df():
    df = pd.read_csv("data/processed/mumbai/visualization.csv")
    df['PRICE'] = round(df['PRICE'], 2)
    df['AREA'] = round(df['AREA'], 2)
    return df

group_df = load_group_df()
group_df["LOG_PRICE"] = np.log1p(group_df["PRICE"])

# Load full property dataset
@st.cache_data
def load_property_data():
    df = pd.read_csv("data/mumbai/res_apartment_dataset.csv")
    return df

df = load_property_data()

# Clean AGE column
def clean_age(age):
    if pd.isna(age):
        return None
    age = str(age).strip().lower()
    if "under construction" in age or "new" in age:
        return 0
    elif "-" in age:
        try:
            return int(age.split("-")[0])
        except:
            return None
    else:
        try:
            return int(age.split()[0])
        except:
            return None

df["AGE_CLEANED"] = df["AGE"].apply(clean_age)
df = df[df["PRICE"].notnull() & df["AGE_CLEANED"].notnull()]

# Tab 1: Map View
with map_tab:
    st.header("📍 Locality-wise Price & Area Map")
    st.markdown("This scatter map shows how properties are distributed across Mumbai localities. Price is indicated by color intensity and area is represented by the marker size.")

    tick_vals = list(range(14, 22))
    tick_text = [f"₹{int(np.expm1(val)) // 1_00_000}L" for val in tick_vals]

    fig = px.scatter_mapbox(
        group_df,
        lat="LATITUDE",
        lon="LONGITUDE",
        color="LOG_PRICE",
        size="AREA",
        hover_name="LOCALITY_NAME",
        hover_data={"PRICE": True, "AREA": True, "LOG_PRICE": False, "LATITUDE": False, "LONGITUDE": False},
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        mapbox_style="open-street-map",
    )
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.update_coloraxes(colorbar=dict(title="AVG PRICE (₹)", tickvals=tick_vals, ticktext=tick_text))
    st.plotly_chart(fig, use_container_width=True)

# Tab 2: Price Trend
with trend_tab:
    st.header("🏙️ Price Trend by Property Age")
    st.markdown("This line chart displays how average property prices vary based on the age of the building, grouped by city. It helps users understand how newer vs. older buildings are priced.")

    trend_df = df.groupby(["AGE_CLEANED", "CITY"])["PRICE"].mean().reset_index()
    fig2 = px.line(
        trend_df,
        x="AGE_CLEANED",
        y="PRICE",
        color="CITY",
        markers=True,
        labels={"AGE_CLEANED": "Property Age (Years)", "PRICE": "Average Price (INR)"},
        title="Average Property Price by Age Across Cities"
    )
    fig2.update_layout(legend_title_text="City")
    st.plotly_chart(fig2, use_container_width=True)

# Tab 3: Word Cloud
with wordcloud_tab:
    st.header("🛋️ Word Cloud of Property Amenities")
    st.markdown("This word cloud visualizes the most frequently mentioned amenities across property listings. It gives users a quick glance at common lifestyle features in the listings.")

    amenity_keywords = ["gym", "swimming", "pool", "garden", "clubhouse", "security", "lift", "elevator",
        "parking", "intercom", "cctv", "wifi", "internet", "playground", "kids", "park",
        "jogging", "yoga", "indoor", "game", "sports", "fire", "alarm", "power", "backup",
        "maintenance", "community", "solar", "rainwater", "spa", "library", "theatre"]

    text = " ".join(desc for desc in df["DESCRIPTION"].dropna().astype(str).str.lower())
    amenity_text = " ".join(word for word in re.findall(r'\b\w+\b', text) if word in amenity_keywords)

    wordcloud = WordCloud(background_color="white", width=1200, height=600).generate(amenity_text)
    fig_wc, ax = plt.subplots(figsize=(12, 6))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig_wc)

# Tab 4: Sunburst Plot
with sunburst_tab:
    st.header("🧭 Sunburst Plot: City > Locality > BHK")
    st.markdown("This hierarchical sunburst chart lets you drill down from city to locality to BHK configuration, helping users see the availability of property types across regions.")

    sunburst_df = df[["CITY", "LOCALITY_NAME", "BEDROOM_NUM"]].dropna()
    sunburst_df["BHK"] = sunburst_df["BEDROOM_NUM"].astype(int).astype(str) + " BHK"
    selected_city = st.selectbox("🔍 Select a City to Zoom In:", ["All Cities"] + sorted(sunburst_df["CITY"].unique()))

    if selected_city != "All Cities":
        filtered_df = sunburst_df[sunburst_df["CITY"] == selected_city]
        path = ["LOCALITY_NAME", "BHK"]
    else:
        filtered_df = sunburst_df
        path = ["CITY", "LOCALITY_NAME", "BHK"]

    fig3 = px.sunburst(filtered_df, path=path, color_discrete_sequence=px.colors.qualitative.Prism,
        title=f"Availability of BHKs {'in ' + selected_city if selected_city != 'All Cities' else 'by City and Locality'}")
    fig3.update_layout(margin=dict(t=40, l=0, r=0, b=0))
    st.plotly_chart(fig3, use_container_width=True)

# Tab 5: Radial Bar Chart
with radial_tab:
    st.header("🎯 Avg Property Price by Facing")
    st.markdown("This radial chart shows the average property price based on the direction a property is facing. It can help users assess if certain facings have higher market value.")

    facing_df = df.groupby("FACING")["PRICE"].mean().reset_index().dropna()
    facing_df = facing_df.sort_values("PRICE", ascending=False)

    fig4 = go.Figure(go.Barpolar(
        r=facing_df["PRICE"],
        theta=facing_df["FACING"],
        marker_color=px.colors.sequential.Plasma_r,
        marker_line_color="black",
        marker_line_width=1,
        opacity=0.8
    ))
    fig4.update_layout(
        title="🎯 Radial Bar Chart: Avg Price by Property Facing",
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=False
    )
    st.plotly_chart(fig4, use_container_width=True)
