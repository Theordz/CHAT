
import streamlit as st
from PIL import Image
st.header("Ai Tool for Meal suggestions", divider='gray')
st.subheader("By Spencer, Joel, and Theo")
PROGRAM = "ON"
if PROGRAM == "ON":
    button_clicked = st.button('Click here to access AI', key=f"{'yes'}")
    if button_clicked:
        import requests
        st.markdown(requests.__file__)
        r = requests.get('https://chat.openai.com/')
        st.markdown (r.url)
        st.markdown("Paste the following prompt when you enter the website: 'Speak like you are a chef making meals based off what the user gives you'")
        st.markdown("Please open the blue link.")
        
        PROGRAM == "OFF"
        quit()    
