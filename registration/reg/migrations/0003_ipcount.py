# Generated by Django 2.2.12 on 2020-04-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_auto_20200407_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('count', models.IntegerField(default=1)),
            ],
        ),
    ]