from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ArticleItems(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='articles/', blank=True, null=True)
    text=models.TextField(blank=True, null=True)
    status=models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.article}-{self.text[:32]}"

class SocialMedia(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='social-media/', blank=True, null=True)
    url=models.URLField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




