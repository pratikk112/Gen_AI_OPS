import streamlit as st
from imggenOai import *
st.title("Welcome to My Image generator")
st.write("Here you can just enter the prompt and can get the image.")





if st.button("image generation using prompt"):
    st.info("ok i will generate the image")
    prompt = st.text_input("Enter your prompt for image generation")
    if prompt:
        gen_img = generate_img(prompt)
    if gen_img is not None:
        st.image(gen_img, caption="generated image")
    

if st.button("image generation using image and mask"):
    st.info("ok i will generate the image using mask and image provided")
    base_image_path = st.file_uploader("Upload base image", type=["png", "jpg", "jpeg"])
    mask_image_path = st.file_uploader("Upload mask image", type=["png", "jpg", "jpeg"])
    prompt = st.text_input("Enter your prompt for image generation")
    
    gen_img = generate_image_with_mask(base_image_path,mask_image_path,prompt)
    if gen_img is not None:
        st.image(gen_img, caption="generated image")
        
        
if st.button("image variation generation"):
    st.info("ok i will generate the image variation")
    base_image_path = st.file_uploader("upload the image for variation")
    gen_img = creating_variation(base_image_path)
    if gen_img is not None:
        st.image(gen_img, caption="generated image")