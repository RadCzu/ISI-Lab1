# Generated by Django 3.2.25 on 2024-06-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_post_id_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=100),
        ),
    ]