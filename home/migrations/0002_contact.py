# Generated by Django 3.0.5 on 2020-05-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=126)),
                ('phone', models.CharField(max_length=12)),
                ('message', models.TextField()),
            ],
        ),
    ]
