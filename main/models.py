from django.db import models


class Device(models.Model):

    name      = models.CharField(max_length=50, default='', verbose_name="نام دستگاه")
    app       = models.CharField(max_length=50, blank=True, verbose_name="اپ")
    details   = models.TextField(default='', verbose_name="توضیحات")
    price     = models.CharField(max_length=50, default=0, verbose_name="قیمت")
    count     = models.IntegerField(default=1, verbose_name="تعداد")

    class Meta:
        verbose_name_plural = 'دستگاه ها'

    def __str__(self):
        return self.name


class Client(models.Model):

    device = models.ForeignKey(Device,on_delete=models.SET_NULL, null=True, verbose_name="دستگاه")
    serial_no = models.CharField(max_length=50, default='', verbose_name="شماره سریال")
    terminal = models.CharField(max_length=50, default='', verbose_name="ترمینال")
    name = models.CharField(max_length=50,default='', verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=15, default='09', verbose_name="شماره همراه")
    melli_id = models.CharField(max_length=20,default='', verbose_name="کد ملی")
    shop = models.CharField(max_length=50,default='', verbose_name="فروشگاه")
    phone_stat = models.CharField(max_length=20, default='', verbose_name="تلفن")
    date = models.CharField(max_length=20,default='', verbose_name="تاریخ درخواست")


    class Meta:
        verbose_name_plural = 'مشتریان'


    def __str__(self):
        return self.name



class Costs(models.Model):
    amount = models.IntegerField(default=0, verbose_name="مبلغ")
    date = models.CharField(max_length=20, default='', verbose_name="تاریخ")
    detail = models.TextField(default='', verbose_name='توضیحات')

    class Meta:

        verbose_name_plural = "هزینه ها"

    def __str__(self):
        return '{} | {}'.format(self.amount,self.date)





class Payment(models.Model):

    client = models.ForeignKey(Client,on_delete=models.CASCADE,verbose_name="مشتری")
    amount = models.IntegerField(default=0, verbose_name="مبلغ")
    date = models.CharField(max_length=20, default='', verbose_name="تاریخ پرداخت")
    class Meta:
        verbose_name_plural = 'پرداختی ها'

    def __str__(self):
        return '{}  |  {}   |  {}'.format(self.client.name,self.client.device.name,
                                                self.amount)