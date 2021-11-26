from django.shortcuts import render, redirect, get_object_or_404
from .models import test, question_with_multiple_choice, question_with_free_answer, question_all
from .forms import TestForm, QuestionFreeForm, QuestionChoiceForm
from django.contrib.auth.decorators import login_required


@login_required
def tests_list(request):
    tests = test.objects.order_by('id')[:5]
    return render(request, 'tests/tests_list.html', {'tests': tests, 'current_page': 2})


@login_required
def loadmore(request, pages):
    tests = test.objects.order_by('id')[:(pages) * 5]
    if len(test.objects.all()) // 5 + 1 >= pages:
        pages = int(pages) + 1
    return render(request, 'tests/tests_list.html', {'tests': tests, 'current_page': pages})


@login_required
def create_test(request):
    if request.method == 'GET':
        return render(request, 'tests/create_test.html', {'test': TestForm})
    else:
        try:
            form = TestForm(request.POST)
            newtest = form.save(commit=False)
            newtest.user = request.user
            newtest.save()
            return redirect('/tests/my_tests')
        except ValueError:
            return render(request, 'tests/create_test.html', {'test': TestForm, 'error': 'Это название уже занято'})


@login_required
def my_tests_list(request):
    tests = test.objects.filter(user=request.user)
    return render(request, 'tests/my_tests.html', {'tests': tests})


@login_required
def viewtest(request, test_pk):
    one_test = get_object_or_404(test, pk=test_pk, user=request.user)
    all_questions = set(list(question_with_multiple_choice.objects.filter(TestId=one_test)) + list(
        question_with_free_answer.objects.filter(TestId=one_test)))
    if request.method == 'GET':
        form = TestForm(instance=one_test)
        question_form = QuestionChoiceForm
        return render(request, 'tests/viewtest.html',
                      {'test': one_test, 'form': form, 'question_form': question_form, 'all_questions': all_questions})
    else:
        try:
            if request.POST['submit'] == 'QChoice':
                question_form = QuestionChoiceForm
            elif request.POST['submit'] == 'QOpen':
                question_form = QuestionFreeForm
            form = TestForm(request.POST, instance=one_test)
            form.save()
            return redirect('/tests/my_tests')
        except ValueError:
            return render(request, 'tests/viewtest.html',
                          {'test': one_test, 'form': form, 'question_form': question_form,
                           'all_questions': all_questions})


@login_required
def createquestion(request, test_pk):
    one_test = get_object_or_404(test, pk=test_pk, user=request.user)
    if request.method == 'POST':
        form = TestForm(instance=one_test)
        question_form = QuestionChoiceForm
        if request.POST.get('answer1') is None:
            question_with_free_answer.objects.create(TestId=one_test, question=request.POST['question'],
                                                     correct_answer=request.POST['correct_answer'])
        else:
            question_with_multiple_choice.objects.create(TestId=one_test, question=request.POST['question'],
                                                         answer1=request.POST['answer1'],
                                                         answer2=request.POST['answer2'],
                                                         answer3=request.POST['answer3'],
                                                         answer4=request.POST['answer4'],
                                                         correct_answer=request.POST['correct_answer'])
        all_questions = set(list(question_with_multiple_choice.objects.filter(TestId=one_test)) + list(
            question_with_free_answer.objects.filter(TestId=one_test)))
        return render(request, 'tests/viewtest.html',
                      {'test': one_test, 'form': form, 'question_form': question_form, 'all_questions': all_questions})


@login_required
def deletequestion(request, test_pk, question_pk):
    if request.method == 'POST':
        one_test = get_object_or_404(test, pk=test_pk, user=request.user)
        one_question = get_object_or_404(question_all, pk=question_pk)
        one_question.delete()
        form = TestForm(instance=one_test)
        question_form = QuestionChoiceForm
        all_questions = set(list(question_with_multiple_choice.objects.filter(TestId=one_test)) + list(
            question_with_free_answer.objects.filter(TestId=one_test)))
        return render(request, 'tests/viewtest.html',
                      {'test': one_test, 'form': form, 'question_form': question_form, 'all_questions': all_questions})


@login_required
def deletetest(request, test_pk):
    one_test = get_object_or_404(test, pk=test_pk, user=request.user)
    if request.method == 'POST':
        one_test.delete()
        tests = test.objects.filter(user=request.user)
        return render(request, 'tests/my_tests.html', {'tests': tests})


@login_required
def starttest(request, test_pk):
    one_test = get_object_or_404(test, pk=test_pk)
    all_questions = set(list(question_with_multiple_choice.objects.filter(TestId=one_test)) + list(
        question_with_free_answer.objects.filter(TestId=one_test)))
    return render(request, 'tests/starttest.html',
                  {'test': one_test, 'questions': all_questions})


@login_required
def sendanswers(request, test_pk):
    one_test = get_object_or_404(test, pk=test_pk)
    all_questions = set(list(question_with_multiple_choice.objects.filter(TestId=one_test)) + list(
        question_with_free_answer.objects.filter(TestId=one_test)))
    num_correct_answers = 0
    for question in all_questions:
        correct_answer = question.correct_answer
        answer = request.POST[str(question.id)]
        if str(correct_answer).lower() == str(answer).lower():
            num_correct_answers += 1
    persent_correct = num_correct_answers * 100 // len(all_questions)
    Return = {'test': one_test, 'questions': all_questions, 'persent_correct': str(persent_correct)}
    if persent_correct == 0:
        Return['awful'] = 'awful'
    elif persent_correct < 33:
        Return['bad'] = 'bad'
    elif persent_correct < 66:
        Return['ok'] = 'ok'
    elif persent_correct < 100:
        Return['good'] = 'good'
    if persent_correct == 100:
        Return['great'] = 'great'
    return render(request, 'tests/result.html', Return)
