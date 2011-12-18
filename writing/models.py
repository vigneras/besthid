from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save

TYPES = (
    (u'Text', u'Text'),
    (u'Code', u'Code'),
    (u'Calc', u'Calc'),
    (u'Markup', u'Markup'),
    )
