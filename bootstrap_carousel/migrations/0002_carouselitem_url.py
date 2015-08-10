from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_carousel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselitem',
            name='url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
