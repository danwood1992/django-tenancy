# Generated by Django 4.2.4 on 2023-08-15 07:25

import apps.admin.tenancy.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenancy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffSeat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tenancy_owner', models.BooleanField(default=False)),
                ('mobile_no', models.CharField(blank=True, max_length=20, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('can_pay_tenancy', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('tenant_management_level', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=apps.admin.tenancy.utils.seat_personal_upload_path)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenancy.tenant')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'indexes': [models.Index(fields=['tenant'], name='seats_staff_tenant__579670_idx')],
            },
        ),
    ]