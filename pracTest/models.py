from django.db import models

class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    suburb = models.CharField(max_length=25)
    state = models.CharField(max_length=3)
    postcode = models.IntegerField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Purchase(models.Model):
    orderID = models.CharField(max_length=7)
    customerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderDate = models.DateField()
    shipped = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    shippingDate = models.DateField(null=True, blank=True)
    staffID = models.IntegerField()

    def __str__(self):
        return f"Order {self.orderID} by {self.customerID.firstName} {self.customerID.lastName}"
