# Generated by Django 4.2 on 2024-08-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0005_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeria',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
