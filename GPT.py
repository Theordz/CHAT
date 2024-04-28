
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
        r = requests.get('https://chat.openai.com/c/7acbb239-6602-412e-a542-7b2925f9777b')
        st.markdown (r.url)
        st.markdown("Please open the blue link.")
        PROGRAM == "OFF"
        quit()    
