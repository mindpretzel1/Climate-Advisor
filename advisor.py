from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def generate_advice(answers, impact, profile):
    prompt = f"""
    You are a climate advisor helping a user reduce their carbon footprint.
    User self reported profile (if response is not useful, ignore it):
    {profile}

    User lifestyle data:
    {answers}

    Impact analysis:
    Total score: {impact["total_score"]}/{impact["max_score"]}
    Highest impact categories: {impact["highest_categories"]}

    Provide exactly 3 suggestions to reduce impact.

    Rules:
    - Focus primarily on the highest impact categories.
    - Each suggestion must be 2 sentences or fewer.
    - Number the suggestions 1-3.
    - Do not repeat the introduction.
    - Do not add extra commentary.
    """
    response = client.responses.create(
        model="gpt-5.2",
        input=prompt
    )

    print(response.output_text)