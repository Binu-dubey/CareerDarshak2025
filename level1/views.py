from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Option, UserResponse, TraitScore, MLPredictionResult
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import json
import logging
import joblib
import os
from django.conf import settings
from .utils.personality_profiles import get_personality_insights

# MODEL_PATH = os.path.join(settings.BASE_DIR, "ml_model", "personality_model.pkl")
# ENCODER_PATH = os.path.join(settings.BASE_DIR, "ml_model", "personality_encoder.pkl")

# model = joblib.load(MODEL_PATH)
# encoder = joblib.load(ENCODER_PATH)
# print(type(model))  # Add temporarily


logger = logging.getLogger(__name__)

from django.http import JsonResponse
avatars = [
    {"filename": "avatar1.png", "name": "The Thinker"},
    {"filename": "avatar2.png", "name": "The Visionary"},
    {"filename": "avatar3.png", "name": "The Creator"},
    {"filename": "avatar4.png", "name": "The Strategist"},
    {"filename": "avatar5.png", "name": "The Helper"},
    {"filename": "avatar6.png", "name": "The Explorer"},
    {"filename": "avatar7.png", "name": "The Leader"},
    {"filename": "avatar8.png", "name": "The Innovator"},
]
@login_required
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to homepage
    return render(request, 'login.html')
@login_required
def level1_intro(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'level1/intro.html')
@login_required
def level1_view(request):
    questions = Question.objects.all().order_by('question_number').prefetch_related('options')

    formatted_questions = []
    for question in questions:
        options = list(question.options.all())
        formatted_questions.append({
            'id': question.id,
            'question_number': question.question_number,
            'question_text': question.question_text,
            'options': [{'id': opt.id, 'text': opt.text} for opt in options]
        })

    return render(request, 'level1/level1.html', {
        'questions': questions,
        'formatted_questions': json.dumps(formatted_questions)
    })


@login_required
def submit_level1(request):
    if request.method == 'POST':
        user = request.user

        # Clear previous data
        UserResponse.objects.filter(user=user).delete()
        TraitScore.objects.filter(user=user).delete()

        # Save new user responses
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = key.split('_')[1]
                try:
                    selected_option = Option.objects.get(id=int(value))
                    question = Question.objects.get(id=question_id)
                    UserResponse.objects.create(user=user, question=question, selected_option=selected_option)
                except (Option.DoesNotExist, Question.DoesNotExist, ValueError):
                    continue

        # Calculate trait scores
        trait_scores = {}
        for response in UserResponse.objects.filter(user=user).select_related('selected_option', 'question'):
            trait = response.question.trait
            trait_scores[trait] = trait_scores.get(trait, 0) + response.selected_option.score

        for trait, score in trait_scores.items():
            TraitScore.objects.create(user=user, trait=trait, score=score)

        # ML Prediction input
        input_array = [[
            trait_scores.get("Self-Learning", 0),
            trait_scores.get("Introvert-Extrovert", 0),
            trait_scores.get("Teamwork", 0),
            trait_scores.get("Toughness", 0),
            trait_scores.get("Work Style", 0)
        ]]

        try:
            pred_encoded = model.predict(input_array)[0]
            personality = encoder.inverse_transform([pred_encoded])[0]
        except Exception as e:
            print("Prediction Error:", e)
            personality = "Unknown"

        insights = get_personality_insights(personality)

        # Save prediction result
        MLPredictionResult.objects.update_or_create(
            user=user,
            defaults={
                'predicted_personality': personality,
                'description': insights["description"],
                'key_strengths': json.dumps(insights["key_strengths"]),
                'growth_areas': json.dumps(insights["growth_areas"]),
                'radar_scores': json.dumps(trait_scores)
            }
        )

        return render(request, 'level1/submit_level1.html', {"personality": personality})


    return redirect('level1')


def personality_assessment_result(request):
    return render(request, 'level1/personality_assessment_result.html')

@login_required
def level1_result(request):
    user = request.user
    try:
        prediction = MLPredictionResult.objects.get(user=user)
        radar_data = json.loads(prediction.radar_scores)
        strengths = json.loads(prediction.key_strengths)
        growth_areas = json.loads(prediction.growth_areas)
    except MLPredictionResult.DoesNotExist:
        prediction = None
        radar_data = {}
        strengths = []
        growth_areas = []

    context = {
        "prediction": prediction,
        "radar_data": radar_data,
        "strengths": strengths,
        "growth_areas": growth_areas,
    }
    return render(request, "level1/level1_result.html", context)