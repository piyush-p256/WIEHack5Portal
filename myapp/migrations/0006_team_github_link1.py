# Generated by Django 5.0.1 on 2024-04-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_team_feedback1_team_feedback_overall_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='github_link1',
            field=models.URLField(blank=True),
        ),
    ]
