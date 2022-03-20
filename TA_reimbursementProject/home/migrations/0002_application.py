# Generated by Django 4.0.3 on 2022-03-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_yr', models.IntegerField(default=0)),
                ('joining', models.IntegerField(default=0)),
                ('basic_pay', models.IntegerField(default=0)),
                ('Name', models.CharField(default='NA', max_length=122)),
                ('Designation', models.CharField(default='NA', max_length=122)),
                ('section', models.CharField(default='NA', max_length=122)),
                ('avail', models.CharField(default='NA', max_length=122)),
                ('duration', models.IntegerField(default=0)),
                ('departure', models.IntegerField(default=0)),
                ('nature', models.CharField(default='NA', max_length=122)),
                ('Purpose', models.CharField(default='NA', max_length=122)),
                ('place', models.CharField(default='NA', max_length=122)),
                ('place1', models.CharField(default='NA', max_length=122)),
                ('address', models.CharField(default='NA', max_length=122)),
                ('mode', models.CharField(default='NA', max_length=122)),
                ('Name1', models.CharField(default='NA', max_length=122)),
                ('Age1', models.IntegerField(default=0)),
                ('Name2', models.CharField(default='NA', max_length=122)),
                ('Age2', models.IntegerField(default=0)),
                ('Name3', models.CharField(default='NA', max_length=122)),
                ('Age3', models.IntegerField(default=0)),
                ('advance', models.IntegerField(default=0)),
            ],
        ),
    ]
