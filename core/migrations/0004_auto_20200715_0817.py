# Generated by Django 3.0.7 on 2020-07-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200714_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sports Wear'), ('OW', 'Outwear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
