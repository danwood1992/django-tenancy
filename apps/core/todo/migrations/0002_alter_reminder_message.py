# Generated by Django 4.2.4 on 2023-08-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='message',
            field=models.TextField(blank=True, default='You have a task due', null=True),
        ),
    ]