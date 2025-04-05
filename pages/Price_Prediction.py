# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd

# # Load the saved dataframe and model pipeline
# with open("model/df.pkl", "rb") as file:
#     df = pickle.load(file)

# with open("model/pipeline.pkl", "rb") as file:
#     pipeline = pickle.load(file)

# st.title("Price Prediction Page")
# st.write("Welcome to the Price Prediction Page! Enter details to predict property price.")

# # User Inputs
# area = st.number_input("Area (sq. ft.)", min_value=100, step=50, value=500)

# bedroom_options = sorted(df['BEDROOM_NUM'].unique().tolist())
# bedroom_num = st.selectbox('No. of Bedrooms', bedroom_options)

# balcony_options = sorted(df['BALCONY_NUM'].unique().tolist())
# balcony_num = st.selectbox('No. of Balcony', balcony_options)

# floornum = st.selectbox('Floor Number', sorted(df['FLOOR_NUM'].unique().tolist()))
# furnish = st.selectbox('Furnishing Type', sorted(df['FURNISH'].unique().tolist()))
# age = st.selectbox('Age of the Property', sorted(df['AGE'].unique().tolist()))
# facing = st.selectbox('Facing', sorted(df['FACING'].unique().tolist()))
# locality_options = sorted(df["LOCALITY_NAME"].dropna().unique().tolist())
# locality = st.selectbox("Locality Name", locality_options)

# if st.button('Predict'):
#     # Create DataFrame from user input
#     input_data = pd.DataFrame([{
#         'AREA': float(area),
#         'BEDROOM_NUM': float(bedroom_num),
#         'BALCONY_NUM': float(balcony_num),
#         'FLOOR_NUM': floornum,
#         'FURNISH': furnish,
#         'AGE': age,
#         'FACING': facing,
#         'LOCALITY_NAME': locality
#     }])

#     # Predict price
#     predicted_price = pipeline.predict(input_data)[0]
    
#     predicted_price = np.expm1(predicted_price)

#     # Display the prediction
#     st.success(f"Predicted Price: ₹{predicted_price/100000:,.2f} Lacs")
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Set the title and description
st.set_page_config(page_title="Property Price Predictor", page_icon="🏠", layout="wide")

st.title("🏠 Property Price Prediction")
st.markdown("""
Welcome to the Property Price Prediction tool!  
Enter the property details below to predict the price.
""")
st.markdown("___")

# Load the saved dataframe and model pipeline
with open("model/df.pkl", "rb") as file:
    df = pickle.load(file)

with open("model/pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

# Style using markdown (add some padding or line breaks for better spacing)
st.markdown("<h3>Fill in the details of the property:</h3>", unsafe_allow_html=True)

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    # User Inputs with default values
    area = st.number_input("Area (sq. ft.)", min_value=100, step=50, value=375)  # Default: 375
    bedroom_num = st.selectbox('No. of Bedrooms', sorted(df['BEDROOM_NUM'].unique().tolist()), index=sorted(df['BEDROOM_NUM'].unique().tolist()).index(1))  # Default: 1
    balcony_num = st.selectbox('No. of Balcony', sorted(df['BALCONY_NUM'].unique().tolist()), index=sorted(df['BALCONY_NUM'].unique().tolist()).index(1))  # Default: 1
    floornum = st.selectbox('Floor Number', sorted(df['FLOOR_NUM'].unique().tolist()), index=sorted(df['FLOOR_NUM'].unique().tolist()).index('mid rise'))  # Default: 'mid rise'

with col2:
    furnish = st.selectbox('Furnishing Type', sorted(df['FURNISH'].unique().tolist()), index=sorted(df['FURNISH'].unique().tolist()).index('unfurnished'))  # Default: 'unfurnished'
    age = st.selectbox('Age of the Property', sorted(df['AGE'].unique().tolist()), index=sorted(df['AGE'].unique().tolist()).index('10+ year old property'))  # Default: '10+ year old property'
    facing = st.selectbox('Facing', sorted(df['FACING'].unique().tolist()))
    locality_options = sorted(df["LOCALITY_NAME"].dropna().unique().tolist())
    locality = st.selectbox("Locality Name", locality_options, index=locality_options.index('dadar'))  # Default: 'Dadar'

# Add some padding between inputs and button
st.markdown("<br>", unsafe_allow_html=True)

# When user presses predict
if st.button('🔮 Predict Price'):
    # Create DataFrame from user input
    input_data = pd.DataFrame([{
        'AREA': float(area),
        'BEDROOM_NUM': float(bedroom_num),
        'BALCONY_NUM': float(balcony_num),
        'FLOOR_NUM': floornum,
        'FURNISH': furnish,
        'AGE': age,
        'FACING': facing,
        'LOCALITY_NAME': locality
    }])

    # Predict price
    predicted_price = pipeline.predict(input_data)[0]
    predicted_price = np.expm1(predicted_price)  # Convert back from log scale

    # Display the result with some styling
    st.markdown(f"<h2 style='color: #1E90FF;'>Predicted Price: ₹{predicted_price/100000:,.2f} Lacs</h2>", unsafe_allow_html=True)
    
    # Additional information or tips (optional)
    st.markdown("""
    * Keep in mind that this is an estimate based on historical data.
    * The model does not account for certain external factors such as market conditions or sudden trends.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("___")

# Footer with some information or links
st.markdown("""
### 📝 About the App:
This tool is designed to predict the price of a property based on user-provided details.  
It is powered by machine learning models trained on historical real estate data.
""")

st.markdown("___")