from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Course, Product, Enrollment, Cart, Student
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import stripe
import os
import datetime

stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}
stripe.api_key = stripe_keys['secret_key']

# get_object_or_404

def index(request):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    any_new_courses = Course.objects.filter(date_created__gte=yesterday).exists()
    any_new_products = Product.objects.filter(date_created__gte=yesterday).exists()
    context = {
        'any_new_courses':any_new_courses,
        'any_new_products':any_new_products
    }
    return render(request, 'lms/index.html', context)

def category(request, category_id):
    category = Category.objects.get(pk=category_id)
    courses = category.course_set.all()
    context = {
        'category':category,
        'courses':courses
    }
    return render(request, 'lms/category.html', context)

def categories(request):
    categories = Category.objects.all()
    return render(request, 'lms/categories.html', {'categories':categories})

def courses(request, page=None):
    courses = Course.objects.all()
    course_count = courses.count()
    courses_per_page = 5
    pages = -(-course_count // courses_per_page)
    course_default_subset_start = 0
    course_default_subset_end = 5
    if page:
        course_default_subset_start = (page - 1) * course_default_subset_end
        course_default_subset_end = page * course_default_subset_end
    course_query = courses[course_default_subset_start:course_default_subset_end]
    paginate = False
    previous_page = None
    next_page = None
    if course_count > course_query.count():
        paginate = True
    if page is None:
        previous_page = 1
        next_page = 2
    else:
        previous_page = page - 1
        next_page = page + 1
    context = {
        'courses':course_query,
        'course_count':course_count,
        'paginate': paginate,
        'pages':pages,
        'page':page,
        'previous_page':previous_page,
        'next_page':next_page,
    }
    return render(request, 'lms/courses.html', context)

def search(request):
    return render(request, 'lms/search', {})

def course(request, course_id):
    if request.user.is_authenticated:
        student = Student.objects.get(user=request.user)
        if Enrollment.objects.filter(course=course_id, student=student).exists():
            enrollment = Enrollment.objects.get(course=course_id, student=student)
            enrollment_url = '/enrollment/' + str(enrollment.id)
            return redirect(enrollment_url)
    course = Course.objects.get(pk=course_id)
    course_content = course.course_contents.all()
    products = Product.objects.filter(courses=course).distinct()
    context = {
        'course':course,
        'course_content':course_content,
        'products':products
    }
    return render(request, 'lms/course.html', context)

def products(request, page=None):
    products = Product.objects.all()
    product_count = products.count()
    products_per_page = 5
    pages = -(-product_count // products_per_page)
    product_default_subset_start = 0
    product_default_subset_end = 5
    if page:
        product_default_subset_start = (page - 1) * product_default_subset_end
        product_default_subset_end = page * product_default_subset_end
    product_query = products[product_default_subset_start:product_default_subset_end]
    paginate = False
    previous_page = None
    next_page = None
    if product_count > product_query.count():
        paginate = True
    if page is None:
        previous_page = 1
        next_page = 2
    else:
        previous_page = page - 1
        next_page = page + 1
    context = {
        'products':product_query,
        'product_count':product_count,
        'paginate': paginate,
        'pages':pages,
        'page':page,
        'previous_page':previous_page,
        'next_page':next_page,
    }
    return render(request, 'lms/products.html', context)

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    courses = product.courses.all()
    context = {
        'product':product,
        'courses':courses
    }
    return render(request, 'lms/product.html', context)

def signup(request):
    # test sign up func change
    form = UserCreationForm()
    if request.method != 'POST':
        return render(request, 'signup.html', {'form':form})
    formPost = UserCreationForm(request.POST)
    if not formPost.is_valid():
        return render(request, 'signup.html', {'form':form})
    formPost.save()
    username = formPost.cleaned_data.get('username')
    password = formPost.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    if user is None:
        return render(request, 'signup.html', {'form':form})
    login(request, user)
    student = Student(user=user, first_name='', last_name='', email='')
    student.save()
    return redirect('index')

@login_required
def enrollments(request):
    student = Student.objects.get(user=request.user)
    enrollments = student.enrollment_set.all()
    return render(request, 'lms/enrollments.html', {'enrollments':enrollments})

@login_required
def enrollment(request, enrollment_id):
    student = Student.objects.get(user=request.user)
    enrollment = Enrollment.objects.get(pk=enrollment_id)
    if enrollment.student.id is not student.id:
        return redirect('enrollments')
    course_contents = enrollment.course.course_contents.all()
    context = {
        'enrollment':enrollment,
        'course_contents':course_contents
    }
    return render(request, 'lms/enrollment.html', context)

# @login_required
# def enrollment_content(request, enrollment_id, content_id):
#     student = Student.objects.get(user=request.user)
#     enrollment = Enrollment.objects.get(pk=enrollment_id)
#     content = Course_Content.objects.get(pk=content_id)    
#     if enrollment.student.id is not student.id:
#         return redirect('enrollments')
#     if content not in enrollment.course.course_contents.all():
#         return redirect('enrollments')
#     # get ids of order +- 1 from content
#     # move comments to course_contents, not course
#     # display nested comments
#     # add comment form as 'reply' link to each comment
#     # w/ hidden field parent=comment.id
#     # comment.approved=0 as default
#     context = {
#         'content':content,
#         'next_content': '',
#         'prev_content': ''
#     }
#     return render(request, 'lms/enrollment_content.html', {'content':content})

@login_required
def add_to_cart(request, product_id):
    cart = Cart.objects.filter(user=request.user).exists()
    if cart is False:
        cart = Cart(user=request.user, cart_total=0)
        cart.save()
    else:
        cart = Cart.objects.filter(user=request.user)[0]
    product = Product.objects.get(pk=product_id)
    product_exists = cart.products.filter(pk=product_id).exists()
    if product_exists is True:
        return render(request, 'lms/add_to_cart.html', {'error':'product already added to cart'})
    cart.cart_total = cart.cart_total + product.price
    cart.save()
    cart.products.add(product)
    return render(request, 'lms/add_to_cart.html', {'product':product}) 

@login_required
def cart(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.products.all()
    context = {
        'cart':cart,
        'products':products
    }
    return render(request, 'lms/cart.html', context)

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    charge_description = ''
    for product in cart.products.all():
        charge_description += product.name
        charge_description += ', '
    # why cant stripe communicate?
    context = {
        'cart':cart,
        'charge_description':charge_description,
        'key':stripe_keys['publishable_key']
    }
    return render(request, 'lms/checkout.html', context)

@login_required
def charge(request):
    if request.method != 'POST':
        return redirect('checkout')
    student = Student.objects.get(user=request.user)
    cart = Cart.objects.get(user=request.user)
    customer = stripe.Customer.create(
        email=student.email,
        source=request.POST['stripeToken']
        # cleaned_data()?
    )
    charge_description = ''
    for product in cart.products.all():
        charge_description += product.name
        charge_description += ', '
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=cart.cart_total,
        currency='usd',
        description=charge_description
    )
    for product in cart.products.all():
        for course in product.courses.all():
            enrollment = Enrollment(student=student, course=course)
            enrollment.save()
    cart = delete()
    return render(request, 'lms/charge.html', {'cart_total':cart.cart_total})

@login_required
def receipt(request):
    return render(request, 'lms/receipt.html', {})
