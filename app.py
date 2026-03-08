import streamlit as st
import matplotlib.pyplot as plt
from questionnaire import QUESTIONS
from impact_calculator import calculate_impact
from advisor import generate_advice
from display import generate_intro, create_chart

st.title("Climate Impact Advisor")
st.caption("Estimate your climate footprint and get personalized reduction advice.")

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

    for choice in options:
        value, label = options[choice]
        if label == selected_label:
            answers[question_id] = value

profile = st.text_area(
    "(Recommended) Describe your lifestyle", 
    placeholder="student, status, commuting habits, diet, etc"
)

if st.button("Analyze impact"):
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact, profile)
    intro = generate_intro(impact["climate_impact"])

    st.divider()
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
        st.write(f"**{category}**: {value}%")

    st.divider()

    fig = create_chart(percentage_breakdown)

    st.pyplot(fig)
    st.caption("Percent contribution of each category to your total impact score.")

    st.divider()
    st.write(intro)

    st.subheader("Recommendations")
    st.write(advice)