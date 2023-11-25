
import numpy as np
import pandas as pd
from pathlib import Path
import joblib 
import mlflow
import streamlit as st 



def predict_with_joblib(data):
    model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
    predicted_qualities=model.predict(data)
    return predicted_qualities



def predict_with_mlflow(data):
    logged_model = 'runs:/544b03c9f3f44cb9b496c0e9dbaa13ab/model'
    # Load model as a PyFuncModel.
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    # Predict on a Pandas DataFrame.
    predicted_qualities=loaded_model.predict(pd.DataFrame(data))
    return predicted_qualities


def main():
    st.title("Wine Quality")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Wine Quality tML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    fixed_acidity= st.text_input("fixed acidity",0.0)
    volatile_acidity = st.text_input("volatile acidity",0.0)
    citric_acid = st.text_input("citric acid",0.0)
    residual_sugar = st.text_input("residual sugar",0.0)
    free_sulfur_dioxide= st.text_input("free sulfur dioxide",0.0)
    total_sulfur_dioxide= st.text_input("total sulfur dioxide",0.0) 
    density= st.text_input("density",0.0)
    pH= st.text_input("pH",0.0) 
    sulphates= st.text_input("sulphates",0.0)
    alcohol= st.text_input("alcohol",0.0) 
    quality= st.text_input("quality",0.0)

    result=""

    input_values = [float(x) for x in[fixed_acidity
    ,volatile_acidity
    ,citric_acid 
    ,residual_sugar 
    ,free_sulfur_dioxide
    ,total_sulfur_dioxide
    ,density
    ,pH
    ,sulphates
    ,alcohol
    ,quality]]

    data = [input_values]

    if st.button("Predict"):
        result=predict_with_mlflow(data)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()


