# Generated by Django 2.2 on 2019-05-02 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('britecoreapi', '0004_auto_20190502_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datacontent',
            name='row_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row_contents', to='britecoreapi.DataRow'),
        ),
    ]