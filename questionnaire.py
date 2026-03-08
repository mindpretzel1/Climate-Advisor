QUESTIONS = {
    "transport":{
        "prompt": "How do you get to campus usually?",
        "options": {
            "1": ("walk", "Walking"),
            "2": ("bike", "Bike"),
            "3": ("bus", "Bus"),
            "4": ("car", "Car")
        }
    },
    "diet": {
        "prompt": "How would you describe your usual diet?",
        "options": {
            "1": ("vegan", "Vegan"),
            "2": ("vegetarian", "Vegetarian"),
            "3": ("mixed", "Mixed"),
            "4": ("meat", "Lots of meat")
        }
    },
    "flights": {
        "prompt": "How many flights do you take per year?",
        "options": {
            "1": ("none", "0 flights"),
            "2": ("low", "1-2 flights"),
            "3": ("medium", "3-6 flights"),
            "4": ("high", "7+ flights")
        }
    },
    "clothing": {
        "prompt": "How often do you buy new clothing?",
        "options": {
            "1": ("rare", "Rarely (only when needed)"),
            "2": ("occasional", "A few times per year"),
            "3": ("monthly", "About once per month"),
            "4": ("frequent", "Multiple times per month")
        }
    },
    "housing": {
        "prompt": "What type of housing do you live in?",
        "options": {
            "1": ("shared", "Small shared housing (dorm/shared apartment)"),
            "2": ("apartment", "Apartment"),
            "3": ("house_shared", "House with roommates"),
            "4": ("large_home", "Large single-family home")
        }
    }
}

def run_mcq():
    answers = {}

    for question_id in QUESTIONS: #transport, diet, clothing, etc
        question = QUESTIONS[question_id]
        options = question["options"]

        print(question["prompt"])

        for choice in options: #1, 2, 3, etc
            value, label = options[choice]

            print(f"{choice}: {label}")

        answer = input()

        value, label = options[answer]
        answers[question_id] = value
    
    return answers
 
def run_frq():
    profile = input(
        "\n(Recommended) Briefly describe your lifestyle "
        "(student status, commuting habits, budget, etc):\n"
    )
    return profile

