from django.forms import ModelForm
from .models import test, question_with_multiple_choice, question_with_free_answer, question_all


class TestForm(ModelForm):
    class Meta:
        model = test
        fields = ['title']
        user = ['user']


class QuestionAllForm(ModelForm):
    class Meta:
        model = question_all
        fields = ['TestId', 'question']


class QuestionChoiceForm(ModelForm):
    class Meta:
        model = question_with_multiple_choice
        fields = ['question', 'answer1', 'answer2', 'answer3', 'answer4', 'correct_answer']


class QuestionFreeForm(ModelForm):
    class Meta:
        model = question_with_free_answer
        fields = ['question', 'correct_answer']
