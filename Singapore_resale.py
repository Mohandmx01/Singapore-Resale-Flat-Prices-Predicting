# Packages

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from PIL import Image

# Streamlit

st.set_page_config(layout="wide")

st.markdown(
    f""" <style>.stApp {{
                    background:url("https://wallpapers.com/images/high/dark-gradient-quwlcn6vowfuwug1.webp");
                    background-size:cover}}
                 </style>""",
    unsafe_allow_html=True
)

st.title(":orange[Singapore Resale Flat Price Predictor]")

st.write("")

with st.sidebar:
    select= option_menu("MENU",["Home", "Price Prediction","About"],
                        icons=["house", "calculator", "book"],
                        menu_icon="cast",
                        default_index=0)

 # Functions

def town_mapping(town_map):
    if town_map == 'ANG MO KIO':
        town_1 = int(0)
    elif town_map == 'BEDOK':
        town_1 = int(1)
    elif town_map == 'BISHAN':
        town_1= int(2)
    elif town_map == 'BUKIT BATOK':
        town_1= int(3)
    elif town_map == 'BUKIT MERAH':
        town_1= int(4)
    elif town_map == 'BUKIT PANJANG':
        town_1= int(5)

    elif town_map == 'BUKIT TIMAH':
        town_1= int(6)
    elif town_map == 'CENTRAL AREA':
        town_1= int(7)
    elif town_map == 'CHOA CHU KANG':
        town_1= int(8)
    elif town_map == 'CLEMENTI':
        town_1= int(9)
    elif town_map == 'GEYLANG':
        town_1= int(10)
    
    elif town_map == 'HOUGANG':
        town_1 = int(11)
    elif town_map == 'JURONG EAST':
        town_1= int(12)
    elif town_map == 'JURONG WEST':
        town_1= int(13)
    elif town_map == 'KALLANG/WHAMPOA':
        town_1= int(14)
    elif town_map == 'MARINE PARADE':
        town_1= int(15)

    elif town == 'PASIR RIS':
        town_1= int(16)
    elif town == 'PUNGGOL':
        town_1= int(17)
    elif town == 'QUEENSTOWN':
        town_1= int(18)
    elif town == 'SEMBAWANG':
        town_1= int(19)
    elif town == 'SENGKANG':
        town_1= int(20)

    elif town == 'SERANGOON':
        town_1= int(21)
    elif town == 'TAMPINES':
        town_1= int(22)
    elif town == 'TOA PAYOH':
        town_1= int(23)
    elif town == 'WOODLANDS':
        town_1= int(24)        
    elif town == 'YISHUN':
        town_1= int(25)      

    return town_1

def flat_type_mapping(flt_type):

    if flt_type == '3 ROOM':
        flat_type_1= int(2)
    elif flt_type == '4 ROOM':
        flat_type_1= int(3)
    elif flt_type == '5 ROOM':
        flat_type_1= int(4)
    elif flt_type == '2 ROOM':
        flat_type_1= int(1)
    elif flt_type == 'EXECUTIVE':
        flat_type_1= int(5)
    elif flt_type == '1 ROOM':
        flat_type_1= int(0)
    elif flt_type == 'MULTI-GENERATION':
        flat_type_1= int(6)

    return flat_type_1

def flat_model_mapping(fl_m):

    if fl_m == 'Improved':
        flat_model_1= int(5)
    elif fl_m == 'New Generation':
        flat_model_1= int(12)
        
    elif fl_m == 'Model A':
        flat_model_1= int(8)
    elif fl_m == 'Standard':
        flat_model_1= int(17)
    elif fl_m == 'Simplified':
        flat_model_1= int(16)
    elif fl_m == 'Premium Apartment':
        flat_model_1= int(13)
    elif fl_m == 'Maisonette':
        flat_model_1= int(7)

    elif fl_m == 'Apartment':
        flat_model_1= int(3)
    elif fl_m == 'Model A2':
        flat_model_1= int(10)
    elif fl_m == 'Type S1':
        flat_model_1= int(19)
    elif fl_m == 'Type S2':
        flat_model_1= int(20)
    elif fl_m == 'Adjoined flat':
        flat_model_1= int(2)

    elif fl_m == 'Terrace':
        flat_model_1= int(18)
    elif fl_m == 'DBSS':
        flat_model_1= int(4)
    elif fl_m == 'Model A-Maisonette':
        flat_model_1= int(9)
    elif fl_m == 'Premium Maisonette':
        flat_model_1= int(15)
    elif fl_m == 'Multi Generation':
        flat_model_1= int(11)

    elif fl_m == 'Premium Apartment Loft':
        flat_model_1= int(14)
    elif fl_m == 'Improved-Maisonette':
        flat_model_1= int(6)
    elif fl_m == '2-room':
        flat_model_1= int(0)
    elif fl_m == '3Gen':
        flat_model_1= int(1)

    return flat_model_1


def predict_price(year,town,flat_type,flr_area_sqm,flat_model,stry_start,stry_end,re_les_year,
                  re_les_month,les_coms_dt):
    
    year_1= int(year)
    town_2= town_mapping(town)
    flt_ty_2= flat_type_mapping(flat_type)
    flr_ar_sqm_1= int(flr_area_sqm)
    flt_model_2= flat_model_mapping(flat_model)
    str_str= np.log(int(stry_start))
    str_end= np.log(int(stry_end))
    rem_les_year= int(re_les_year)
    rem_les_month= int(re_les_month)
    lese_coms_dt= int(les_coms_dt)


    with open(r"C:/Users/Mohan.S/Desktop/Mohan_Project/Singapore/Resale_Flat_Prices_Model_1.pkl","rb") as f:
        regg_model= pickle.load(f)

    user_data = np.array([[year_1,town_2,flt_ty_2,flr_ar_sqm_1,
                           flt_model_2,str_str,str_end,rem_les_year,rem_les_month,
                           lese_coms_dt]])
    y_pred_1 = regg_model.predict(user_data)
    price= np.exp(y_pred_1[0])

    return round(price)

# Streamlit Continuation

if select == "Home":

    st.header(":green[Documentation and Instructions for Using the Application:]")

    st.subheader(":blue[Introduction:]")

    st.write("The Singapore Resale Flat Prices Predicting application is designed to provide users with a tool for predicting resale prices of HDB flats in Singapore based on various input parameters. Users can navigate through two main sections: 'Home' and 'Price Prediction'.")

    st.header(":violet[Usage Instructions:]")

    st.subheader(":blue[Home Section:]")

    st.write("1. This section provides general information about HDB flats in Singapore and the resale process.")

    st.write("2. It covers steps involved in the resale process, eligibility criteria, grant schemes, financing options, market trends, and online platforms for listing and browsing resale flats.")

    st.subheader(":blue[Price Prediction Section:]")

    st.write("1. Year Selection: Choose the year for which you want to make the prediction.")

    st.write("2. Town Selection: Select the town where the HDB flat is located.")

    st.write("3. Flat Type: Choose the type of flat (e.g., 3 ROOM, 4 ROOM, etc.).")

    st.write("4. Floor Area (sqm): Enter the floor area of the flat in square meters.")

    st.write("5. Flat Model: Select the model of the flat.")

    st.write("6. Storey Start and End: Enter the storey start and end values for the flat.")

    st.write("7. Remaining Lease: Enter the remaining lease year and month.")
    
    st.write("8. Lease Commencement Date: Select the lease commencement date of the flat.")

    st.subheader(":blue[Predict the Price:]")

    st.write("1. After entering the required information, click the Predict the Price button.")

    st.write("2. The predicted price of the resale flat will be displayed.")


elif select == "Price Prediction":

    st.divider()

    col1,col2= st.columns(2)

    with col1:

        year= st.selectbox("Select the Year",["2015", "2016", "2017", "2018", "2019", "2020", "2021",
                           "2022", "2023", "2024"])
        
        town= st.selectbox("Select the Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                            'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                                            'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                            'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                                            'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                                            'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
        
        flat_type= st.selectbox("Select the Flat Type", ['3 ROOM', '4 ROOM', '5 ROOM', '2 ROOM', 'EXECUTIVE', '1 ROOM',
                                                        'MULTI-GENERATION'])
        
        flr_area_sqm= st.number_input("Enter the Value of Floor Area sqm (Min: 31 / Max: 280")

        flat_model= st.selectbox("Select the Flat Model", ['Improved', 'New Generation', 'Model A', 'Standard', 'Simplified',
                                                        'Premium Apartment', 'Maisonette', 'Apartment', 'Model A2',
                                                        'Type S1', 'Type S2', 'Adjoined flat', 'Terrace', 'DBSS',
                                                        'Model A-Maisonette', 'Premium Maisonette', 'Multi Generation',
                                                        'Premium Apartment Loft', 'Improved-Maisonette', '2-room', '3Gen'])
        
    with col2:

        stry_start= st.number_input("Enter the Value of Storey Start")

        stry_end= st.number_input("Enter the Value of Storey End")

        re_les_year= st.number_input("Enter the Value of Remaining Lease Year (Min: 42 / Max: 97)")

        re_les_month= st.number_input("Enter the Value of Remaining Lease Month (Min: 0 / Max: 11)")
        
        les_coms_dt= st.selectbox("Select the Lease_Commence_Date", [str(i) for i in range(1966,2023)])

    button= st.button(":green[Predict the Price]", use_container_width= True)

    if button:

            
        pre_price= predict_price(year, town, flat_type, flr_area_sqm, flat_model,
                        stry_start, stry_end, re_les_year, re_les_month, les_coms_dt)

        st.write("## :green[**The Predicted Price is :**]",pre_price)

elif select == "About":

    st.divider()

    st.header(":green[Technologies Used:]")

    st.write("Python, Streamlit, Pandas, NumPy, Scikit-learn, Pickle, PIL(Python Imaging Library)")

    st.header(":red[Project Report Summary:]")

    st.subheader(":blue[1. Introduction:]")

    st.write("The project aimed to develop a predictive model for estimating resale prices of HDB flats in Singapore. The project involved data analysis, model development, and deployment of a Streamlit application.")

    st.subheader(":blue[2. Data Analysis:]")

    st.write("Dataset: The dataset contained historical data of resale flat transactions in Singapore.")

    st.write("Exploratory Data Analysis (EDA): Conducted to understand the distribution of data, identify patterns, and explore relationships between features and target variable.")

    st.subheader(":blue[3. Model Development:]")

    st.write("Feature Engineering: Preprocessed the data and engineered features such as town mapping, flat type mapping, and flat model mapping.")

    st.write("Machine Learning Model: Developed a regression model using Scikit-learn to predict resale flat prices based on input features.")

    st.write("Model Evaluation: Evaluated the model's performance using appropriate metrics and fine-tuned hyperparameters for better performance.")

    st.subheader(":blue[4. Deployment Process:]")

    st.write("Developed a Streamlit application for user interaction.")

    st.write("Integrated the trained machine learning model into the application.")

    st.write("Provided user-friendly interface with interactive widgets for inputting parameters.")

    st.write("Deployed the application to a web server for public access.")

    st.subheader(":blue[5. Conclusion:]")

    st.write("The project successfully developed and deployed a predictive model for estimating resale prices of HDB flats in Singapore. The Streamlit application provides a user-friendly interface for users to predict resale prices based on various input parameters. Further improvements and enhancements can be made to the model and application based on feedback and additional data sources.")
