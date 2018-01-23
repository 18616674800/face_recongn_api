from django.db import models
from datetime import datetime
# Create your models here.


class FaceSets(models.Model):
    """
    人脸库名
    """
    name = models.CharField(default="", max_length=50, verbose_name="人脸库名", help_text="人脸库名")
    desc = models.TextField(default="", verbose_name="人脸库名描述", help_text="人脸库名描述")
    active = models.BooleanField(default=True, verbose_name="是否激活", help_text="是否激活")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "人脸库名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
