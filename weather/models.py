from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, default="Unknown")  # Set default value
    country = models.CharField(max_length=100, default="Unknown")
    local_time = models.CharField(max_length=100, default="Unknown")  # Set default value
    temperature_c = models.FloatField(default=0.0)  # Set default value
    feelslike_c = models.FloatField(default=0.0)  # Set default value
    condition_text = models.CharField(max_length=100, default="Unknown")  # Set default value
    condition_icon = models.URLField(default="")  # Set default value

    wind_kph = models.FloatField(default=0.0)  # Set default value
    wind_dir = models.CharField(max_length=10, default="Unknown")  # Set default value
    pressure_mb = models.FloatField(default=0.0)  # Set default value
    precip_mm = models.FloatField(default=0.0)  # Set default value
    humidity = models.IntegerField(default=0)  # Set default value
    cloud = models.IntegerField(default=0)  # Set default value

    uv = models.FloatField(default=0.0)  # Set default value
    vis_km = models.FloatField(default=0.0)  # Set default value
    gust_kph = models.FloatField(default=0.0)  # Set default value
    last_updated = models.DateTimeField(default=None, null=True)  # Set default value for DateTimeField

    def __str__(self):
        return f"{self.city} Weather at {self.last_updated}"
