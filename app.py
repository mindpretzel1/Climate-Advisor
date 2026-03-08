import streamlit as st
from questionnaire import QUESTIONS

st.title("Climate Impact Advisor")

for question_id in QUESTIONS:
    question = QUESTIONS[question_id]
    prompt = question["prompt"]
    options = question["options"]

    labels = []
    for choice in options:
        value, label = options[choice]
        labels.append(label)

    selected_label = st.radio(prompt, labels, key=question_id)

    st.write("You selected:", selected_label)