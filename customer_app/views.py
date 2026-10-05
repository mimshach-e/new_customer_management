from django.contrib import messages
from .models import Customer
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomerForm
from django.urls import reverse_lazy


# Fields that should match when searching
PARTIAL_MATCH_FIELDS = {'name', 'email', 'address'}
SEARCH_FIELDS = ['name', 'email', 'phone', 'address']


# Creating Customer 
class CustomerCreateView(SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer_app/customer_form.html"
    success_message = "A new customer '%(name)s' was created successfully!"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Customer'
        context['submit_label'] = 'Create Customer' 
        return context


# Listing Customers with Searching Features
class CustomerListView(ListView):
    model = Customer
    template_name = "customer_app/customer_list.html"
    context_object_name = "customers"
    paginate_by = 10

    # Listing all customers, searching fields and reading search parameters
    def get_queryset(self):
        queryset = super().get_queryset()
        field = self.request.GET.get('field', '')
        query = self.request.GET.get('q', '').strip()

        # Looking up fields and ppplying the search filter if valid
        if field in SEARCH_FIELDS and query:
            lookup = f'{field}__icontains' if field in PARTIAL_MATCH_FIELDS else f'{field}__iexact'
            queryset = queryset.filter(**{lookup: query})

        return queryset

    # Get default context, let's search form render dropdown and also re-display the user's current field/search text after reload.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_fields'] = SEARCH_FIELDS
        context['current_field'] = self.request.GET.get('field', '')
        context['current_query'] = self.request.GET.get('q', '')
        context['total_count'] = Customer.objects.count()
        return context


# Customer Detail View
class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customer_app/customer_detail.html"
    context_object_name = "customer"


# Customer Update View
class CustomerUpdateView(SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customer_app/customer_form.html"
    success_message = "The customer '%(name)s' was updated successfully!"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit {self.object.name}'
        context['submit_label'] = 'Save Changes' 
        return context


# Customer Delete View
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "customer_app/customer_confirm_delete.html"
    success_url = reverse_lazy('customer_app:customer_list')  
    context_object_name = "customer" 

    def form_valid(self, form):
        messages.success(self.request, f"Customer '{self.object.name}' was deleted.")
        return super().form_valid(form)




class HomeView(TemplateView):
    template_name = "customer_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_customers"] = Customer.objects.count()
        context["recent_customers"] = Customer.objects.order_by("-id")[:4]
        return context
