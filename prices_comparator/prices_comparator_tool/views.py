from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.db.models import F


from .models import  Product, ProductCategory
from .forms import ProductCategoryForm, ProductForm

def index(request):
    form= ProductCategoryForm()
    products=ProductCategory.objects.all()
    if request.method == 'POST':
        delete_param=request.POST.get('delete')
        if delete_param is not None:
            to_delete=get_object_or_404(ProductCategory, id=request.POST['delete'])
            to_delete.delete()
            return redirect('home')
        else:
            product = ProductCategory(product_name = request.POST['product_name'],measure_units=request.POST['measure_units'])
            measure_unit = product.measure_units
            product.save()
            return render(
                request,
                'index.html',
                context={
                "form":form,
                'products':products,
                'measure_unit':measure_unit
                }
                )
    return render(
            request,
            'index.html',
            context={
            "form":form,
            'products':products
            }
            )
    

def edit_product_category(request,pk):
    to_edit = get_object_or_404(ProductCategory, id=pk)
    if request.method == 'GET':
        form= ProductCategoryForm(instance=to_edit)  
        return render(request,'edit_product_category.html',
                    {
                        'form':form
                        }) 
    elif request.method == 'POST':
        to_edit.product_name=request.POST['product_name']
        to_edit.measure_units=request.POST['measure_units']
        to_edit.save()
        return redirect('home')
    

def edit_product(request,pk):
    to_edit = get_object_or_404(Product,id=pk)
    if request.method == 'GET':
        form= ProductForm(instance=to_edit)  
        return render(request,'edit_product.html',
                    {
                        'form':form
                        }) 
    elif request.method == 'POST':
        to_edit.product_name = request.POST['product_name']
        to_edit.product_weight_volume_longitude = request.POST['product_weight_volume_longitude']
        to_edit.product_price = request.POST['product_price']
        to_edit.total_units = request.POST['total_units']
        to_edit.save()
        return redirect('home')



def delete_product_category(request,pk):
    to_delete=get_object_or_404(ProductCategory, id=pk)
    if request.method == 'POST':
        to_delete.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect('home')
    return render(request, 'delete.html', {'product': to_delete})


def add_products_to_compare(request,pk):
    form = ProductForm()
    products = Product.objects.filter(product_category__id=pk).annotate(
        price_per_measure_unit = 100*F('product_price')/(F('product_weight_volume_longitude')*F('total_units'))).order_by('price_per_measure_unit')
    measure_unit = ProductCategory.objects.get(id=pk).measure_units
    if request.method == 'POST':
        delete_param=request.POST.get('delete')
        if delete_param is not None:
            to_delete=get_object_or_404(Product, id=request.POST['delete'])
            to_delete.delete()
            return redirect('add_products_to_compare',pk)
        else:
            product_category = get_object_or_404(ProductCategory, id=pk)
            product=Product(
            product_name=request.POST['product_name'],
            product_weight_volume_longitude=request.POST['product_weight_volume_longitude'],
            product_price=request.POST['product_price'],
            total_units=request.POST['total_units'],
            product_category=product_category
            )
            product.save()
            return render(request, 'products_comparision.html', 
                            {
                            'form': form,
                            'products':products
                            }
                            )

    return render(request, 'products_comparision.html', 
                {
                    'form': form,
                    'products':products,
                    'measure_unit':measure_unit
                }
            )