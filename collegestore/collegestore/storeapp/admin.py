from django.contrib import admin
from .models import Department, Course, Order


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Department, DepartmentAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'department', 'course',
                    'purpose', 'materials_provided']
    list_per_page = 20


admin.site.register(Order, OrderAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
