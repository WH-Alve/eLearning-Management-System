# Generated by Django 3.2.11 on 2022-05-22 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_course_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
