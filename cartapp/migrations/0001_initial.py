# Generated by Django 2.2 on 2020-01-18 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodID', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('email', models.CharField(max_length=15)),
            ],
        ),
    ]
