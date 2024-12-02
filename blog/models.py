from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    body = models.TextField()
    techspecific = models.BooleanField(default=False)
    # date_created = models.DateField(auto_now_add=True, default=datetime.now())
    # date_updated = models.DateField(auto_now=True)
    # age = models.DecimalField(max_digits=6, decimal_places=2)
    # email = models.EmailField()
    def __str__(self):
            return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])


