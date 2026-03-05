from questionnaire import run_questionnaire
from impact_calculator import calculate_impact
from advisor import generate_advice

def main():
    answers = run_questionnaire()
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact)

    print(impact)
    print(advice)

if __name__ == "__main__":
    main()