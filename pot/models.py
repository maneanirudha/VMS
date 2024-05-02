from django.db import models
from vpm.models import Vendor
from datetime import timedelta
from django.utils import timezone

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=150)
    vendor = models.ForeignKey(Vendor,on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(default=timezone.now)  # Set default to current date and time
    delivery_date = models.DateTimeField(default=timezone.now() + timedelta(days=5))  # Set default to current date + 5 days
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(default="pending",max_length=15)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgement_date = models.DateTimeField(default=timezone.now)

    
    @property
    def json(self):
        return{
            "id": self.pk,
            "po_number":self.po_number,
            "order_date":self.order_date,
            "delivery_date":self.delivery_date,
            "items":self.items,
            "quantity":self.quantity,
            "status":self.status,
            "quality_rating":self.quality_rating,
            "issue_date":self.issue_date,
            "acknowledgement_date":self.acknowledgement_date
        }