from django.db import models
from datetime import datetime
import uuid
import os

from face_sets.models import FaceSets
# Create your models here.


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('upload/', filename)


class FaceInfo(models.Model):
    """
    人脸详细信息
    """
    faceset = models.ForeignKey(FaceSets, verbose_name="人脸库", help_text="储存到对应的人脸库",related_name="face_sets")
    name = models.CharField(max_length=100, default="", verbose_name="用户名")
    face_detail = models.CharField(max_length=2000, default="", verbose_name="面部细节数据")
    face_encode = models.CharField(max_length=3000, default="", verbose_name="面部encode")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '人脸详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name