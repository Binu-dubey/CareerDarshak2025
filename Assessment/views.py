from django.shortcuts import render, redirect

# Create your views here.
from .models import Question, UserProfile
import os
import joblib
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User



@login_required
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect logged-in users to homepage
    return render(request, 'login.html')
@login_required
def assessment(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'assessment/assessment.html')
    

def psychometric_test(request):
    
    # Get psychometric questions
    questions = Question.objects.filter(category='psychometric')

    if request.method == 'POST':
        form = QuestionForm(questions, request.POST)
        if form.is_valid():
            total_scores = {'o_score': 0, 'c_score': 0, 'e_score': 0, 'a_score': 0, 'n_score': 0}
            count = {'o_score': 0, 'c_score': 0, 'e_score': 0, 'a_score': 0, 'n_score': 0}

            # Calculate the average scores for each subcategory
            for question in questions:
                selected_option = form.cleaned_data[f'question_{question.id}']
                total_scores[question.subcategory] += int(selected_option)
                count[question.subcategory] += 1

            # Store scores in UserProfile
            profile = request.user.userprofile
            for subcategory in total_scores.keys():
                if count[subcategory] > 0:
                    setattr(profile, subcategory, total_scores[subcategory] / count[subcategory])

            profile.save()

            # Redirect to aptitude test after psychometric test submission
            return redirect('aptitude_test')
    else:
        form = QuestionForm(questions)

    return render(request, 'assessment/psychometric_test.html', {'form': form})

@login_required
def aptitude_test(request):
    # Fetch aptitude questions
    questions = Question.objects.filter(category='aptitude')

    if request.method == 'POST':
        form = QuestionForm(questions, request.POST)
        if form.is_valid():
            numerical_total = 0
            numerical_count = 0

            # Calculate average numerical ability score
            for question in questions:
                selected_option = form.cleaned_data[f'question_{question.id}']
                numerical_total += int(selected_option)
                numerical_count += 1

            # Store numerical ability score in UserProfile
            profile = request.user.userprofile
            profile.numerical_ability = numerical_total / numerical_count
            profile.save()

            # Redirect to reasoning test after aptitude test submission
            return redirect('reasoning_test')
    else:
        form = QuestionForm(questions)

    return render(request, 'assessment/aptitude_test.html', {'form': form})

@login_required
def reasoning_test(request):
    # Fetch reasoning questions
    questions = Question.objects.filter(category='reasoning')

    if request.method == 'POST':
        form = QuestionForm(questions, request.POST)
        if form.is_valid():
            verbal_total = 0
            verbal_count = 0
            logical_total = 0
            logical_count = 0

            # Calculate average verbal and logical reasoning scores
            for question in questions:
                selected_option = form.cleaned_data[f'question_{question.id}']
                if question.subcategory == 'verbal':
                    verbal_total += int(selected_option)
                    verbal_count += 1
                elif question.subcategory == 'logical':
                    logical_total += int(selected_option)
                    logical_count += 1

            # Store reasoning scores in UserProfile
            profile = request.user.userprofile
            if verbal_count > 0:
                profile.verbal_reasoning = verbal_total / verbal_count
            if logical_count > 0:
                profile.logical_reasoning = logical_total / logical_count
            profile.save()

            # Redirect to some other page after reasoning test submission
            return redirect('assessment_complete')
    else:
        form = QuestionForm(questions)

    return render(request, 'assessment/reasoning_test.html', {'form': form})

@login_required
def assessment_complete(request):
    profile = request.user.userprofile
    input_scores = [
        profile.o_score,
        profile.c_score,
        profile.e_score,
        profile.a_score,
        profile.n_score,
        profile.numerical_ability,
        profile.verbal_reasoning,
    ]
    career_0 = [
       'Chef', 'Artist', 'Fashion Designer', 'Event Photographer',
       'Musician', 'Interior Designer', 'Video Game Tester',
       'Fashion Stylist', 'Film Director'
    ]
    career_1 = [
       'Accountant', 'Graphic Designer', 'Research Scientist',
       'Architect', 'Software Developer', 'Construction Engineer',
       'Astronomer', 'Financial Analyst', 'Biologist',
       'Environmental Scientist', 'IT Support Specialist',
       'Biomedical Engineer', 'Data Analyst', 'Pharmacist',
       'Financial Planner', 'Biotechnologist',
       'Software Quality Assurance Tester', 'Industrial Engineer',
       'Financial Auditor', 'Zoologist', 'Mechanical Engineer',
       'Forensic Scientist', 'Geologist', 'Web Developer',
       'Wildlife Biologist', 'Air Traffic Controller', 'Game Developer',
       'Urban Planner', 'Financial Advisor', 'Airline Pilot',
       'Environmental Engineer', 'Mechanical Designer',
       'Marketing Analyst', 'Aerospace Engineer',
       'Wildlife Conservationist', 'Biomedical Researcher',
       'Database Administrator', 'Electrical Engineer',
       'Investment Banker', 'Marine Biologist', 'Database Analyst',
       'Forensic Psychologist', 'Public Health Analyst',
       'Insurance Underwriter', 'Tax Accountant',
       'Quality Control Inspector', 'Tax Collector', 'Civil Engineer',
       'Robotics Engineer', 'Electronics Design Engineer'
    ]
    career_2 = [
       'Salesperson', 'Teacher', 'Nurse', 'Psychologist',
       'Marketing Manager', 'Physician', 'Human Resources Manager',
       'Journalist', 'Event Planner', 'Real Estate Agent', 'Lawyer',
       'Marketing Coordinator', 'Social Worker', 'HR Recruiter',
       'Elementary School Teacher', 'Market Research Analyst',
       'Police Detective', 'Marketing Copywriter', 'Speech Therapist',
       'Social Media Manager', 'Physical Therapist', 'Dental Hygienist',
       'Pediatric Nurse', 'Advertising Executive', 'IT Project Manager',
       'Forestry Technician', 'Marriage Counselor',
       'Public Relations Specialist', 'Genetic Counselor',
       'Market Researcher', 'Occupational Therapist',
       'Human Rights Lawyer', 'Pediatrician', 'Technical Writer',
       'Product Manager', 'Speech Pathologist', 'Sports Coach',
       'Chiropractor', 'Radiologic Technologist',
       'Rehabilitation Counselor', 'Diplomat', 'Police Officer',
       'Administrative Officer', 'Foreign Service Officer',
       'Customs and Border Protection Officer'  
    ] 
    model_path = os.path.join(settings.BASE_DIR, 'Prediction-model.pkl')
    
    model = joblib.load(model_path)
    print(type(model))

    predicted_cluster = model.predict([input_scores]) 
    if predicted_cluster == 0:
        recommended_careers = career_0
    elif predicted_cluster == 1:
        recommended_careers = career_1
    elif predicted_cluster == 2:
        recommended_careers = career_2
    else:
        recommended_careers = ["Unknown cluster"]
    explanation = (
        f"Based on your scores, you exhibit a strong inclination towards recommended career. "
        f"Your strengths in numerical reasoning and logical thinking indicate suitability for this field."
    )

    return render(request, 'assessment/complete.html' , {
        'profile': profile, 
        'recommended_careers': recommended_careers,
        'explanation': explanation 
    })

@method_decorator(login_required, name='dispatch')	
class UserProfileView(DetailView):
    model = UserProfile
    template_name = "assessment/profile.html"
    context_object_name = "profile"

    def get_object(self):
        # Fetch the UserProfile object for the currently logged-in user
        user = get_object_or_404(User, username=self.kwargs['username'])
        return get_object_or_404(UserProfile, user=user)
   

           
