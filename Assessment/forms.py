from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordChangeForm,SetPasswordForm,PasswordResetForm 
from django.contrib.auth.forms import User
from .models import Question,UserProfile

class QuestionForm(forms.Form):
    # Dynamically create fields based on the questions for a category/subcategory
    def __init__(self, questions, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        for question in questions:
            choices = [
                (question.option_1_score, question.option_1),
                (question.option_2_score, question.option_2),
                (question.option_3_score, question.option_3),
                (question.option_4_score, question.option_4),
            ]
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices, widget=forms.RadioSelect, label=question.question_text
            )
