# Generated by Django 4.0.4 on 2022-05-30 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='touristuser',
            old_name='dob',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='touristuser',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='touristuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='touristuser',
            name='image',
        ),
        migrations.AddField(
            model_name='touristuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='touristuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
