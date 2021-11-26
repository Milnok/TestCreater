from django.urls import include, path
from . import views

app_name = 'tests'

urlpatterns = [
    path('', views.tests_list, name=''),
    path('page/<int:pages>', views.loadmore, name='loadmore'),
    path('create_test', views.create_test, name='create_test'),
    path('<int:test_pk>', views.starttest, name='starttest'),
    path('<int:test_pk>/sendanswers', views.sendanswers, name='sendanswers'),

    path('my_tests', views.my_tests_list, name='my_tests'),
    path('my_tests/<int:test_pk>', views.viewtest, name='viewtest'),
    path('my_tests/<int:test_pk>/createquestion', views.createquestion, name='createquestion'),
    path('my_tests/<int:test_pk>/deletequestion/<int:question_pk>', views.deletequestion, name='deletequestion'),
    path('my_tests/<int:test_pk>/deletetest', views.deletetest, name='deletetest'),
]