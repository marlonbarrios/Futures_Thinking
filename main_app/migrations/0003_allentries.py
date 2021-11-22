# Generated by Django 3.2.9 on 2021-11-22 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_userentries_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_entries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.userentries')),
            ],
        ),
    ]
