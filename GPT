import streamlit as st
from PIL import Image
image = Image.open('Downloads/WOW.png')
st.header("Ai Tool for Meal suggestions", divider='gray')
st.subheader("By Spencer, Joel, and Theo")
PROGRAM = "ON"
if PROGRAM == "ON":
    button_clicked = st.button('Click here to access AI', key=f"{'yes'}")
    if button_clicked:
        import requests
        st.markdown(requests.__file__)
        r = requests.get('https://chat.openai.com/c/455ea111-016d-4fe8-88b7-3b48d5511f7b')
        st.markdown (r.url)
        st.markdown("Please open the blue link.")
        PROGRAM == "OFF"
        quit()    
st.image(image)
