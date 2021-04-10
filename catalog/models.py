from django.db import models

# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(blank=True)
#     photo = models.URLField(blank=True)
#     location = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.title
class Customer(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    CID = models.AutoField(primary_key=True)
    Password = models.CharField(max_length=8)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Gender = models.CharField(max_length=1, choices = GENDER)
    BDate = models.DateField()
    City = models.CharField(max_length=50)
    def __str__(self):
        return self.Firstname, self.Lastname

class Supplier(models.Model):
    SID = models.AutoField(primary_key=True)
    SName = models.CharField(max_length=50)
    class Meta:
        unique_together = ('SID', 'SName')
    def __str__(self):
        return self.SName

# class Cart(models.Model):
#     CART_STATUS = (
#         ('in_cart', 'Product is in the cart'),
#         ('ordered', 'Product is ordered'),
#         ('deleted', 'Product is deleted'),
#     )
#     CartID = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer, related_name = "carts", on_delete=models.CASCADE)
#     product = models.ForeignKey("Product", related_name = "carts", on_delete=models.CASCADE)
#     CartStatus = models.CharField(max_length=1, choices = CART_STATUS)
#     class Meta:
#         unique_together = ('CartID', 'customer', 'product')
#     def __str__(self):
#         return self.CartID

# class Warehouse(models.Model):
#     product = models.ManyToManyField(Product, through='Store')
# class Store(models.Model):
#     Quantity = models.IntegerField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
#     class Meta :
#         db_table = "Store"
# class Supplier(models.Model):
#     product = models.ManyToManyField(Product, through='Supply')
# class Supply(models.Model):
#     Quantity = models.IntegerField()
#     UnitCost = models.IntegerField()
#     SupplyDate = models.DateField()
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
#     class Meta :
#         db_table = "Supply"
