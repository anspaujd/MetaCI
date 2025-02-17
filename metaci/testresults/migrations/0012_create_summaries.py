# Generated by Django 2.1.7 on 2019-04-26 17:55

from django.db import migrations, models

from metaci.testresults.models import TestResultPerfWeeklySummary


def generate_summaries(apps, schema_editor):
    TestResultPerfWeeklySummary.summarize_weeks()


class Migration(migrations.Migration):
    atomic = False

    dependencies = [("testresults", "0011_auto_20190426_1755")]

    operations = [
        migrations.RunPython(generate_summaries, reverse_code=migrations.RunPython.noop)
    ]
