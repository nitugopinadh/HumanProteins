from django.contrib import admin

# Register your models here.
from .models import Protein, Protein2Drug

admin.site.register(Protein)
admin.site.register(Protein2Drug)
