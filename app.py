"""
CREATED BY: AISHWARYA MATE
"""
import pickle
import streamlit as st 

loaded_model = open("gb_model.pkl","rb")
predictor = pickle.load(loaded_model)

def welcome():
    return "Welcome All"

def predict_premium(age,sex,bmi,children,smoker,region):
    prediction = predictor.predict([[age,sex,bmi,children,smoker,region]])
    print(prediction)
    return prediction
def main():
    st.title("Premium Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Health Insurance Premium Prediction </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.number_input("age",min_value=0,max_value=100)
    
    sex = st.selectbox("sex", ('female','male'))
    
    bmi = st.number_input("bmi",min_value=0.0,max_value=50.0)
    
    children = st.selectbox("children", ('0','1','2','3','4','5'))
    
    smoker = st.selectbox("smoker", ('yes','no'))
    
    region = st.selectbox("region", ('northwest','northeast','southwest','southeast'))
    
    
    result = ""
    if st.button("Predict"):
        result=predict_premium(age,sex,bmi,children,smoker,region)
    st.success('The Predicted Health Insurance Premium is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__== '__main__':
    main()
    
    