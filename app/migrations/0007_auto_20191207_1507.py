# Generated by Django 2.2.4 on 2019-12-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20191207_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
