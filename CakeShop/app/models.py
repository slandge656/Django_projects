from django.db import models

# Create your models here.

class CustomUser(models.Model):
    First_Name=models.CharField(max_length=255,default='')
    Last_Name=models.CharField(max_length=255,default='')
    Mobile_No=models.CharField(max_length=255,default='')
    Email=models.EmailField(max_length=255,default='')
    Password=models.CharField(max_length=255,default='')
    RE_Password=models.CharField(max_length=255,default='')
    last_login_time = models.DateTimeField(null=True, blank=True)
    def __str__(self) -> str:
        return f'{self.First_Name}  {self.Last_Name}'
    
    def register_user(self):
        return self.save()



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
            return Products.objects.filter(category_name=category_id)
        else:
            return  Products.objects.all()