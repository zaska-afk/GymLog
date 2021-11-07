from django.db import models
from django.contrib.auth.models import User
from app_authorization.models import Profile
# from mptt.models import MPTTModel, TreeForeignKey

class Gym(models.Model):
    gym_name = models.CharField(max_length=50)
    gym_rating = models.IntegerField()
    gym_bio = models.TextField(max_length=2000, default="Welcome")
    # gym_founder = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    created_on = models.DateField(auto_now_add=True)
    gym_url = models.URLField(max_length=200, blank=True)
    gym_members = models.ManyToManyField(Profile, blank=True)


# class Comment(MPTTModel):
#     comment_name = models.CharField(max_length=40)
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='chilren')

#     def __str__(self):
#         return self.name
    
#     class MPTTMeta:
#         order_insertion_by = ['name']

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    
    # post_photo = models.ImageField(
    #     ('post photo'),
    #     # MEDIA_ROOT/post_photos/ == website/static/uploads/post_photos/
    #     upload_to='post_photos/',
    #     null=True,
    #     blank=True,
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(
    Profile,
    verbose_name=('author'),
    related_name='posts_made',
    on_delete=models.CASCADE,
)
    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    
    commented_on =models.ForeignKey(Gym, related_name='comments', on_delete=models.CASCADE, blank=True)
    
    author = models.ForeignKey(Profile,
        related_name='comments_made',
        on_delete=models.CASCADE,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body