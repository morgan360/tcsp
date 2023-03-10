from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.
class PublicSwim(models.Model):
    name = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Public Swimming"
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name


def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)


pre_save.connect(create_slug, sender=PublicSwim)


class SwimSchedule(models.Model):
    swim = models.ForeignKey(PublicSwim, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    DAY_CHOICES = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES, blank=True)
    num_places = models.IntegerField(null=True)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.swimprice_set.exists():
            SwimPrice.objects.create(schedule=self)

    def __str__(self):
        return str(self.swim) + " " + self.day_of_week + " " + str(self.start_time)


class AgeGroup(models.Model):
    age_group = models.CharField(max_length=10)

    def __str__(self):
        return self.age_group


class SwimPrice(models.Model):
    schedule = models.ForeignKey(SwimSchedule, on_delete=models.CASCADE, related_name='prices')
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.age_group) + " " + "€" + str(self.price)
