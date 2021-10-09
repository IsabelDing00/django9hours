from django.db import models

# Create your models here.

class Account(models.Model):
    """
    Account Table
    """
    # in Django, id is default
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    register_date = models.DateTimeField(auto_now_add=True)
    signature = models.CharField("Sign your name",max_length=255, null=True,blank=True)

    def __str__(self):
        return self.username

class Article(models.Model):
    """
    Article Table
    """
    title = models.CharField(max_length=255, unique=True) # CharField has to put max_length, but textField doesn't need to
    content = models.TextField()
    account = models.ForeignKey("Account", on_delete=models.CASCADE)  # on_delete = CASCADE: if I delete a account in Account(), and the article this account write will be deleted
    # because account is a FK so in database it will be account_id automatically
    tags = models.ManyToManyField("Tag", null=True,blank=True)
    pub_date = models.DateField()
    # read_count = models.IntegerField()

    def get_tags(self):
        return ','.join([i.name for i in self.tags.all()])

    def __str__(self):
        return "%s - %s" % (self.title, self.account)

class Tag(models.Model):
    """
    Tag Table
    """
    name = models.CharField(max_length=64, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name