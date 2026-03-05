from questionnaire import run_frq, run_mcq
from impact_calculator import calculate_impact
from advisor import generate_advice

def main():
    answers = run_mcq()
    profile = run_frq()
    impact = calculate_impact(answers)
    advice = generate_advice(answers, impact, profile)

    print(impact)
    print(advice)

if __name__ == "__main__":
    main()