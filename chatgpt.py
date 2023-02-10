import os
import openai

def askChatGpt(question):
    print(question)
    # print("question length=", len(question))
    # Load your API key from an environment variable or secret management service
    openai.api_key = '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'

    try:
        response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=1, max_tokens=4000)
        # print(response)

        text = response["choices"][0]["text"]
        print(text)
        return text

    except:
        return "Question is too long. ChatGPT can't response"
    
    


