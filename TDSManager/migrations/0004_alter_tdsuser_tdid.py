# Generated by Django 4.0.4 on 2022-06-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TDSManager', '0003_tdsuser_tdid_alter_tdsuser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdsuser',
            name='tdid',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False),
        ),
    ]