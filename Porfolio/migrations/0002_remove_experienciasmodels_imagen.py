

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Porfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experienciasmodels',
            name='imagen',
        ),
    ]
