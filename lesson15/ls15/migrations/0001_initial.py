# Generated by Django 4.2.3 on 2023-07-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=50)),
                ('date_of_creation', models.DateTimeField()),
                ('date_deadline', models.DateField()),
                ('level', models.CharField(choices=[('sm', 'small'), ('av', 'average'), ('hh', 'high')], max_length=20)),
                ('status', models.CharField(choices=[('dn', 'done'), ('nd', 'not done')], max_length=20)),
            ],
        ),
    ]
