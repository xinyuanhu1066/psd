'''Chatbot using Gemini API'''

from google import genai
from google.genai import types


client = genai.Client()


def chatbot():
    '''Command line chatbot.'''
    print('\nWelcome to AI powered Itinerary Planner!\n')
    city = input('Which city are you going to? ').strip()
    days = input('How many days are you going to stay? ').strip()
    age = input('How old are you? ').strip()

    prompt = (
        'The user provides:\n'
        f'city: {city}\n'
        f'days: {days}\n'
        f'age: {age}\n'
        'Based on your personal information, '
        'Then, give a structured itinerary with a name of the place, '
        'address and short description for each day seperatly in order with maximom three activities in a day.'
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction='You are a professional itinerary recommender.',
            temperature=0.7,
        ),
        contents=prompt,
    )
    print(response.text)


if __name__ == '__main__':
    chatbot()