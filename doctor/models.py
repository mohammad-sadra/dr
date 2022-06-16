from django.db import models
from multiselectfield import MultiSelectField

MY_CHOICES = (('sh', 'شنبه'),
              ('1sh', 'یک شنبه'),
              ('2sh', 'دوشنبه'),
              ('3sh', 'سه شنبه'),
              ('4sh', 'چهارشنبه'),
              ('5sh', 'پنچ شنبه')
              )
MY_CHOICES_time = (
           ('14:00', '14:00'),
           ('14:15', '14:15'),
           ('14:30', '14:30'),
           ('14:45', '14:45'),
           ('15:00', '15:00'),
           ('15:15', '15:15'),
           ('15:30', '15:30'),
           ('15:45', '15:45'),
           ('16:00', '16:00'),
           ('16:15', '16:15'),
           ('16:30', '16:30'),
           ('16:45', '16:45'),
           ('17:00', '17:00'),
           ('17:15', '17:15'),
           ('17:30', '17:30'),
           ('17:45', '17:45'),
           ('18:00', '18:00'),
           ('18:15', '18:15'),
           ('18:30', '18:30'),
           ('18:45', '18:45'),
           ('19:00', '19:00'),
           ('19:15', '19:15'),
           ('19:30', '19:30'),
           ('19:45', '19:45')
)

type_pay = (
    ('pos', 'کارتخوان'),
    ('cash', 'نقدی'),
    ('int', 'اینترنتی'),

)


class doctor (models.Model):
    name = models.CharField('نام و نام خانوادگی', max_length=150)
    type = models.CharField('تخصص',max_length=200)
    day = MultiSelectField('روز های کاری', choices=MY_CHOICES, max_choices=3)

    class Meta:
        db_table = 'doctor'
        verbose_name = 'دکتر ها'
        verbose_name_plural = 'doctors'


class reserve (models.Model):
    name = models.CharField('نام بیمار', max_length=100)
    phone = models.BigIntegerField('شماره تلفن بیمار')
    doctor_reserve = models.ForeignKey('doctor',verbose_name='دکتر بیمار' ,on_delete=models.CASCADE ,default=1)
    reserve_date = models.DateField('تاریخ رزرو', auto_now=True)
    reserve_time = MultiSelectField('ساعت رزرو', choices=MY_CHOICES_time, max_choices=1)
    price = models.BigIntegerField('مبلغ پرداختی')
    pay = MultiSelectField('نوع پرداخت', choices=type_pay, max_choices=1, default=1)

    class Meta:
        db_table = 'reserve'
        verbose_name = 'رزرو ها'
        verbose_name_plural = 'reserves'




