from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.http import get_object_or_404
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from .models import Product
from .models import Category
from .models import Shopping
from .models import History
from .models import Requests
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required  # for function based views
from django.contrib.auth.mixins import LoginRequiredMixin  # for class based views
from django.contrib.auth import get_user
import ipdb
from .forms import AddProductForm
from .forms import AddCategoryForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse()


# Funkcja po zalogowaniu ma wyświetić listę produktów przypisanych do użytkownika posortowanych wedle Kategorii.
@login_required
def entry_welcome(request):
    queryset = Product.objects.all().order_by('category')
    context = {
        'queryset': queryset,
        'user_id': request.user.id
    }
    return TemplateResponse(request, 'base.html', context)


# Funkcja po zalogowaniu ma wyświetić listę produktów przypisanych do użytkownika posortowanych wedle id.
@login_required
def shopping_list(request):
    queryset = Shopping.objects.filter(owner=get_user(request), name="tempShoppingList").order_by('id')
    context = {
        'queryset': queryset
    }
    return TemplateResponse(request, 'shopping_list.html', context)


# Funkcja wyświetla listę kategorii sortując je po nazwie.
@login_required
def category_list(request):
    queryset = Category.objects.all().order_by('name')
    context = {
        'queryset': queryset
    }
    return TemplateResponse(request, 'categories.html', context)


# Funkcja dostępna dla zalogowanych użytkowników pozwala na dodanie nowego produktu do swojej listy.
@login_required
def add_product(request):
    form = (request.POST or None)
    # categories = Category.objects.all().order_by('name')

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        "form": form,
        #      "categories_sel": categories
    }
    return render(request, 'shopping_list.html', context)


# dodanie liczby produktów
# def add_number_of_products(request, product):
#   return HttpResponse()

# Funkcja tylko dla zalogowanych użytkowników wyświetla listę posiadanych produktów.
@login_required
def table_view(request):
    context = {}
    context["dataset"] = Product.objects.all()

    return render(request, "table_view.html", context)


# Funkcja tylko dla zalogowanych użytkowników pozwala na usunięcie produktu z listy produktów posiadanych.
# Na podstawie usuniętych produktów tworzy się lista zakupów.
@login_required
def remove_product(request, id):
    context = {}
    data = get_object_or_404(product, id=id)

    if request.method == "POST":
        data.delete()
        return HttpResponseRedirect("/")
    return render(request, "remove_product.html", context)


# Klasa przy użyciu metody post dodaje produkt.
class AddProductFormView(LoginRequiredMixin, CreateView):
    def get(self, request):
        pr_form = AddProductForm()
        return render(request, 'createform.html', {'product_form': pr_form})

    def post(self, request):
        pr_form = AddProductForm(request.POST)
        if pr_form.is_valid():
            # pobierz dane przeslane z formularza przez post
            v_name = pr_form.cleaned_data['name']
            v_desc = pr_form.cleaned_data['description']
            v_price = pr_form.cleaned_data['price']
            v_quantity = pr_form.cleaned_data['quantity']
            v_category = pr_form.cleaned_data['category']

            # stworz instancje obiektu produkt
            new_product = Product(name=v_name, description=v_desc, price=v_price, quantity=v_quantity,
                                  category=v_category)
            new_product.save()
            # procesowanie danych
            return HttpResponseRedirect('products')


# Klasa przy użyciu metody post dodaje nową kategorię produktu.
class AddCategoryFormView(LoginRequiredMixin, CreateView):
    def get(self, request):
        cat_form = AddCategoryForm()
        return render(request, 'createcategoryform.html', {'category_form': cat_form})

    def post(self, request):
        cat_form = AddCategoryForm(request.POST)
        if cat_form.is_valid():
            # pobierz dane przeslane z formularza przez post
            v_name = cat_form.cleaned_data['name']

            # stworz instancje obiektu category
            new_category = Category(name=v_name)
            new_category.save()
            # procesowanie danych
            return HttpResponseRedirect('categories')


# Klasa ma za zadanie usuwac produkt wcześniej utworzony i przypisany do użytkownika.
class DeleteProductFormView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/polls'
    template_name = 'product/productmodel_confirm_delete.html'


# Klasa ma za zadanie modyfikować produkt wcześniej utworzony i przypisany do użytkownika.
class UpdateProductFormView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = [
        "name",
        "description",
        "price",
        "quantity",
        "category"
    ]
    template_name = 'product/product_form.html'
    success_url = '/polls'


class AddProductToShopping(LoginRequiredMixin, CreateView):
    def get(self, request,pk):
        currUser = request.user
        shopping_list = Shopping.objects.create(name="tempShoppingList",
                                                owner=self.request.user) # temporary name, to enable multiple lists later
        shopping_list.product_list.add(Product.objects.get(id=pk))
        shopping_list.save()

        queryset = Shopping.objects.filter(name="tempShoppingList",
                                                owner=self.request.user)
        context = {
            'queryset': queryset
        }

        return render(request, 'shopping_list.html', context)


class BuyProductFormView(LoginRequiredMixin, CreateView):
    def get(self, request,pk):
        product_id = pk
        product = Product.objects.get(id=product_id)

        new_history = History(name=product.name, description=product.description,
                              price=product.price,category=product.category)
        new_history.save()

        queryset = History.objects.all()
        context = {
            'queryset': queryset
        }
       # ipdb.set_trace()
        return render(request, 'history.html', context)




class RequestProductFormView(LoginRequiredMixin, CreateView):
    def get(self, request,pk):
        product_id = pk
        product = Product.objects.get(id=product_id)

        new_request = Requests(name=product.name, description=product.description,
                              quantity=product.quantity,category=product.category, requestor=request.user)
        new_request.save()

        queryset = Requests.objects.all()
        context = {
            'queryset': queryset
        }
        #  ipdb.set_trace()
        return render(request, 'request.html', context)


class ListBuyProductFormView(LoginRequiredMixin, CreateView):
    def get(self, request):

        queryset = Requests.objects.all()
        context = {
            'queryset': queryset
        }

        return render(request, 'history.html', context)


class ListRequestProductFormView(LoginRequiredMixin, CreateView):
    def get(self, request):

        queryset = Requests.objects.all()
        context = {
            'queryset': queryset
        }

        return render(request, 'request.html', context)










