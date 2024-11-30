from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField # type: ignore
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=55)
    def __str__(self) -> str:
        return self.name


class Por(models.Model):
    handel = models.CharField(max_length=20, null=True)
    body = RichTextField(max_length=600, null=True)
    create = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    active = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag, null=True) # 
    img= models.ImageField(null=True)
    slug = models.SlugField( null=True, blank=True)
    def __str__(self) -> str:
        return self.handel
    
    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.handel)

            has_slug = Por.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.handel) + '-' + str(count) 
                has_slug = Por.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
    
    # def save (self, *args, **kwargs):
    #     if self.slug == None:
    #         slug = slugify(self.handel)
    #         foundSlug = Por.objects.filter(slug=slug).exists()
    #         cont = 1
    #         while foundSlug :
    #             cont += 1
    #             slug +=slugify(self.handel) + '_'+ str(cont)
    #             foundSlug = Por.objects.filter(slug=slug).exists()
    #         self.slug = slug
    #     super().save(*args, **kwargs)
    

class Test(models.Model):
    name = models.CharField(max_length=20, null=True)
    age = models.IntegerField(max_length=20, null=True)
    tex = models.TextField(max_length=500, null=True)
    imgg =models.ImageField(null=True)
    def __str__(self) -> str:
        return self.name