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
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact, profile)
    intro = generate_intro(impact["climate_impact"])

    st.header("Results")

    st.metric(
        "Climate Impact Score",
        f"{impact['percent_score']}%"
    )
    st.write(f"Impact Level: {impact['climate_impact']}")

    percentage_breakdown = {}
    for category in impact["score_breakdown"]:
        value = impact["score_breakdown"][category]

        if impact["total_score"] > 0:
            percent = (value / impact["max_score"]) * 100
        else:
            percent = 0
        
        percentage_breakdown[category.capitalize()] = round(percent, 1)

    st.subheader("Score Breakdown")

    for category in percentage_breakdown:
        value = percentage_breakdown[category]
        st.write(f"{category}: {value}%")

    st.bar_chart(percentage_breakdown)
    st.write(intro)

    st.subheader("Recommendations")
    st.write(advice)