from django.shortcuts import render
from store.models import Product,StockProduct
from teacher.models import City , Teacher
from category.models import Category
from django.views.generic import TemplateView , CreateView , ListView , UpdateView  , DetailView , DeleteView
from django.urls import reverse_lazy

def home(request):
    # tras os produtos filtrando os que estao available
    products = Product.objects.all().filter(is_available=True) 
    
    context = {
        'products': products,

    }

    return render(request, 'home.html', context)

# product

class ProductListViewAdmin(ListView):
    model = Product
    template_name = 'panel/product/product_view_admin.html'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'panel/product/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_view_admin')

class ProductUpdateView(UpdateView): 
    model = Product
    template_name = 'panel/product/product_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('product_view_admin')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'panel/product/product_delete.html'
    success_url = reverse_lazy('product_view_admin')

# category

class CategoryListView(ListView):
    model = Category
    template_name = 'panel/category/category_view.html'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'panel/category/category_create.html'
    fields = '__all__'
    success_url = reverse_lazy('category_view')

class CategoryUpdateView(UpdateView): 
    model = Category
    template_name = 'panel/category/category_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('category_view')
    
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'panel/category/category_delete.html'
    success_url = reverse_lazy('category_view')

#city

class CityListView(ListView):
    model = City
    template_name = 'panel/city/city_view.html'

class CityDetailView(DetailView):
    model = City
    template_name = 'panel/city/city_detail.html'

class CityCreateView(CreateView):
    model = City
    template_name = 'panel/city/city_create.html'
    fields = '__all__'
    success_url = reverse_lazy('city_view')

class CityUpdateView(UpdateView): 
    model = City
    template_name = 'panel/city/city_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('city_view')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'panel/city/city_delete.html'
    success_url = reverse_lazy('city_view')  


# Teacher views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'panel/Teacher/Teacher_view.html'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'panel/Teacher/Teacher_detail.html'

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'panel/Teacher/Teacher_create.html'
    fields = '__all__'
    success_url = reverse_lazy('Teacher_view')

class TeacherUpdateView(UpdateView): 
    model = Teacher
    template_name = 'panel/Teacher/Teacher_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('Teacher_view')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'panel/Teacher/Teacher_delete.html'
    success_url = reverse_lazy('Teacher_view')

# stock
class StockListView(ListView):
    model = StockProduct
    template_name = 'panel/stock/stock_view.html'

class StockDetailView(DetailView):
    model = StockProduct
    template_name = 'panel/stock/stock_detail.html'

class StockCreateView(CreateView):
    model = StockProduct
    template_name = 'panel/stock/stock_create.html'
    fields = '__all__'
    success_url = reverse_lazy('stock_view')

class StockUpdateView(UpdateView): 
    model = StockProduct
    template_name = 'panel/stock/stock_update.html'
    fields =  '__all__'
    success_url = reverse_lazy('stock_view')

class StockDeleteView(DeleteView):
    model = StockProduct
    template_name = 'panel/stock/stock_delete.html'
    success_url = reverse_lazy('stock_view')   
