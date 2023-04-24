# Generated by Django 4.2 on 2023-04-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=50)),
                ('facility', models.IntegerField()),
                ('management', models.TextField(max_length=300)),
                ('q1', models.CharField(choices=[('q1', 'Yes'), ('q1', 'No')], max_length=10)),
                ('q2', models.CharField(choices=[('q2', 'Yes'), ('q2', 'No')], max_length=10)),
                ('q3', models.CharField(choices=[('q3', 'Yes'), ('q3', 'No')], max_length=10)),
                ('q4', models.CharField(choices=[('q4', 'Yes'), ('q4', 'No')], max_length=10)),
                ('challenges', models.TextField(max_length=500)),
                ('q5', models.CharField(choices=[('q5', 'Yes'), ('q5', 'No')], max_length=10)),
                ('features', models.TextField(max_length=500)),
                ('q6', models.CharField(choices=[('q6', 'Yes'), ('q6', 'No')], max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]