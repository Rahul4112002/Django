from django.contrib import admin
from features.models import Features
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature_icon','feature_title','feature_desc')
    
admin.site.register(Features,FeaturesAdmin)
# Register your models here.
