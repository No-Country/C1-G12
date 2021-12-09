# Generated by Django 3.1.4 on 2021-12-08 19:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.extenduser')),
                ('speciality', models.CharField(max_length=20)),
                ('turn', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.extenduser')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('dni', models.CharField(max_length=15)),
                ('age', models.DateField()),
                ('gender', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=15)),
                ('social', models.CharField(max_length=30)),
                ('plan', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SysAdmin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.extenduser')),
            ],
        ),
        migrations.AddField(
            model_name='extenduser',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='doctor status'),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='is_pacient',
            field=models.BooleanField(default=False, verbose_name='pacient status'),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='is_sysadmin',
            field=models.BooleanField(default=False, verbose_name='sysadmin status'),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extenduser',
            name='surname',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]