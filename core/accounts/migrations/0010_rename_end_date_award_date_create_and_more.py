# Generated by Django 5.1.4 on 2025-01-07 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_pirepsflight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='end_date',
            new_name='date_create',
        ),
        migrations.RemoveField(
            model_name='award',
            name='start_date',
        ),
        migrations.DeleteModel(
            name='PirepsFlight',
        ),
    ]
