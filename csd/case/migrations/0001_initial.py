# Generated by Django 3.2.5 on 2021-12-22 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fault',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Onduty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TicketNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tktnumber', models.CharField(max_length=124)),
                ('product_ID', models.CharField(max_length=12)),
                ('priority', models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4')], max_length=5)),
                ('TTR', models.IntegerField()),
                ('First_response_time', models.IntegerField()),
                ('closedate', models.DateTimeField(auto_now_add=True)),
                ('fix_by_csd', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.customer')),
                ('fault', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.fault')),
                ('onduty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.onduty')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.provider')),
                ('rfo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.rfo')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.service')),
            ],
        ),
        migrations.AddField(
            model_name='rfo',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='case.service'),
        ),
    ]
