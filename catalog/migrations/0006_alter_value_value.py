# Generated by Django 4.0.1 on 2022-01-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_value_alter_exam_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='value',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
