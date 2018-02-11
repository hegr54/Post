from django.db import models
from django.utils.encoding import smart_text
from django.utils import timezone
from .validators import validate_algo,validate_author_email
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
# Create your models here.


PUBLISH_CHOICES=(
('draft','Draft'),
('publish','Publish'),
('private','Private')
)
class post(models.Model):
    id          = models.BigAutoField(primary_key=True)
    active      = models.BooleanField(default=True)
    title       = models.CharField(max_length=250, verbose_name='post title')
    content     = models.TextField(null=True, blank=True)
    slug        = models.SlugField(null=True, blank=True)
    publish     = models.CharField(max_length=120,choices=PUBLISH_CHOICES, default="draft")
    view_count  = models.IntegerField(default=0)
    publish_date= models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email= models.EmailField(max_length=240 ,validators=[validate_author_email, validate_algo],  null=True, blank=True)


    #active=models.Booleanfield(null=true)
    #QUE ES SLUG? SLUGIFY
    #que son los signals en django? pre_save post_save
    #que es *args,**kwargs y super python?

    def __str__(self):
        return smart_text(self.content)

    def save(self, *args, **kwargs):
        print ('Guardar algo')
        if not self.slug:
            if self.title:
                self.slug=slugify(self.title)
        super(post,self).save(*args,**kwargs)

def post_model_post_seve_receiver(sender, instance, created, *args, **kwargs):
    print ("Despues de almacenar")
    if not instance.slug and instance.title:
        instance.slug=slugify(instance.title)
        instance.save()

post_save.connect(post_model_post_seve_receiver, sender=post)

def post_model_pre_save_receiver(sender,instance,*args,**kwargs):
    print('Antes de almacenar')
    if not instance.slug and instance.title:
        instance.slug=slugify(instance.title)
        instance.save()

pre_save.connect(post_model_pre_save_receiver, sender=post)
