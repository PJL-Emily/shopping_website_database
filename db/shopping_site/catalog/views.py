from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.http import HttpResponse
from datetime import datetime
from .models import Customer, Supplier
from .forms import CustomerForm, SupplierForm


def addCustomer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'customer.html', context)


def addSupplier(request): 
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'supplier.html', context)


def updateSupplier(request, pk):  
    supplier = get_object_or_404(SupplierForm, id=pk)
    form = SupplierForm(request.POST or None, instance=supplier)
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+pk) 
    context = {'form': form}
    return render(request, 'updateSupplier.html', context)


def showUpdatedSupplier(request, pk): 
    context ={} 
    context["data"] = SupplierForm.objects.get(id=pk) 
    return render(request, "showUpdatedSupplier.html", context)

# def hello_world(request):
#     return render(request, 'hello_world.html', {
#         'current_time': str(datetime.now()),
#     })
# from catalog.models import Supplier, Customer

# def lookUpCart(request):
#     product_list = Cart.objects.filter(CartStatus = "in_cart")
#     return render(request, 'lookUpCart.html', {
#         'product_list': product_list,
#     })
# # def post_detail(request, pk):
# #     post = Post.objects.get(pk=int(pk))
# #     return render(request, 'post.html', {'post': post})

# def salesReport(request):

# def lookUpCost(request):


def hello_world(request):
    return HttpResponse("Hello World!")