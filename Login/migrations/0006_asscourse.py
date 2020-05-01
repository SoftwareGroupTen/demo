# Generated by Django 2.2.12 on 2020-04-30 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0005_stucourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='asscourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assistantName', models.CharField(max_length=10)),
                ('thecourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Login.course')),
            ],
        ),
    ]
