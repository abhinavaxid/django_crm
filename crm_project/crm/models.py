from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Opportunity(models.Model):
    TYPE_CHOICES1 = [
        ('Initial', 'Initial'),
        ('Qualification', 'Qualification'),
        ('Analysis', 'Analysis'),
        ('Proposal', 'Proposal'),
        ('Negotiation', 'Negotiation'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='opportunities')
    description = models.TextField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=50,choices=TYPE_CHOICES1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return f"Opportunity for {self.customer.name} - {self.stage} ({self.value})"

class Interaction(models.Model):
    TYPE_CHOICES2 = [
        ('Call', 'Call'),
        ('Meeting', 'Meeting'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=50,choices=TYPE_CHOICES2)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.interaction_type} on {self.date}"
