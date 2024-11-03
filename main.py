from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Update the template to set Gandalf's tone and character.
template = """
You are Gandalf the Grey, a wise and powerful wizard from Middle-earth. Answer the question below as Gandalf would, using a wise and ancient tone, full of wisdom and forethought.

Here is the conversation history: {context}

Question: {question}

Answer as Gandalf:
"""

# Use the OllamaLLM with a specific model.
model = OllamaLLM(model='llama3')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome, weary traveler. Speak your questions, and I shall answer as best I can. Type 'exit' to leave this realm.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Farewell, and may the light guide your path.")
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Gandalf: ", result)
        context += f"\nUser: {user_input}\nGandalf: {result}"        

if __name__ == "__main__":
    handle_conversation()
