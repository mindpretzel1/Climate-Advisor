from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def generate_advice(answers, impact, profile):
    prompt = f"""
    You are a practical climate advisor helping a user reduce their carbon footprint.

    User profile (optional context, ignore if irrelevant):
    {profile}

    User lifestyle data:
    {answers}

    Impact analysis:
    Total score: {impact["total_score"]}/{impact["max_score"]}
    Impact breakdown by category:
    {impact["score_breakdown"]}

    Highest impact categories:
    {impact["highest_categories"]}

    Task:
    Provide exactly 3 realistic actions the user could take to reduce their climate impact.

    Rules:
    - Focus primarily on the highest impact categories.
    - Suggestions must address different behaviors when possible.
    - At least one suggestion should address a category other than the highest when possible.
    - Avoid recommending actions the user already does.
    - Each suggestion must be 1-2 sentences.
    - Number the suggestions 1-3.
    - Do not include introductions or explanations.
    - Do not repeat the prompt or add extra commentary.
    """
    response = client.responses.create(
        model="gpt-5.2",
        input=prompt
    )

    return response.output_text