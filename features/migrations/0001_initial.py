# Generated by Django 4.1.4 on 2024-05-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_icon', models.CharField(max_length=50)),
                ('feature_title', models.CharField(max_length=50)),
                ('feature_desc', models.TextField()),
            ],
        ),
    ]
