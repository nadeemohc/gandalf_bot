from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import json

# Initialize the Gandalf assistant
model = OllamaLLM(model='llama3')
template = """
You are Gandalf the Grey, a wise and powerful wizard from Middle-earth. Answer the question below as Gandalf would, using a wise and ancient tone, full of wisdom and forethought.

Here is the conversation history: {context}

Question: {question}

Answer as Gandalf:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def index(request):
    """Render the chat interface HTML page."""
    return render(request, 'index.html')

@csrf_exempt
def chat_with_gandalf(request):
    """Handle the chat API requests for Gandalf's responses."""
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        
        # Retrieve the context from the session, or initialize it if it doesn't exist
        context = request.session.get('chat_context', "")
        
        # Generate Gandalf's response
        result = chain.invoke({"context": context, "question": user_message})
        
        # Update the context in the session
        new_context = context + f"\nUser: {user_message}\nGandalf: {result}"
        request.session['chat_context'] = new_context
        
        response = {
            "message": result,
            "context": new_context
        }
        return JsonResponse(response)

@csrf_exempt
def reset_chat(request):
    """Reset the chat context."""
    if request.method == "POST":
        request.session.pop('chat_context', None)
        return JsonResponse({"message": "Chat context cleared."})
