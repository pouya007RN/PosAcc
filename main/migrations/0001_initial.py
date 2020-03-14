# Generated by Django 2.2.3 on 2020-03-12 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('serial_no', models.CharField(default='', max_length=50)),
                ('app', models.CharField(blank=True, max_length=50)),
                ('terminal', models.CharField(default='', max_length=50)),
                ('details', models.TextField(default='')),
                ('price', models.CharField(default=0, max_length=50)),
                ('count', models.IntegerField(default=1, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='09', max_length=15)),
                ('melli_id', models.CharField(default='', max_length=20)),
                ('shop', models.CharField(default='', max_length=50)),
                ('phone_stat', models.CharField(default='', max_length=20)),
                ('paid', models.CharField(default=0, max_length=10)),
                ('date', models.CharField(default='', max_length=20)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Device')),
            ],
        ),
    ]