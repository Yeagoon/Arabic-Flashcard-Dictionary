# Generated by Django 2.2.6 on 2019-11-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_searchhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentFlashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_index', models.IntegerField()),
            ],
        ),
    ]
