# Generated by Django 3.1.5 on 2021-03-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.IntegerField()),
                ('email_id', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('cpassword', models.CharField(max_length=10)),
            ],
        ),
    ]
