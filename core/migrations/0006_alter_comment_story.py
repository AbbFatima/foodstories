# Generated by Django 5.1.6 on 2025-05-31 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_comment_story_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='story',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='core.story'),
        ),
    ]
