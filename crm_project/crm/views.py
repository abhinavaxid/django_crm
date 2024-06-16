from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Contact, Opportunity, Interaction
from rest_framework import viewsets
from .serializers import CustomerSerializer, ContactSerializer, OpportunitySerializer, InteractionSerializer
from .forms import CustomerForm, OpportunityForm, InteractionForm, ContactForm


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_confirm_delete.html', {'customer': customer})

def dashboard(request):
    num_customers = Customer.objects.count()
    num_opportunities = Opportunity.objects.count()
    num_interactions = Interaction.objects.count()
    context = {
        'num_customers': num_customers,
        'num_opportunities': num_opportunities,
        'num_interactions': num_interactions,
    }
    return render(request, 'dashboard.html', context)

def opportunity_list(request):
    opportunities = Opportunity.objects.all()
    return render(request, 'opportunity_list.html', {'opportunities': opportunities})

def opportunity_create(request):

    if request.method == 'POST':
        form = OpportunityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opportunity_list')  
    else:
        form = OpportunityForm()
    return render(request, 'opportunity_form.html', {'form': form})

def opportunity_edit(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    if request.method == 'POST':
        form = OpportunityForm(request.POST, instance=opportunity)
        if form.is_valid():
            form.save()
            return redirect('opportunity_list')  
    else:
        form = OpportunityForm(instance=opportunity)
    return render(request, 'opportunity_form.html', {'form': form})

def opportunity_detail(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    return render(request, 'opportunity_detail.html', {'opportunity': opportunity})

def opportunity_delete(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    
    if request.method == 'POST':
        opportunity.delete()
        return redirect('opportunity_list')  # Redirect to a success page, like the opportunity list
    else:
        # Handle GET request, maybe show a confirmation page
        return render(request, 'opportunity_confirm_delete.html', {'opportunity': opportunity})

def interaction_list(request):
    interactions = Interaction.objects.all()
    return render(request, 'interaction_list.html', {'interactions': interactions})

def interaction_create(request):
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interaction_list')  # Redirect to the interaction list view
    else:
        form = InteractionForm()
    return render(request, 'interaction_form.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact_confirm_delete.html', {'object': contact})



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
