# Generated by Django 5.1 on 2024-10-07 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='create_on',
            new_name='created_on',
        ),
    ]
