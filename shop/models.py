from django.db import models


class Shop(models.Model):
    shop_name=models.CharField(max_length=30)

    def __str__(self):
        return self.shop_name

class Elect_shop(models.Model):
    shop_name=models.ForeignKey(Shop,on_delete=models.CASCADE,null=True)
    item_name=models.CharField(max_length=30)

    def __str__(self):
        return self.item_name