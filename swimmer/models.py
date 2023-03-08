from django.db import models
from django.conf import settings


# Create your models here.
# Stores the swimmer details with link to guardians
class Swimling(models.Model):
    guardian = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_swimlings',
                             blank=True, null=True, )
    first_name = models.CharField(max_length=255, blank=True, null=True, )
    last_name = models.CharField(max_length=255, blank=True, null=True, )
    dob = models.DateField(null=True)
    school_role_number = models.CharField(max_length=6, blank=True,
                                          null=True, )
    notes = models.TextField(null=True, blank=True)
    # id from student details table in wordpress site
    wp_student_id = models.IntegerField(null=True)

    def __str__(self):
        return self.first_name + "  " + str(self.last_name)
