# Generated by Django 2.2.6 on 2022-12-15 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_history_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='arch_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]