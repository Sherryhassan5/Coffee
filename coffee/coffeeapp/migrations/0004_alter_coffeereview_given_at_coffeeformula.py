# Generated by Django 4.2.13 on 2024-06-01 23:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeapp', '0003_alter_coffee_type_coffeereview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeereview',
            name='given_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='CoffeeFormula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=200)),
                ('coffee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='coffeeapp.coffee')),
            ],
        ),
    ]
