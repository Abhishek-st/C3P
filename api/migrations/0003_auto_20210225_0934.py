# Generated by Django 3.0.5 on 2021-02-25 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210225_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Size'),
        ),
    ]