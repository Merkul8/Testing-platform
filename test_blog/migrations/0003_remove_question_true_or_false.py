# Generated by Django 4.2.4 on 2023-08-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_blog', '0002_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='true_or_false',
        ),
    ]