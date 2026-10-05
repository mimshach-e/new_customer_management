from django.db import models
from django.urls import reverse


# Creating Customer Model.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Ordering by Name of Customer
    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """ Used by CreateView and UpdateView to redirect after a successful save,
and by templates to link to this customer's detail page."""
        
        return reverse('customer_app:customer_detail', kwargs={'pk': self.pk})
