# Generated by Django 5.0 on 2023-12-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("videoaulas", "0002_alter_videoaula_ano_alter_videoaula_thumb"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videoaula",
            name="arquivo_codigo",
            field=models.FileField(blank=True, null=True, upload_to="arquivos_codigo/"),
        ),
        migrations.AlterField(
            model_name="videoaula",
            name="thumb",
            field=models.ImageField(blank=True, null=True, upload_to="thumbs/"),
        ),
    ]