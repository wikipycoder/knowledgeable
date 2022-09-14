from django.db import models
import uuid


class DigitalWallet(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    point = models.PositiveBigIntegerField(default=0)
    dollar = models.FloatField(default=0.0)

    def calculate_dollar(self):
        self.dollar = self.point/100
        return self.dollar
    
    def calculate_point(self):
        self.point = self.dollar*100
        return self.point

    
        




