# Generated by Django 2.1.4 on 2019-05-21 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('contact_no', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AgentRegister',
            fields=[
                ('agent_no', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('otp', models.IntegerField()),
                ('photo', models.ImageField(upload_to='agent')),
                ('address', models.TextField()),
                ('contact_no', models.IntegerField()),
            ],
        ),
    ]
