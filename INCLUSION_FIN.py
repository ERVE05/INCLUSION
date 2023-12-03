import pandas as pd
import numpy as np
import streamlit as st



st.title("INCLUSION FINANCIERE")
st.subheader( 'inclusion financiere en Afrique')
st.write("Cette application permet de prédire si l'individu est susceptible d'ouvrir un compte bancaire.\n")
st.header("Prédire si le client va ouvrir un compte ou non")

# Chargez le modèle depuis le fichier
with open("clf_inclusion.pkl", 'rb') as model_file:


# Fonction de prediction
 def predict_bank_account(feature):
    input_data = pd.DataFrame(feature, index=[0])
  # Créez un DataFrame à partir de la fonctionnalité d'entrée
    prediction = model.predict(input_data)
    return prediction[0]

# Creation de l'application web via streamlit
 def main():
    # Le titre
    #st.title("Application de prediction d'ouverture de compte bancaire")
    # Description
    st.write("Cette application permet de prédire si l'individu est susceptible d'ouvrir un compte bancaire.\n")
    st.header("Prédire si le client va ouvrir un compte ou non")

    age = st.slider("Age: ", 24, 100)
    # Modifiez la plage d'âge en fonction de vos données
    household_size = st.slider("Household Size: ", 1, 21)
    # Modifiez la plage en fonction de vos données
    year = st.selectbox("Year: ", ['2016', '2017', '2018'])
    # Modifiez les années en fonction de vos données
    age_of_respondent = st.slider("Age of Respondent: ", 16, 100)
    # Modifiez la plage d'âge en fonction de vos données
    country = st.multiselect("Country : ", ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
    location_type = st.multiselect("Location Type: ", ['Rural', 'Urban'])
    cellphone_access = st.multiselect("Cellphone Access :", ['Yes', 'No'])
    gender_of_respondent = st.multiselect("Gender of Respondent: ", ['Female', 'Male'])
    relationship_with_head = st.multiselect("Relationship with Head: ",
                                            ['Spouse', 'Head of Household', 'Other relative', 'Child', 'Parent',
                                             'Other non-relatives'])
    marital_status = st.selectbox("Marital Status: ",
                                  ['Married/Living together', 'Widowed', 'Single/Never Married', 'Divorced/Seperated',
                                   'Dont know'])
    education_level = st.selectbox("Education Level :",
                                   ['Secondary education', 'No formal education', 'Vocational/Specialised training',
                                    'Primary education', 'Tertiary education', 'Other/Dont know/RTA'])
    job_type = st.multiselect("Job Type :", ['Self employed', 'Government Dependent', 'Formally employed Private',
                                             'Informally employed', 'Formally employed Government',
                                             'Farming and Fishing', 'Remittance Dependent', 'Other Income',
                                             'Dont Know/Refuse to answer', 'No Income'])
if __name__=='__main__':
    main()

