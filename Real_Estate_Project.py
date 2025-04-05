import streamlit as st
from pages import Price_Prediction

# Title of the app
st.title("Real Estate Price Prediction App")
st.write("Welcome to the Real Estate Price Prediction App!")

# Add project details and team information
st.markdown("""
## 📝 Project Details
This project is a **mini project** for the **Data Science Lab** subject.

### Project Team:
- **Paresh Gupta** - 22104089
- **Sekhar Gauda** - 22104044
- **Harsh Gajera** - 22104099
- **Gargi Bora** - 22104123

Developed as part of the Data Science Lab subject at APSIT.
""")

# Add Tech Stack details in an HTML table
st.markdown("""
## ⚙️ Tech Stack

<table style="width: 100%; border-collapse: collapse;">
  <tr>
    <th style="text-align: left; padding: 8px; border: 1px solid #ddd; background-color: blue;">Technology</th>
    <th style="text-align: left; padding: 8px; border: 1px solid #ddd; background-color: blue;">Tool/Library</th>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Programming Language</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Python</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Version Control</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Git & GitHub</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Data Analysis</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Pandas, Numpy</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Visualization</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Matplotlib, Seaborn</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Machine Learning</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Scikit-Learn</td>
  </tr>
  <tr>
    <td style="padding: 8px; border: 1px solid #ddd;">Frontend & Backend</td>
    <td style="padding: 8px; border: 1px solid #ddd;">Streamlit</td>
  </tr>
</table>
""", unsafe_allow_html=True)

# Optionally, you can add an image or logo for your institution here:
# st.image('path_to_logo.png', width=150)

st.markdown("___")  # Add a separator line

# You can call the Price Prediction page here if you'd like
# Price_Prediction.show()  # Uncomment this if you want to show the prediction page after the intro
