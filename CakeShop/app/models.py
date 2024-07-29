from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=30,default='')

    def __str__(self) -> str:
        return self.category_name
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

class Products(models.Model):
    name=models.CharField(max_length=30,default='')
    price=models.CharField(max_length=30,default='')
    description=models.TextField(default='')
    image=models.ImageField(upload_to='app/Upload/Prod_Img/')
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)

    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            return Products.objects.filter(id=category_id)
        else:
            return  Products.objects.all()