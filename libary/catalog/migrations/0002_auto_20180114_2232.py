# Generated by Django 2.0.1 on 2018-01-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(default='Published nn.nn.nnnn.Good choose ', max_length=200),
        ),
    ]