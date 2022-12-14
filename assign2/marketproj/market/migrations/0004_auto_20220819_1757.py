# Generated by Django 3.2.9 on 2022-08-19 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20220814_0513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='barcode',
            field=models.IntegerField(default='98765', unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='emailid',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
