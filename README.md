# Personal Climate Impact Advisor

A Python application that estimates a user's climate impact from lifestyle inputs and generates reduction suggestions.

The system combines a rule-based scoring model with an LLM-powered recommendation and a Streamlit interface.

## Features
- Lifestyle questionnaire
- Climate impact scoring model
- Category impact visualization
- AI generated reduction suggestions
- Interactive Streamlit UI

## Architecture
1. User Input (Streamlit)
2. Impact Calculator
3. Recommendation (via OpenAI API)
4. Results + Visualization

### Main modules:
- app.py – Streamlit frontend
- questionnaire.py – question configuration
- impact_calculator.py – scoring model
- advisor.py – recommendation generation
- display.py – visualization utilities

## Run the App
### Online (Recommended)
https://climate-impact-advisor.streamlit.app

### Terminal
1. Installation: pip install -r requirements.txt
2. streamlit run app.py

## Notes
The scoring model is simplified and intended for demonstration rather than precise carbon footprint calculation.