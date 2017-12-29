from django.contrib import admin
from .models import Permission, Category, User, Course, Product, Cart, Comment, Course_Content, Enrollment, Order

# Register your models here.

admin.site.register(Permission)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Comment)
admin.site.register(Course_Content)
admin.site.register(Enrollment)
admin.site.register(Order)
