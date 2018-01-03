from django.contrib import admin
from .models import Category, Course, Product, Cart, Comment, Course_Content, Enrollment, Order, Student

# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Comment)
admin.site.register(Course_Content)
admin.site.register(Enrollment)
admin.site.register(Order)
admin.site.register(Student)

# put Users back in?
