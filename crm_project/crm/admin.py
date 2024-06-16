from django.contrib import admin
from .models import Customer, Contact, Opportunity, Interaction

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class OpportunityInline(admin.TabularInline):
    model = Opportunity
    extra = 1

class InteractionInline(admin.TabularInline):
    model = Interaction
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    inlines = [ContactInline, OpportunityInline, InteractionInline]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'customer', 'email', 'phone', 'role']

@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ['customer', 'description', 'value', 'stage', 'created_at', 'updated_at']

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['customer', 'interaction_type', 'date', 'notes']
