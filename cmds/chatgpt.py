import openai
import sys
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

openai.api_key = "xxx" # replace with your API key

def get_answer(question):
    # set up the OpenAI API request
    prompt = f"{question}"
    model = "text-davinci-002"
    temperature = 0.5
    max_tokens = 500

    # generate the answer using the OpenAI API
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    # extract the generated answer from the API response
    answer = response.choices[0].text.strip()

    return answer

if __name__ == '__main__':
    question = ' '.join(sys.argv[1:]) # get the question from the command line argument
    answer = get_answer(question)
    print(answer)
    engine.say(answer)
    engine.runAndWait()
