# Generated by Django 2.2.6 on 2019-10-23 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arabic_word', models.CharField(max_length=40)),
                ('definition1', models.TextField()),
                ('definition2', models.TextField(blank=True, null=True)),
                ('definition3', models.TextField(blank=True, null=True)),
                ('definition4', models.TextField(blank=True, null=True)),
                ('definition5', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
