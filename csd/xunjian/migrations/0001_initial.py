# Generated by Django 3.2.5 on 2021-12-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xunjian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xunjian_items', models.CharField(max_length=32)),
                ('web', models.CharField(blank=True, max_length=128, null=True)),
                ('suggestTime', models.DateTimeField()),
                ('daily', models.BooleanField()),
                ('weekly', models.BooleanField()),
                ('monthly', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Xunjian_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('OK', 'OK'), ('Resolve', 'Resolve'), ('Fault', 'Fault'), ('Warning', 'Warning')], max_length=10)),
                ('check_time', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='xunjian.xunjian')),
                ('onduty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.onduty')),
            ],
        ),
    ]