from django.db import models
from face_sets.models import FaceSets
from faces.models import FaceInfo
from datetime import datetime

# Create your models here.
class CompareResults(models.Model):
    """
    人脸搜索结果
    """
    faceset = models.ForeignKey(FaceSets, verbose_name="人脸库", help_text="储存到对应的人脸库",related_name="compare_facesets")
    search_encode = models.CharField(max_length=3000, default="", verbose_name="面部encode")
    related_face = models.ForeignKey(FaceInfo, verbose_name="相关联人脸id", help_text="相关联人脸id",related_name="related_faces")
    related_name = models.CharField(max_length=30, default="", verbose_name="人脸名字")
    tolerance = models.CharField(max_length=30, default="", verbose_name="结果公差")
    response_time = models.CharField(max_length=3000, default="", verbose_name="响应时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '人脸搜索结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tolerance