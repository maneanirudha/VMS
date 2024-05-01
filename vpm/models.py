from django.db import models

class Vendor(models.Model):
    name = models.CharField(default="",max_length=150,null=True)
    contact_details = models.TextField()
    address = models.TextField(default="",max_length=150)
    vendor_code = models.CharField(default="",max_length=10)
    on_time_delivery_rate = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fullfillment_rate = models.FloatField(default=0.0)
    
    @property
    def json(self):
        return{
            "id": self.pk,
            "name": self.name,
            "address":self.address,
            "vendor_code":self.vendor_code,
            "on_time_delivery_rate":self.on_time_delivery_rate,
            "average_response_time":self.average_response_time,
            "fullfillment_rate":self.fullfillment_rate
        }
