# Generated by Django 3.2.4 on 2021-08-17 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_details_home_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('abbrev', models.TextField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50)),
                ('index', models.FloatField()),
                ('grocery', models.FloatField()),
                ('housing', models.FloatField()),
                ('utilities', models.FloatField()),
                ('transportation', models.FloatField()),
                ('healthcare', models.FloatField()),
                ('misc', models.FloatField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='city', to='budget.state')),
            ],
        ),
    ]