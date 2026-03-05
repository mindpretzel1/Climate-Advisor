from questionnaire import run_questionnaire #temp pipeline until integrated on main

def main():
    answers = run_questionnaire()
    print(calculate_impact(answers))

#Sets scores for questionnaire answers
SCORES = {
"transport": {"walk": 5, "bike": 5, "bus": 15, "car": 30},
"diet": {"vegan": 5, "vegetarian": 10, "mixed": 20, "meat": 30},
"flights": {"none": 0, "low": 10, "medium": 20, "high": 30},
"fashion": {"rare": 5, "occasional": 10, "monthly": 20, "frequent": 30},
"housing": {"shared": 5, "apartment": 10, "house_shared": 20, "large_home": 30},
}
MAX_SCORE = 0 #Max possible score based on questionnaire
for options in SCORES.values():
    MAX_SCORE += max(options.values())

'''
Example of 'answers' structure: 
{'transport': 'walk', 
'diet': 'vegetarian', 
'flights': 'medium', 
'fashion': 'frequent', 
'housing': 'large_home'}
'''
def calculate_impact(answers):
    impact = {}

    score_breakdown = {}
    total_score = 0

    highest_categories = []
    highest_choice = 0
    
    for category in answers.keys():
        choice = answers[category]
        
        val = SCORES[category][choice]
        total_score += val
        score_breakdown[category] = val

        if val > highest_choice: 
            highest_choice = val
            highest_categories = [category]

        elif val == highest_choice:
            highest_categories.append(category)

    impact["total_score"] = total_score
    impact["max_score"] = MAX_SCORE
    impact["score_breakdown"] = score_breakdown
    impact["highest_categories"] = highest_categories

    if total_score > 100:
        impact["climate_impact"] = "high"
    elif total_score > 50:
        impact["climate_impact"] = "moderate"
    else:
        impact["climate_impact"] = "low"

    return impact

if __name__ == "__main__":
    main()

