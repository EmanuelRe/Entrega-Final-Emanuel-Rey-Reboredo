

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='experienciasModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('año', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='porfolioModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ocupacion', models.CharField(max_length=30)),
                ('linkedin', models.CharField(max_length=100)),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
        
    ]
