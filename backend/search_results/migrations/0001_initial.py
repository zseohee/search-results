from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SearchResult",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255)),
                ("category", models.CharField(blank=True, max_length=100)),
                ("state", models.CharField(blank=True, max_length=100)),
                ("summary", models.TextField(blank=True)),
                ("source_url", models.URLField()),
                ("publish_date", models.DateField()),
                ("tags", models.JSONField(default=list)),
            ],
        ),
    ]
