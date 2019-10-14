# Generated by Django 2.1 on 2019-10-14 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crypto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rate_change', models.DecimalField(decimal_places=3, max_digits=6)),
                ('quantity', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=10, max_digits=19)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='api.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='crypto',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Crypto', to='api.Wallet'),
        ),
    ]
