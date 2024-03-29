# Generated by Django 3.1.3 on 2022-08-21 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('grade', models.IntegerField()),
                ('course', models.ManyToManyField(to='onlinecourse.Course')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('grade', models.IntegerField()),
                ('course', models.ManyToManyField(to='onlinecourse.Course')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('grade', models.IntegerField(default=0)),
                ('course', models.ManyToManyField(to='onlinecourse.Course')),
                ('lesson', models.ForeignKey(default='lesson', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
                ('question', models.ForeignKey(default='question', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField()),
                ('grade', models.IntegerField(default=0)),
                ('course', models.ManyToManyField(to='onlinecourse.Course')),
                ('lesson', models.ForeignKey(default='lesson', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson')),
                ('question', models.ForeignKey(default='question', on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.question')),
            ],
        ),
    ]
