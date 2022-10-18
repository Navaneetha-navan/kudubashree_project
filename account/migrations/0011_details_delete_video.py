# Generated by Django 4.0.2 on 2022-03-04 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('discription', models.TextField()),
                ('videofile', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='video',
        ),
    ]
