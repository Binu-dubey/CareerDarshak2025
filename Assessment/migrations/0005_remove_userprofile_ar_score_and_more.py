# Generated by Django 5.1.4 on 2025-01-27 15:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Assessment", "0004_rename_c_score_userprofile_cr_score_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="AR_score",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="CR_score",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="ER_score",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="IR_score",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="RR_score",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="SR_score",
        ),
    ]
