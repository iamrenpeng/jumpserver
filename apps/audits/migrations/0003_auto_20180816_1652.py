# Generated by Django 2.0.7 on 2018-08-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audits', '0002_ftplog_org_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ftplog',
            name='org_id',
            field=models.CharField(blank=True, default='', max_length=36, verbose_name='Organization'),
        ),
    ]