# Generated by Django 3.2.16 on 2022-12-26 17:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
