from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.urls import reverse


class TimeStampModel (models.Model):
    created = models.DateTimeField (auto_now_add=True, auto_now=False)
    updated = models.DateTimeField (auto_now_add=False, auto_now=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'TimeStampModel'
        verbose_name_plural = 'TimeStampModels'


class User(AbstractUser):
    bio = RichTextField()
    nick_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Tags(TimeStampModel):
    name = models.CharField(verbose_name= _('Tag Name'), max_length=120)
    is_active = models.BooleanField(verbose_name=_('Active Or Not?'))


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Tags'
        verbose_name_plural = 'Tagss'


class Category(models.Model):
    name = models.CharField(verbose_name=_('Catory Name'), max_length=120)
    is_active = models.BooleanField(verbose_name=_('Active Or Not?'))

    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'


class BlogQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Blog(TimeStampModel):
    author = models.ForeignKey(User, verbose_name=_('Author'), related_name='user_blogs',
                               on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Blog Title'), max_length=200, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'),
                                 related_name='blogs')
    tags = models.ManyToManyField(Tags, verbose_name=_('Tag'))
    description = RichTextField()
    short_content = models.TextField(verbose_name=_('Short Content'))
    reading_time = models.CharField(max_length=30, verbose_name=_('Reading Time'), null=True, blank=True)

    # SEO details
    meta_description = models.CharField(verbose_name=_('Meta Description'), max_length=150, null=True,
                                        blank=True)
    meta_tags = models.TextField(verbose_name=_('Meta Tags(sep in ,)'))
    image_url = models.URLField(verbose_name=_('Image URL'), null=True, blank=True)
    video_url = models.URLField(verbose_name=_('Video URL'), null=True, blank=True)

    published = models.BooleanField(default=False, verbose_name=_('Published ?'))
    order_by = models.IntegerField(default=1, verbose_name=_('Blog Order'))
    visitor_count = models.IntegerField(default=1, verbose_name=_('Visitor Count'))
    # user = models

    is_trending = models.BooleanField(default=False, verbose_name=_('Trending?'))
    is_featured = models.BooleanField(default=False, verbose_name=_('Featured?'))

    def get_absolute_path(self):
        return reverse('detail_post_page', kwargs={'slug': str(self.slug)})

    # def default_image_url(self):
    #     if not self.image_url:
    #         return "Default"
    #     return self.image_url

    # def update_count(self):
    #     blog = Blog.objects.get(id=self.id)
    #     blog.visitor_count += 1
    #     blog.save()

    def __str__(self):
        return str(self.title) if self.title else ''






