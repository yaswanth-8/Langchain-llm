import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is you pet?", ("Cat", "Dog", "Cow", "Hamster"))

if animal_type == "Cat" :
    animal_color = st.sidebar.text_area("What color is your cat?", max_chars=15)

if animal_type == "Dog" :
    animal_color = st.sidebar.text_area("What color is your dog?", max_chars=15)

if animal_type == "Cow" :
    animal_color = st.sidebar.text_area("What color is your cow?", max_chars=15)

if animal_type == "Hamster" :
    animal_color = st.sidebar.text_area("What color is your hamster?", max_chars=15)

if animal_color :
    response = lch.generate_pet_name(animal_type, animal_color)
    st.text(response['pet_name'])
