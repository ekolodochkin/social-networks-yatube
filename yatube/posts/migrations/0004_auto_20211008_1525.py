# Generated by Django 2.2.9 on 2021-10-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20211006_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['group']},
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]