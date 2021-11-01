from django.contrib import admin
from .models import *

admin.site.register(MetaTags)

class PostPriceAdmin(admin.StackedInline):
    model = PriceSubCategory


@admin.register(PriceCategory)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostPriceAdmin]

    class Meta:
        model = PriceCategory
