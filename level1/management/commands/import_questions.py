import json
from django.core.management.base import BaseCommand
from level1.models import Question, Option  # Replace with your actual app name

class Command(BaseCommand):
    help = 'Import Level 1 questions and options from JSON file'

    def handle(self, *args, **kwargs):
        with open('level1_questions.json') as f:
            data = json.load(f)

        for item in data:
            question, created = Question.objects.get_or_create(
                level=item["level"],
                question_number=item["question_number"],
                question_text=item["question_text"],
                trait=item["trait"]
            )

            # Clear existing options if re-importing
            question.options.all().delete()

            for option in item["options"]:
                Option.objects.create(
                    question=question,
                    text=option["text"],
                    score=option["score"]
                )

        self.stdout.write(self.style.SUCCESS("Successfully imported all Level 1 questions."))
