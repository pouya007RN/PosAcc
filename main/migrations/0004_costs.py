# Generated by Django 2.2.3 on 2020-03-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200313_1358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='مبلغ')),
                ('date', models.CharField(default='', max_length=20, verbose_name='تاریخ')),
                ('detail', models.TextField(default='')),
            ],
            options={
                'verbose_name_plural': 'هزینه ها',
            },
        ),
    ]