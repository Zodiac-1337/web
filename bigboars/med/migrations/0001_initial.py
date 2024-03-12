# Generated by Django 5.0.3 on 2024-03-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('passport_details', models.TextField()),
                ('place_of_work', models.TextField()),
                ('insurance_policy', models.TextField()),
                ('insurance_company', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
