# Generated by Django 4.0.5 on 2022-10-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TokenList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tokens', models.CharField(max_length=100)),
                ('CustomerName', models.CharField(max_length=100)),
                ('CallStatus', models.BooleanField(default=False)),
                ('Token_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
