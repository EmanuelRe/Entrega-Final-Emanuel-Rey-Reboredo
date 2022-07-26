

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Porfolio', '0003_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='experienciasmodels',
            name='imagen',
            field=models.ImageField(default=1, upload_to='media/images/'),
            preserve_default=False,
        ),
    ]
