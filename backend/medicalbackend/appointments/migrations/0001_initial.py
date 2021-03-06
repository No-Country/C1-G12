# Generated by Django 3.1.4 on 2021-12-08 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20211208_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=20)),
                ('Time', models.CharField(max_length=15)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('Pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.pacient')),
            ],
        ),
    ]
