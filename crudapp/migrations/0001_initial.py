# Generated by Django 4.0.3 on 2023-04-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('userName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('Checkbox', models.BooleanField(default=False)),
            ],
        ),
    ]
