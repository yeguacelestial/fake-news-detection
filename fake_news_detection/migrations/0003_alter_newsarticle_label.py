# Generated by Django 3.2 on 2021-04-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_news_detection', '0002_newsarticle_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='label',
            field=models.CharField(default='Fake', max_length=10),
        ),
    ]
