import xadmin
from .models import CompareResults


class CompareResultsAdmin:
    list_display = ['faceset', 'search_encode', 'related_face', 'tolerance','response_time','related_name','add_time']


xadmin.site.register(CompareResults, CompareResultsAdmin)


