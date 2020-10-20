# Generated by Django 3.1.2 on 2020-10-20 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_flows", "0014_auto_20200925_2332"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowstagebinding",
            name="re_evaluate_policies",
            field=models.BooleanField(
                default=False,
                help_text="Evaluate policies when the Stage is present to the user.",
            ),
        ),
        migrations.AddField(
            model_name="flowstagebinding",
            name="evaluate_on_plan",
            field=models.BooleanField(
                default=True,
                help_text="Evaluate policies during the Flow planning process. Disable this for input-based policies.",
            ),
        ),
    ]
