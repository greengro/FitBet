# Generated by Django 3.1.2 on 2020-11-22 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbet',
            name='payout',
            field=models.IntegerField(default=0),
        ),
    ]
