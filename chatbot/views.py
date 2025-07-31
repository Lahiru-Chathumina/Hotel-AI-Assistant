from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .faq_data import faq

@csrf_exempt
def chatbot_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_question = data.get('question', '').lower()
        response = "Sorry, I don't understand the question."
        for key in faq:
            if key in user_question:
                response = faq[key]
                break
        return JsonResponse({"answer": response})
    return JsonResponse({"error": "Invalid method"}, status=400)
