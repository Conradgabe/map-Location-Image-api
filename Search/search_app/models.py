from django.db import models

import geocoder

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng # return the latitude and longitude
        self.lat = g[0]
        self.lng = g[1]
        return super(Address, self).save(*args, **kwargs)

        def __str__(self):
            return self.address
