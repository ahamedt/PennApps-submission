# Generated by Django 3.0.6 on 2020-06-02 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0010_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='caption',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
