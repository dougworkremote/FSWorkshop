from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Course, Product, Enrollment, Cart
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# get_object_or_404

def index(request):
    return render(request, 'lms/index.html', {})

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

def courses(request):
    courses = Course.objects.all()
    return render(request, 'lms/courses.html', {'courses':courses})

def course(request, course_id):
    course = Course.objects.get(pk=course_id)
    course_content = course.course_contents.all()
    context = {
        'course':course,
        'course_content':course_content
    }
    return render(request, 'lms/course.html', context)

def products(request):
    products = get_object_or_404(Product, Product.objects.all())
    return render(request, 'lms/products.html', {'products':products})

def product(request, product_id):
    product = get_object_or_404(Product, Product.objects.get(pk=product_id))
    return render(request, 'lms/product.html', {'product':product})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'lms/signup.html', {'form':form})

def enrollments(request):
    user_id = False
    enrollments = get_object_or_404(Enrollment, Enrollment.objects.get(user=session.user_id))
    return render(request, 'lms/enrollments.html', {'enrollments':enrollments})

def enrollment(request, enrollment_id):
    # get user id from session
    user_id = False
    enrollment = get_object_or_404(Enrollment, Enrollment.objects.get(pk=enrollment_id, user=user_id))
    return render(request, 'lms/enrollment.html', {'enrollment':enrollment})

def cart(request):
    # get user id from session
    user_id = False;
    cart = get_object_or_404(Cart, Cart.objects.get(user=user_id))
    return render(request, 'lms/cart.html', {'cart':cart})

