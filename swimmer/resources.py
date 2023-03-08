from import_export import resources, fields
from .models import Swimling
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


#

class SwimlingResource(resources.ModelResource):
    class Meta:
        model = Swimling
        fields = ('id', 'user', 'first_name', 'last_name', 'notes', 'dob', 'school_role_number',)
