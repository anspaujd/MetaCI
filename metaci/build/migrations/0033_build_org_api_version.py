# Generated by Django 2.2.6 on 2019-10-31 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("build", "0032_auto_20191025_1453")]

    operations = [
        migrations.AddField(
            model_name="build",
            name="org_api_version",
            field=models.CharField(blank=True, max_length=5, null=True),
        )
    ]
