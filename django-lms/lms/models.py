from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    banner = models.CharField(max_length=255, null=True)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    courses = models.ManyToManyField('Course', through='Enrollment')
    # products = models.ManyToManyField('Product', null=True, blank=True)

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    summary = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail = models.CharField(max_length=255, null=True, blank=True)
    banner = models.CharField(max_length=255, null=True, blank=True)
    staging = models.BooleanField()
    start_date = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    comments_enabled = models.BooleanField()
    max_users = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    course_contents = models.ManyToManyField('Course_Content')
    students = models.ManyToManyField(Student, through='Enrollment')
    # related_courses = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course)

class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_total = models.DecimalField(max_digits=7, decimal_places=2)
    products = models.ManyToManyField(Product)

class Comment(models.Model):
    ip = models.GenericIPAddressField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    approved = models.BooleanField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Course_Content(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    additional_resource_link = models.CharField(max_length=255, null=True, blank=True)
    order = models.PositiveSmallIntegerField()

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    last_acessed = models.DateTimeField(auto_now=True)
    # course_contents = models.ManyToManyField(Course_Content, through='Course')

class Order(models.Model):
    invoice_number = models.CharField(max_length=255, unique=True)
    paid_total = models.DecimalField(max_digits=7, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
