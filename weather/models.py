from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100, default="Unknown")
    region = models.CharField(max_length=100, default="Unknown")
    country = models.CharField(max_length=100, default="Unknown")
    local_time = models.CharField(max_length=100, default="Unknown")

    temperature_c = models.FloatField(default=0.0)
    temp_f = models.FloatField(default=0.0)
    is_day = models.BooleanField(default=True)

    condition_text = models.CharField(max_length=100, default="Unknown")
    condition_icon = models.URLField(default="")
    condition_code = models.IntegerField(default=0)

    wind_mph = models.FloatField(default=0.0)
    wind_kph = models.FloatField(default=0.0)
    wind_degree = models.IntegerField(default=0)
    wind_dir = models.CharField(max_length=10, default="Unknown")

    pressure_mb = models.FloatField(default=0.0)
    pressure_in = models.FloatField(default=0.0)

    precip_mm = models.FloatField(default=0.0)
    precip_in = models.FloatField(default=0.0)

    humidity = models.IntegerField(default=0)
    cloud = models.IntegerField(default=0)

    feelslike_c = models.FloatField(default=0.0)
    feelslike_f = models.FloatField(default=0.0)

    windchill_c = models.FloatField(default=0.0)
    windchill_f = models.FloatField(default=0.0)

    heatindex_c = models.FloatField(default=0.0)
    heatindex_f = models.FloatField(default=0.0)

    dewpoint_c = models.FloatField(default=0.0)
    dewpoint_f = models.FloatField(default=0.0)

    vis_km = models.FloatField(default=0.0)
    vis_miles = models.FloatField(default=0.0)

    uv = models.FloatField(default=0.0)

    gust_mph = models.FloatField(default=0.0)
    gust_kph = models.FloatField(default=0.0)

    last_updated = models.DateTimeField(default=None, null=True)
     # Air Quality fields
    air_quality_co = models.FloatField(null=True, blank=True)
    air_quality_no2 = models.FloatField(null=True, blank=True)
    air_quality_o3 = models.FloatField(null=True, blank=True)
    air_quality_so2 = models.FloatField(null=True, blank=True)
    air_quality_pm2_5 = models.FloatField(null=True, blank=True)
    air_quality_pm10 = models.FloatField(null=True, blank=True)
    air_quality_us_epa_index = models.IntegerField(null=True, blank=True)
    air_quality_gb_defra_index = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.city} Weather at {self.last_updated}"
