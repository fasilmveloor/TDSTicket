# Generated by Django 4.0.4 on 2022-06-09 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TDSManager', '0004_alter_tdsuser_tdid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('tds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TDSManager.tdsuser')),
            ],
        ),
    ]
