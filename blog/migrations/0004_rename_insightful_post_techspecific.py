# Generated by Django 5.0 on 2024-11-27 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_date_updated_post_insightful'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='insightful',
            new_name='techspecific',
        ),
    ]