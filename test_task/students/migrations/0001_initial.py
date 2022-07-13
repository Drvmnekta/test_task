# Generated by Django 4.0.6 on 2022-07-13 11:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Возраст')),
                ('department', models.CharField(choices=[('bio', 'Биология'), ('math', 'Математика'), ('eco', 'Экономика')], default='eco', max_length=100, verbose_name='Кафедра')),
            ],
        ),
    ]