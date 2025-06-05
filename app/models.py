from django.db import models

# Create your models here.


class MCQ(models.Model):
    question_text = models.TextField()
    choices = models.JSONField(help_text="A list of answer options, e.g., ['A', 'B', 'C', 'D']")
    correct_answer = models.CharField(max_length=255, help_text="Must match one of the choices")
    
    def __str__(self):
        return self.question_text

    def is_correct(self, selected_answer):
        return selected_answer == self.correct_answer