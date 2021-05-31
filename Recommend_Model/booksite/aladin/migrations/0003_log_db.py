# Generated by Django 3.2.3 on 2021-05-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aladin', '0002_auto_20210526_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='LOG_DB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('book_id', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
