import streamlit as st
from questionnaire import QUESTIONS
from impact_calculator import calculate_impact
from advisor import generate_advice

st.title("Climate Impact Advisor")

answers = {}

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
    for choice in options:
        value, label = options[choice]
        if label == selected_label:
            answers[question_id] = value

    answers[question_id] = value

profile = st.text_area(
    "Describe your lifestyle", 
    placeholder="student, status, commuting habits, diet, etc"
)

if st.button("Analyze impact"):
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact, profile)

    st.write(impact)
    st.write(advice)