# Generated by Django 4.1.1 on 2022-09-16 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=20)),
                ('about', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ow_app.category')),
            ],
        ),
    ]
