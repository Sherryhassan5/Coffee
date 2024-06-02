# Generated by Django 4.2.13 on 2024-06-01 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeapp', '0004_alter_coffeereview_given_at_coffeeformula'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('coffee', models.ManyToManyField(to='coffeeapp.coffee')),
            ],
        ),
    ]
