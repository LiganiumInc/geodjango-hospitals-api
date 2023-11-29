from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import *


class ADM0Admin(LeafletGeoAdmin):
    list_display = ["pk", "adm_name", "adm_type","background_story"]

    list_display_links = ["adm_name"]

class ADM1Admin(LeafletGeoAdmin):
    list_display = ["pk", "adm_name", "adm_type","background_story"]

    list_display_links = ["adm_name"]

class ADM2Admin(LeafletGeoAdmin):
    list_display = ["pk", "adm_name", "adm_type","background_story"]

    list_display_links = ["adm_name"]

class ADM3Admin(LeafletGeoAdmin):
    list_display = ["pk", "adm_name", "adm_type","background_story"]

    list_display_links = ["adm_name"]

class ADM4Admin(LeafletGeoAdmin):
    list_display = ["pk", "adm_name", "adm_type","background_story"]

    list_display_links = ["adm_name"]



admin.site.register(ADM0, ADM0Admin)
admin.site.register(ADM1, ADM1Admin)
admin.site.register(ADM2, ADM2Admin)
admin.site.register(ADM3, ADM3Admin)
admin.site.register(ADM4, ADM4Admin)

admin.site.register(Document)