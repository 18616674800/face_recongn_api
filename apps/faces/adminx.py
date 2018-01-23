import xadmin
from xadmin import views
from .models import FaceInfo


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Face Recognition"
    site_footer = "Face Recognition"
    # menu_style = "accordion"


class FaceInfoAdmin(object):
    list_display = ['id','faceset', 'name', 'face_detail', 'face_encode','add_time']


xadmin.site.register(FaceInfo, FaceInfoAdmin)
