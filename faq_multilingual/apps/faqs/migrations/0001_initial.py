# Generated by Django 5.0.1 on 2025-01-31 12:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField(help_text="Question text in English")),
                (
                    "answer",
                    ckeditor.fields.RichTextField(
                        help_text="Answer with rich text formatting"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "question_hi",
                    models.TextField(blank=True, help_text="Hindi translation"),
                ),
                (
                    "question_bn",
                    models.TextField(blank=True, help_text="Bengali translation"),
                ),
                (
                    "answer_hi",
                    ckeditor.fields.RichTextField(blank=True, help_text="Hindi answer"),
                ),
                (
                    "answer_bn",
                    ckeditor.fields.RichTextField(
                        blank=True, help_text="Bengali answer"
                    ),
                ),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQs",
                "ordering": ["-created_at"],
            },
        ),
    ]
