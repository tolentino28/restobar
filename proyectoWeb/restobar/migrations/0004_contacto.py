# Generated by Django 4.2 on 2024-08-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restobar', '0003_carta_galeria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('asunto', models.CharField(max_length=200)),
                ('mensaje', models.TextField()),
                ('contacto', models.CharField(choices=[('email', 'Correo electrónico'), ('telefono', 'Teléfono')], max_length=10)),
            ],
        ),
    ]
