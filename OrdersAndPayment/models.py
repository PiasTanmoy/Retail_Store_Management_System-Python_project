from django.db import models

# Create your models here.

class Payment(models.Model):
    #customers = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Invoice_num = models.IntegerField(blank=True)
    payment_date = models.DateField(blank=True)
    Amount = models.IntegerField(blank=True)

    def __str__(self):
        return self.Invoice_num

class Order(models.Model):
    #customers = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Order_status = models.CharField(max_length=200, default="Order Status")
    Order_date = models.DateField(blank=True)
    Require_date = models.DateField(blank=True)
    Shipped_date = models.DateField(blank=True)

    def __str__(self):
        return self.Order_status

class Order_Detail(models.Model):
    #order = models.ForeignKey(Order, on_delete=models.CASCADE,default=1)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE,default=1)
    quantity = models.IntegerField(blank=True)
    price_each = models.IntegerField(blank=True)

    def __str__(self):
        return self.quantity