from django.contrib import admin
from .models import Question, Option, UserResponse, TraitScore, MLPredictionResult

admin.site.register(Question)
admin.site.register(Option)
admin.site.register(UserResponse)
admin.site.register(TraitScore)
admin.site.register(MLPredictionResult)

