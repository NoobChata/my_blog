from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) #博客题目
    category = models.CharField(max_length = 50,blank = True) #博客标签
    date_time = models.DateTimeField(auto_now_add = True) #博客日期时间
    content = models.TextField(blank = True) #正文


    #py2使用__unicode__，py3使用__str__
    def __str__(self):
        return self.title

    class Meta:  #按时间降序
        ordering = ['-date_time']