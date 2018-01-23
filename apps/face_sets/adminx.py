import xadmin
from .models import FaceSets


class FaceSetsAdmin:
    list_display = ['name', 'desc', 'active', 'add_time']


xadmin.site.register(FaceSets, FaceSetsAdmin)