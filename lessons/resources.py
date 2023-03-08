from import_export import resources, fields
from .models import Day, Lesson, Module, PublicClasses
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget, TimeWidget, DecimalWidget
from django.contrib.auth.models import Group


class DayResource(resources.ModelResource):
    class Meta:
        model = Day
        fields = ('id', 'name', 'short_name', 'day_no',)


class ModuleResource(resources.ModelResource):
    class Meta:
        model = Module
        fields = ('id', 'name',)


class LessonResource(resources.ModelResource):
    module = fields.Field(
        column_name='module',
        attribute='module',
        widget=ForeignKeyWidget(Module, 'name'))

    class Meta:
        model = Lesson
        fields = ('name', 'module',)


class ProductResource(resources.ModelResource):
    start_time = fields.Field(column_name='start_time', attribute='time_field', widget=TimeWidget(format='%H:%M:%S'))
    end_time = fields.Field(column_name='end_time', attribute='time_field', widget=TimeWidget(format='%H:%M:%S'))
    # price = fields.Field(
    #     column_name='price',
    #     attribute='price',
    #     widget=widgets.DecimalWidget()
    # )
    class Meta:
        model = PublicClasses
        fields = ('id', 'day', 'lesson', 'num_places', 'num_weeks', 'start_time', 'end_time', 'price', 'availibility',)
