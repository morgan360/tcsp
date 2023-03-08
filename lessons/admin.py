from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Category, PublicClasses, Lesson, Day, Term, Module
from .forms import ProductForm
from .resources import DayResource, LessonResource, ProductResource


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(ImportExportModelAdmin):
    # form = ProductForm
    list_display = ('id', 'name', 'slug', 'lesson', 'day', 'start_time', 'price', 'available',)
    resource_class = ProductResource
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


class LessonAdmin(ImportExportModelAdmin):
    list_display = ('name', 'module',)


# @admin.register(Day)
class DayAdmin(ImportExportModelAdmin):
    list_display = ('name',)


class PersonAdmin(ImportExportModelAdmin):
    pass


class TermAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'rebook_start_date', 'rebook_switch_date')


class ModuleAdmin(ImportExportModelAdmin):
    list_display = ('name',)


admin.site.register(PublicClasses, ProductAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Module, ModuleAdmin)
