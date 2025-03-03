from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Departament)
class DepartamentAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    fields = (
        'name', 'number', 'nickname_1', 'nickname_2', 'nickname_3', 'nickname_4', 'nickname_5', 'nickname_6',
        'nickname_7',
        'nickname_8', 'nickname_9', 'nickname_10')


admin.site.register(Section)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'FIO', 'job_title', 'section', 'number_1', 'is_active_vnut_number', 'number_21', 'number_22', 'number_23',
        'is_active_gorod_number', 'number_31', 'number_32', 'number_33')
    list_filter = ('FIO', 'job_title')
    fields = ('section',
              'FIO', 'job_title', 'number_1', 'is_active_vnut_number', 'number_21', 'number_22',
              'number_23',
              'is_active_gorod_number', 'number_31', 'number_32', 'number_33', 'home_vnut',
              'home_41',
              'home_42',
              'home_43')
