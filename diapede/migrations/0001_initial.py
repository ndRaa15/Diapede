# Generated by Django 4.2.7 on 2023-11-05 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Pregnancies', models.IntegerField()),
                ('Glucose', models.FloatField()),
                ('BloodPressure', models.FloatField()),
                ('SkinThickness', models.FloatField()),
                ('Insulin', models.FloatField()),
                ('Height', models.FloatField()),
                ('Weight', models.FloatField()),
                ('DiabetesPedigreeFunction', models.FloatField()),
                ('Age', models.IntegerField()),
            ],
        ),
    ]
