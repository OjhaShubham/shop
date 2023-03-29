from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from .forms import ShopForm


def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop_list.html', {'shops': shops})


def shop_detail(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, 'shop_details.html', {'shop': shop})


def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save()
            return redirect('shop_details', pk=shop.pk)
    else:
        form = ShopForm()
    return render(request, 'shop_form.html', {'form': form})


def shop_update(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            shop = form.save()
            return redirect('shop_details', pk=shop.pk)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop_form.html', {'form': form})


def search_shops(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        distance = float(request.POST.get('distance'))
        shops = Shop.objects.filter(latitude__range=(latitude - (distance / 111), latitude + (distance / 111)), longitude__range=(longitude - (distance / 111), longitude + (distance / 111)))
        return render(request, 'search_results.html', {'shops': shops})
    else:
        return render(request, 'search_form.html')
