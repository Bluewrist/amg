from.models import product_category, Product,Order,OrderItem,Type
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.shortcuts import redirect,render
from django.http import JsonResponse
import json
from django.db.models import Q



def product_list(request):
    q= request.GET.get('q')
    if request.GET.get('q') if request.GET.get('q') != None else "":
        all_products  = Product.objects.filter(Q(car_type__name__icontains=q)|
                                               Q(part_name__icontains=q)|
                                               Q(part_number__icontains=q)|
                                               Q(part_number_1__icontains=q)|
                                               Q(part_number_2__icontains=q)
                                               )
    else:
        all_products = Product.objects.all()
    all_categories  =  Type.objects.all()
    all_types  =  Type.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(all_products, 20)
    try:
        all_products  = paginator.page(page)        
    except PageNotAnInteger:
        all_products  = paginator.page(1)
    except EmptyPage:
        all_products  = paginator.page(paginator.num_pages)
    context  = {
        "pdts":all_products,
        "cats":all_categories,
        "all_types":all_types,
    }
    return context   
