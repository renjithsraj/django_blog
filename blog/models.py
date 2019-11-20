from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     bio = models.TextField(max_length=500, blank=True)
    
#     def __str__(self):
#         pass

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'



class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'TimeStampModel'
        verbose_name_plural = 'TimeStampModels'
        
        
class Tags(TimeStampModel):
    name = models.CharField(verbose_name= _('Tag Name'), max_length=120)
    is_active = models.BooleanField(verbose_name=_('Active Or Not?'))
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tags'
        verbose_name_plural = 'Tagss'


class Category(TimeStampModel):
    name = models.CharField(verbose_name=_('Catory Name'), max_length=120)
    is_active = models.BooleanField(verbose_name=_('Active Or Not?'))
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

class Blog(TimeStampModel):
    title = models.CharField(verbose_name=_('Blog Title'), max_length=110)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    tags = models.ManyToManyField(Tags, verbose_name=_('Tag'))
    # user = models


    def __str__(self):
        return 

    def __unicode__(self):
        return 
