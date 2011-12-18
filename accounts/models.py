from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Run(models.Model):
    RUN_CAT = (
        (u'Writing', u'Writing'),
        (u'Reading', u'Reading'),
        (u'Pointing', u'Pointing')
        )
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=10, choices=RUN_CAT)
    # Type stores stuff like:
    # Text (novel, blog, tweet, litterature, ...)
    # Code (C, Ruby, HTML, XML, MediaWiki, ...)
    # Calc (CSV (space separated), calc/excel (tab separated), ...)
    # They are defined in subclasses
    type = models.CharField(max_length=10)
    result = models.IntegerField()
    user = models.ForeignKey(User)


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
