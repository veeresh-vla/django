# Generated by Django 5.0 on 2024-07-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_contactinfo1_delete_student_delete_teacher_student1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='teacher1',
            name='contactinfo1_ptr',
        ),
        migrations.DeleteModel(
            name='Student1',
        ),
        migrations.DeleteModel(
            name='ContactInfo1',
        ),
        migrations.DeleteModel(
            name='Teacher1',
        ),
    ]
