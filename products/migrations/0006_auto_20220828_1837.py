# Generated by Django 3.2 on 2022-08-28 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220828_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comment',
            new_name='review',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='comment_writer',
            new_name='review_writer',
        ),
    ]