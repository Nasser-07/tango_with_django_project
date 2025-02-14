from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Category, Page


def index(request):
    # Query the database for a list of all categories, sorted by likes (descending)
    category_list = Category.objects.order_by('-likes')[:5]

    # Create a context dictionary to pass data to the template
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list
    }

    # Render the template with context data
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)
