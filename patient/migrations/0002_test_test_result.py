# Generated by Django 3.0.5 on 2020-06-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_result',
            field=models.CharField(default='Negative', max_length=100),
        ),
    ]