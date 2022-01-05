from django.db import models

class Item(models.Model):
    Name=models.CharField(max_length=25)
    Description=models.TextField()
    Cost_per_Item=models.DecimalField(max_digits=19, decimal_places=2)
    Stock_quantity=models.DecimalField(max_digits=19, decimal_places=2)
    Volume=models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    def Calc_Volume(self):
        V=self.Cost_per_Item * self.Stock_quantity
        return V
    def save(self, *args, **kwargs):
        self.Volume=self.Calc_Volume()
        super(Item, self).save()
    def __str__(self):
        return self.Name

