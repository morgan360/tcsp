from django.db import models
from datetime import date, datetime, time
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


# Create your models here.

class Day(models.Model):
    name = models.CharField(max_length=20, null=True)
    short_name = models.CharField(max_length=3, null=True)
    day_no = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(6), MinValueValidator(0)]
    )

    class Meta:
        verbose_name_plural = "Days"

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=20, null=True)

    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.name


class Term(models.Model):
    pass
    start_date = models.DateField()
    end_date = models.DateField()
    rebook_start_date = models.DateField()
    rebook_switch_date = models.DateField()

    class Meta:
        verbose_name_plural = "Terms"

    def __str__(self):
        return str(self.id)


class Lesson(models.Model):
    name = models.CharField(max_length=30, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lessons:product_list_by_category',
                       args=[self.slug])


class PublicClasses(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 default=1)
    name = models.CharField(max_length=100, null=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=True, )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    num_places = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(16), MinValueValidator(1)]
    )
    num_weeks = models.IntegerField(
        null=True,
        blank=True,
        validators=[MaxValueValidator(16), MinValueValidator(1)]
    )
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    start_time = models.TimeField(verbose_name='Time',
                                  help_text='Enter a time (hours:minutes)',
                                  blank=True,
                                  null=True,
                                  default=None,
                                  auto_now=False,
                                  auto_now_add=False,
                                  )
    end_time = models.TimeField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, null=True, )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Public Classes"
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def get_absolute_url(self):
        return reverse('lessons:product_detail',
                       args=[self.id, self.slug])

    def __str__(self):
        return self.name
