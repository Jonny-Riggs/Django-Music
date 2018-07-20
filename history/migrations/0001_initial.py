# Generated by Django 2.0.7 on 2018-07-20 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('birth_date', models.TextField(default='')),
                ('biggest_hit', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('album', models.TextField(default='')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Artist')),
            ],
        ),
    ]
