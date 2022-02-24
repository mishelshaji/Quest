from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseNotFound
from .forms import *
from .models import *
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_list(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'administrator/category/list.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    context = {}
    if request.method == 'GET':
        context['form'] = CategoryForm()
        return render(request, 'administrator/category/create.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            context['form'] = form
            return render(request, 'administrator/category/create.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_update(request, id):
    context = {}
    # try:
    #     category = Category.objects.get(id=id)
    # except Category.DoesNotExist:
    #     return HttpResponseNotFound()
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        context['form'] = CategoryForm(instance=category)
        return render(request, 'administrator/category/create.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            context['form'] = form
            return render(request, 'administrator/category/create.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('category_list')


class BrandListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Brand
    template_name = 'administrator/brand/list.html'
    # context_object_name = 'data'

    def test_func(self):
        return self.request.user.is_superuser


class BrandCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'administrator/brand/create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
    
    # def get_success_url(self):
    #     return reverse('brand_list')

    def test_func(self):
        return self.request.user.is_superuser


class BrandUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'administrator/brand/create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')
    pk_url_kwarg = 'id'
    model = Brand

    # def get_object(self):
    #     id_ = self.kwargs.get('id')
    #     return get_object_or_404(Brand, id=id_)

    def test_func(self):
        return self.request.user.is_superuser


class BrandDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Brand
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('brand_list')
    template_name = 'administrator/brand/delete.html'

    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    template_name = 'administrator/product/list.html'
    queryset = Product.objects.all().select_related('brand', 'category')

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def product_create(request):
    context = {}
    if request.method == 'GET':
        context['form'] = ProductForm()
        return render(request, 'administrator/product/create.html', context)
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
            return render(request, 'administrator/product/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def product_update(request, id):
    context = {}
    product = get_object_or_404(Product, id=id)
    if request.method == 'GET':
        context['form'] = ProductForm(instance=product)
        return render(request, 'administrator/product/create.html', context)
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            context['form'] = form
            return render(request, 'administrator/product/create.html', context)


@login_required
@user_passes_test(lambda u: u.is_superuser or u.is_staff)
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.status = 'Inactive'
    product.save()
    return redirect('product_list')