from django import forms
from .models import MCQ

class MCQForm(forms.ModelForm):
    choices = forms.CharField(
        help_text="Enter choices separated by commas, e.g. A,B,C,D"
    )

    class Meta:
        model = MCQ
        fields = ['question_text', 'choices', 'correct_answer']

    def clean_choices(self):
        raw_choices = self.cleaned_data['choices']
        return [choice.strip() for choice in raw_choices.split(',')]