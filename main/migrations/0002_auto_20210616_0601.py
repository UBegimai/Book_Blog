# Generated by Django 3.1 on 2021-06-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='pub_date',
            new_name='published',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(),
        ),
    ]
