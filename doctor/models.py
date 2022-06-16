from django.db import models
from multiselectfield import MultiSelectField

MY_CHOICES = (('sh', 'شنبه'),
              ('1sh', 'یک شنبه'),
              ('2sh', 'دوشنبه'),
              ('3sh', 'سه شنبه'),
              ('4sh', 'چهارشنبه'),
              ('5sh', 'پنچ شنبه')
              )


class doctors (models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=200)
    day = MultiSelectField(choices=MY_CHOICES, max_choices=3)

    class meta:
        db_table = 'doctors'
        varbose_name = \
            'دکتر ها'


class reserve (models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField(max_length=11)


