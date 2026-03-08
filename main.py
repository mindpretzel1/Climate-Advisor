from questionnaire import run_frq, run_mcq
from impact_calculator import calculate_impact
from advisor import generate_advice
from display import generate_intro

def main():
    answers = run_mcq()
    profile = run_frq()
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact, profile)
    display_result(impact, advice)

def display_result(impact, advice):
    print(f"Climate Impact Score: {impact['total_score']} / {impact['max_score']}")
    print(f"Impact Level: {impact['climate_impact']}")

    print("\nScore Breakdown:")
    for category in impact["score_breakdown"]:
        value = impact["score_breakdown"][category]
        print(f"- {category}: {value}")
    
    print(generate_intro(impact["climate_impact"]))
    print("\nRecommendations:")
    print(advice)

if __name__ == "__main__":
    main()