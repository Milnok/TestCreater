# Generated by Django 3.2.9 on 2021-11-23 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0004_auto_20211123_0637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_with_free_answer',
            name='TestId',
        ),
        migrations.RemoveField(
            model_name='question_with_free_answer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question_with_free_answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question_with_multiple_choice',
            name='TestId',
        ),
        migrations.RemoveField(
            model_name='question_with_multiple_choice',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question_with_multiple_choice',
            name='question',
        ),
        migrations.CreateModel(
            name='question_all',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Вопрос')),
                ('TestId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tests.test', verbose_name='Тест')),
            ],
        ),
        migrations.AddField(
            model_name='question_with_free_answer',
            name='question_all_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tests.question_all'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question_with_multiple_choice',
            name='question_all_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tests.question_all'),
            preserve_default=False,
        ),
    ]
