from django.db import models
from django.contrib.auth.models import User


class test(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Заголовок теста')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


class question_all(models.Model):
    TestId = models.ForeignKey(test, on_delete=models.CASCADE, verbose_name='Тест', null=True)
    question = models.CharField(max_length=200, verbose_name='Вопрос')

    def __str__(self):
        return self.question


class question_with_multiple_choice(question_all):
    # Вопрос с выбором ответа из четырех
    answer1 = models.CharField(max_length=100, verbose_name='Первый ответ')
    answer2 = models.CharField(max_length=100, verbose_name='Второй ответ')
    answer3 = models.CharField(max_length=100, verbose_name='Третий ответ')
    answer4 = models.CharField(max_length=100, verbose_name='Четвертый ответ')
    NUMBERS = []
    for i in range(1, 5):
        NUMBERS.append((i, i))
    correct_answer = models.IntegerField(choices=NUMBERS, verbose_name='Правильный ответ')

    def __str__(self):
        return self.question


class question_with_free_answer(question_all):
    # Вопрос с ответом строкой
    correct_answer = models.CharField(max_length=100, verbose_name='Правильный ответ')

    def __str__(self):
        return self.question
