# Generated by Django 3.0.4 on 2020-03-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizzaType', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subType', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizzaSize',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='dinnerplatter',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.DinnerPlatterType'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='pizzaType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.PizzaType'),
        ),
        migrations.AlterField(
            model_name='sub',
            name='subType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='orders.SubType'),
        ),
    ]
