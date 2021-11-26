from django.contrib import admin
from .models import test, question_with_multiple_choice, question_with_free_answer, question_all

admin.site.register(test)
admin.site.register(question_all)
admin.site.register(question_with_multiple_choice)
admin.site.register(question_with_free_answer)
