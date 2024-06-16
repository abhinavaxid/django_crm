from django import forms
from .models import Customer, Opportunity, Interaction, Contact

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'address', 'email', 'phone']

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['customer', 'description', 'value', 'stage']  # Specify the fields from the Opportunity model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # You can add additional customization here if needed
        self.fields['customer'].queryset = Customer.objects.all()  # Example: Customize queryset for customer field

class InteractionForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            }
        ),
        input_formats=['%Y-%m-%d']
    )
    class Meta:
        model = Interaction
        fields = ['customer', 'interaction_type', 'date', 'notes']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['customer', 'name', 'email', 'phone', 'role']