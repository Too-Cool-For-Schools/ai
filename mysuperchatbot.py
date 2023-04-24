import openai
openai.api_key = "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"

def ask_gpt3(question, model_engine="text-davinci-003"):
    prompt = f"Conversation with GPT-3:\n\nUser: {question}\nGPT-3:"
    response = openai.Completion.create(
        engine=model_engine, 
        prompt=prompt, 
        max_tokens=4000,
        n=1, 
        stop=None, 
        temperature=1,
    )

    message = response.choices[0].text.strip()
    return message

print("Hello! I'm your chat bot. How can I help you today?")

while True:
    user_input = input("> ")
    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye!")
    elif user_input.lower() in ["kiss", "wanna kiss me baby", "exit"]:
        print("Go to hell")
        break
    else:
        response = ask_gpt3(user_input)
        print(response)