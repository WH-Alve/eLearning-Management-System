# Generated by Django 3.2.11 on 2022-05-22 02:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
                ('short_code', models.CharField(max_length=100)),
                ('qualifications', models.CharField(max_length=100)),
                ('designations', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=100)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classroom.department')),
            ],
        ),
    ]
