from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

def generate_advice(answers, impact):
    prompt = f"""
    User lifestyle profile:
    {answers}

    Climate impact analysis:
    {impact}

    Provide 3 realitic ways the user could reduce their climate impact.
    Focus especially on the highest imapct categories.PermissionError
    """
    response = client.responses.create(
        model="gpt-5.2",
        input=prompt
    )

    print(response.output_text)