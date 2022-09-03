from django.db import models
from django.urls import reverse
import wikipedia


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return wikipedia.page(self.name).url


class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('storeapp:product_detail', args=[self.department.slug, self.slug])


class Order(models.Model):
    PURPOSE_CHOICES = (
        ('1', "for enquiry"),
        ('2', "place order"),
        ('3', "return"),
        ('4', "cancel"),
    )
    GENDER_CHOICES = (
        ("1", "MALE"),
        ("2", "FEMALE"),
        ("3", "TRANSGENDER"),
    )

    name = models.CharField(max_length=250)
    dob = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,

    )
    phone_number = models.CharField(max_length=12)
    mail_id = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    purpose = models.CharField(
        max_length=30,
        choices=PURPOSE_CHOICES,

    )
    materials_provided = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.name)
