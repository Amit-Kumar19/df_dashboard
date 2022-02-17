from django.db import models


class MetaDetail(models.Model):
    tbl_name = models.CharField(max_length=40)
    meta_value = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.tbl_name