from questionnaire import run_frq, run_mcq
from impact_calculator import calculate_impact
from advisor import generate_advice

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

def generate_intro(impact_level):

    if impact_level == "low":
        return "Your lifestyle already has a relatively low climate impact. " \
               "Here are a few small ways you could reduce it further:"
    elif impact_level == "moderate":
        return "Your climate impact is moderate. " \
               "Here are a few practical ways you could reduce it:"
    else:
        return "Your climate impact is relatively high. " \
               "The following changes could significantly reduce your carbon footprint:"  

if __name__ == "__main__":
    main()