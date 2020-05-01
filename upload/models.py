from django.db import models

# Create your models here.

# Create your models here.
class userfile(models.Model):
    username = models.CharField(max_length = 30)
    courseNum = models.CharField(max_length = 10,null=True)
    headImg = models.FileField(upload_to= './files/')
    #所以是用upload_to来指定文件存放的前缀路径
    def __str__(self):
        return self.courseNum
