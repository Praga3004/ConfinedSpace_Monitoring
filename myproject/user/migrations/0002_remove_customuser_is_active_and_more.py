# Generated by Django 5.0.3 on 2024-03-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(default='1900-01-01'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='customuser',
            name='street_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]