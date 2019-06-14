# Generated by Django 2.0.13 on 2019-05-02 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoticiasModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('resumen', models.CharField(max_length=200)),
                ('detalle', models.CharField(max_length=500)),
                ('tipoChoice', models.CharField(choices=[('N', 'Noticias'), ('E', 'Eventos')], default='N', max_length=2)),
            ],
        ),
    ]