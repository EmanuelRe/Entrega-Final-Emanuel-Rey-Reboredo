

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Porfolio', '0004_experienciasmodels_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experienciasmodels',
            name='descripcion',
            field=models.CharField(max_length=1000),
        ),
    ]
