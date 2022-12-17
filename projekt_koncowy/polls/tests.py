import pytest
import datetime

from django.contrib.auth.models import User
from .models import Product
from .models import Category


from django.test import TestCase

from django.urls import reverse
from django.utils import timezone
from .views import entry_welcome, shopping_list, category_list, add_product, table_view, remove_product, UpdateView, AddProductFormView, AddCategoryFormView, DeleteProductFormView,UpdateProductFormView,AddProductToShopping,BuyProductFormView,RequestProductFormView,ListBuyProductFormView,ListRequestProductFormView
import ipdb

class TestEntryWelcome(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_entry_welcome_1(self):
        print("Method:test_entry_welcome_1.")
        self.assertTemplateUsed('base.html')

    def test_entry_welcome_2(self):
        print("Method:test_entry_welcome_2.")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        loginresp = self.client.get('/polls/', name="welcome", follow=True)
        self.assertContains(loginresp, "Lista produktów")


class TestShoppingList(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_shopping_list_1(self):
        print("Method:")
        self.assertTemplateUsed('shopping_list.html')

    def test_shopping_list_2(self):
        print("Method:test_shopping_list_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        loginresp = self.client.get('/polls/shopping_list/', follow=True)
        self.assertContains(loginresp, "Shopping List")



class TestCategoryList(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_category_list_1(self):
        print("Method:test_category_list_1.")
        self.assertTemplateUsed('categories.html')

    def test_category_list_2(self):
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        loginresp = self.client.get('/polls/categories/',follow=True)
        print("Method:test_category_list_2.")
        self.assertContains(loginresp,"Kategorie produktów")



class TestAddProduct(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_add_product_1(self):
        print("Method: test_add_product_1.")
        self.assertTemplateUsed('createform.html')


    def test_add_product_2(self):
        response=self.client.get('/polls/add_product/', follow=True)
        print("Method:test_add_product_2")
        self.assertRedirects(response, '/polls/accounts/login/?next=/polls/add_product/',status_code=302, target_status_code=200)



class TestTableView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_table_view_1(self):
        print("Method: test_table_view_1.")
        self.assertTemplateUsed('table_view.html')


#przestarzaly test
    # # #sprawdzić czy context nie jest pusty
    # def test_table_view_2(self):
    #     print("Method:test_table_view_2")
    #     self.username = "jrandomuser"
    #     self.password = "qwerty123"
    #     user = User.objects.create(username=self.username)
    #     user.set_password(self.password)
    #     user.save()
    #
    #     self.client.login(username=self.username, password=self.password)
    #     loginresp = self.client.get('/polls/table_view/', follow=True)
    #     self.assertContains(loginresp, "")
#
#
#
class TestRemoveProduct(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_remove_product_1(self):
        print("Method:test_remove_product_1")
        self.assertTemplateUsed('remove_product.html')

    def test_remove_product_2(self):
        response=self.client.post('/polls/product/1/delete/', follow=True)
        print("Method:test_remove_product_2")
        self.assertRedirects(response, '/polls/accounts/login/?next=/polls/product/1/delete/')



class TestAddProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_AddProductFormView_1(self):
        print("Method:test_AddProductFormView_1")
        self.assertTemplateUsed('createform.html')

    def test_AddProductFormView_2(self):#
        print("Method:test_AddProductFormView_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        loginresp = self.client.get('/polls/add_product/', follow=True, status_code=302, target_status_code=301)
        self.assertContains(loginresp, "Save")


class TestAddCategoryFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_AddCategoryFormView_1(self):
        print("Method:test_AddCategoryFormView_1")
        self.assertTemplateUsed('createcategoryform.html')

    def test_AddCategoryFormView_2(self):
        print("Method:test_AddCategoryFormView_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        loginresp = self.client.get('/polls/add_category/', follow=True)
        self.assertContains(loginresp, "Save")
#
#
class TestDeleteProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
    pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_delete_product_formview_1(self):
        print("Method:test_delete_product_formview_1")
        self.assertTemplateUsed('productmodel_confirm_delete.html')


    def test_test_delete_product_formview_2(self):
        print("Method:test_test_delete_product_formview_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        tcategory = Category(name="test_category")
        tcategory.save()
        tproduct = Product(name="test_name",description="test_description",price=9.99,quantity=1,category=tcategory)
        tproduct.save()

        nproduct = Product.objects.all().last()
        url = '/polls/product/' + str(nproduct.id)+ '/delete/'

        self.client.login(username=self.username, password=self.password)
    #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get(url, follow=True)
        #ipdb.set_trace()
        self.assertContains(loginresp, "Are you sure you want to delete")
#
#
#
class UpdateProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_update_product_formview_1(self):
        print("Method:test_update_product_formview_1")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        tcategory=Category(name="test_category")
        tcategory.save()
        tproduct = Product(name="test_name", description="test_description", price=9.99, quantity=1, category=tcategory)
        tproduct.save()

        nproduct = Product.objects.all().last()
        url = '/polls/product/'+str(nproduct.id)+'/update/'

        self.client.login(username=self.username, password=self.password)
        #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get(url, follow=True)
        #ipdb.set_trace()
        self.assertContains(loginresp, "Save")

    def test_update_product_formview_2(self):
        print("Method:test_update_product_formview_2")
        self.assertTemplateUsed('product_form.html')


class AddProductToShopping(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_add_producttoshopping_1(self):
        print("Method:test_add_producttoshopping_1")
        self.assertTemplateUsed('shopping_list.html')

    def test_add_producttoshopping_2(self):
        print("Method:test_add_producttoshopping_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get('/polls/shopping_list/', follow=True)
        self.assertContains(loginresp, "Shopping List")





class RequestProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_request_product_formview_1(self):
        print("Method:test_request_product_formview_1")
        self.assertTemplateUsed('request.html')

    def test_request_product_formview_2(self):
        print("Method:test_request_product_formview_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        tcategory=Category(name="test_category")
        tcategory.save()
        tproduct = Product(name="test_name", description="test_description", price=9.99, quantity=1, category=tcategory)
        tproduct.save()

        nproduct = Product.objects.all().last()
        url = '/polls/product/' + str(nproduct.id) + '/request/'




        self.client.login(username=self.username, password=self.password)
    #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get(url, follow=True)
        self.assertContains(loginresp, "Zapotrzebowanie")


class ListBuyProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_list_buy_product_formview_1(self):
        print("Method:test_list_buy_product_formview_1")
        self.assertTemplateUsed('history.html')

    def test_list_buy_product_formview_2(self):
        print("Method:test_list_buy_product_formview_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get('/polls/buy/', follow=True)
        self.assertContains(loginresp, "History")


class ListRequestProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_list_request_product_formview_1(self):
        print("Method:test_list_request_product_formview_1")
        self.assertTemplateUsed('request.html')

    def test_list_request_product_formview_2(self):
        print("Method:test_list_request_product_formview_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        self.client.login(username=self.username, password=self.password)
        #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get('/polls/request/', follow=True)
        self.assertContains(loginresp, "Zapotrzebowanie")


class BuyProductFormView(TestCase):
    @classmethod
    def setUpTest(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_buy_product_formview_1(self):
        print("Method:test_buy_product_formview_1")
        self.assertTemplateUsed('history.html')

    def test_buy_product_formview_2(self):
        print("Methpd:test_buy_product_formview_2")
        self.username = "jrandomuser"
        self.password = "qwerty123"
        user = User.objects.create(username=self.username)
        user.set_password(self.password)
        user.save()

        tcategory=Category(name="test_category")
        tcategory.save()
        tproduct = Product(name="test_name", description="test_description", price=9.99, quantity=1, category=tcategory)
        tproduct.save()

        nproduct = Product.objects.all().last()
        url = '/polls/product/' + str(nproduct.id) + '/buy/'

        self.client.login(username=self.username, password=self.password)
    #   self.assertTrue(loginresp, 'Could not log in')
        loginresp = self.client.get(url, follow=True)
        self.assertContains(loginresp, "History")