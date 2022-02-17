from django.db import models


class DbConnectionInfo(models.Model):
    db_name = models.CharField(max_length=40)
    tbl_name = models.CharField(max_length=40,primary_key=True)
    connection_info = models.CharField(max_length=80)

    def __str__(self):
        return self.tbl_name


class MetaDetails(models.Model):
    tbl_name = models.ForeignKey(DbConnectionInfo,max_length=40,on_delete=models.CASCADE)
    meta_value = models.CharField(max_length=40)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.tbl_name) + '-' + str(self.meta_value) + '-' + str(self.date_created)