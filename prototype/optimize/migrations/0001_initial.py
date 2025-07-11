# Generated by Django 4.2.17 on 2025-05-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChipDesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performance', models.CharField(choices=[('Low', 'Low'), ('Balanced', 'Balanced'), ('High', 'High')], max_length=10)),
                ('max_power', models.IntegerField()),
                ('max_area', models.IntegerField()),
                ('selected_core', models.CharField(max_length=50)),
                ('selected_memory', models.CharField(max_length=50)),
                ('selected_connectivity', models.CharField(max_length=50)),
                ('total_power', models.IntegerField()),
                ('total_area', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
