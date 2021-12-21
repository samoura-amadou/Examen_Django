from django.db import models
from django.utils.html import format_html

class Persona(models.Model):
    # prenom
    first_name = models.CharField(max_length=50)
    # nom
    last_name = models.CharField(max_length=50)
    # address
    address_street = models.CharField(max_length=100)
    # numéro adresse
    address_number = models.IntegerField()
    # ville adresse
    city = models.CharField(max_length=50)
    # pays adresse
    country = models.CharField(max_length=50)
    # code postal
    postcode = models.IntegerField()
    # email
    email = models.CharField(max_length=50)
    # username
    username = models.CharField(max_length=50)
    # password
    password = models.CharField(max_length=50)
    # age
    age = models.IntegerField()
    # photo
    picture = models.TextField()

    def __str__(self):
        return f"({self.id}) {self.first_name} {self.last_name}"