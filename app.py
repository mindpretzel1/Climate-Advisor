import streamlit as st
from questionnaire import QUESTIONS

st.title("Climate Impact Advisor")

question = QUESTIONS["transport"]

prompt = question["prompt"]
options = question["options"]

labels = []
for choice in options:
    value, label = options[choice]
    labels.append(label)

selected_label = st.radio(prompt, labels)

st.write("You selected:", selected_label)