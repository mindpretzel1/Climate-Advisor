import streamlit as st
from questionnaire import QUESTIONS
from impact_calculator import calculate_impact
from advisor import generate_advice
from display import generate_intro

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

profile = st.text_area(
    "Describe your lifestyle", 
    placeholder="student, status, commuting habits, diet, etc"
)

if st.button("Analyze impact"):
    st.write("DEBUG answers:", answers)
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact, profile)
    intro = generate_intro(impact["climate_impact"])

    st.header("Results")

    st.metric(
        "Climate Impact Score",
        f"{impact['total_score']} / {impact['max_score']}"
    )
    st.write(f"Impact Level: {impact['climate_impact']}")

    st.subheader("Score Breakdown")

    for category in impact["score_breakdown"]:
        value = impact["score_breakdown"][category]
        st.write(f"{category}: {value}")

    st.write(intro)

    st.subheader("Recommendations")
    st.write(advice)