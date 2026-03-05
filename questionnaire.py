def run_questionnaire():
    answers = {}

    transport_choice = input("How do you get to campus usually?\n"
          "Enter the number that best descibes your transportation:\n"
          "1) Walking\n" 
          "2) Bike\n" 
          "3) Bus\n" 
          "4) Car\n" 
          )
    if transport_choice == "1":
        answers["transport"] = "walk"
    elif transport_choice == "2":
        answers["transport"] = "bike"
    elif transport_choice == "3":
        answers["transport"] = "bus"
    elif transport_choice == "4":
        answers["transport"] = "car"
    
    diet_choice = input("How would you describe your usual diet?\n"
          "Enter the number that best describes your diet:\n"
          "1) Vegan\n" 
          "2) Vegetarian\n" 
          "3) Mixed\n" 
          "4) Lots of meat\n" 
          )
    if diet_choice == "1":
        answers["diet"] = "vegan"
    elif diet_choice == "2":
        answers["diet"] = "vegetarian"
    elif diet_choice == "3":
        answers["diet"] = "mixed"
    elif diet_choice == "4":
        answers["diet"] = "meat"

    flight_choice = input("How many flights do you take per year?\n"
          "1) 0 flights\n" 
          "2) 1-2 flights\n" 
          "3) 3-6 flights\n" 
          "4) 7+ flights\n" 
          )
    if flight_choice == "1":
        answers["flights"] = "none"
    elif flight_choice == "2":
        answers["flights"] = "low"
    elif flight_choice == "3":
        answers["flights"] = "medium"
    elif flight_choice == "4":
        answers["flights"] = "high"

    fashion_choice = input("How often do you buy new clothing?\n"
          "Enter the number that best describes your habits:\n"                 
          "1) Rarely (only when needed)\n" 
          "2) A few times per year\n" 
          "3) About once per month\n" 
          "4) Multiple times per month\n" 
          )
    if fashion_choice == "1":
        answers["fashion"] = "rare"
    elif fashion_choice == "2":
        answers["fashion"] = "occasional"
    elif fashion_choice == "3":
        answers["fashion"] = "monthly"
    elif fashion_choice == "4":
        answers["fashion"] = "frequent"

    housing_choice = input("What type of housing do you live in?\n"
        "Enter the number that best describes your housing:\n"
          "1) Small shared housing (dorm/shared apartment)\n" 
          "2) Apartment\n" 
          "3) House with roommates\n" 
          "4) Large single-family home\n" 
          )
    if housing_choice == "1":
        answers["housing"] = "shared"
    elif housing_choice == "2":
        answers["housing"] = "apartment"
    elif housing_choice == "3":
        answers["housing"] = "house_shared"
    elif housing_choice == "4":
        answers["housing"] = "large_home"
    
    return answers
 

print(run_questionnaire())

