from unittest.mock import DEFAULT
from django.db import models
from inventory.models import İnvertory

STATUS = (
    ("1","DEMONTAJ BEKLİYOR"),
    ("2","ATÖLYEDE TAMİR BEKLİYOR"),
    ("3","TAMİR EDİLİYOR"),
    ("4","ATÖLYEDE MONTAJ BEKLİYOR"),
    ("5","MONTAJ BEKLİYOR"),
    ("6","KAPANDI"),
)

STATUS_OTHER = (
    ("passive","PASİF"),
    ("active","AKTİF"),
)
DEFAULT_STATUS_OTHER = "active"

class Work_Orders(models.Model):
    work_orders_number = models.PositiveIntegerField(verbose_name="Numara",unique=True,blank=False,null=False)
    invertory = models.ForeignKey(İnvertory,verbose_name="Kuyu Bilgisi",on_delete=models.PROTECT,null=True)
    status = models.CharField(verbose_name="Durum",null=False,choices=STATUS,max_length=17,blank=False)
    comment = models.TextField(verbose_name="Açıklama",blank=True)
    job_done = models.CharField(verbose_name="iş akışı",max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.work_orders_number)
    

class Assembly_Orders(models.Model):
    work_orders_number = models.ForeignKey(Work_Orders,verbose_name="İş Emri",on_delete=models.PROTECT,null=True)
    orders_number = models.PositiveIntegerField(verbose_name="Montaj numarası",unique=True,blank=False,null=True)
    status = models.CharField(max_length=7,choices=STATUS_OTHER,default=DEFAULT_STATUS_OTHER)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)

    def __str__(self):
        return str(self.orders_number)

class Workshop_Orders(models.Model):
    work_orders_number = models.ForeignKey(Work_Orders,verbose_name="İş Emri",on_delete=models.PROTECT,null=True)
    orders_number = models.PositiveIntegerField(verbose_name="Atölye İş Emri Numarası",unique=True,blank=False,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)
    def __str__(self):
        return str(self.orders_number)

class Repair_Orders(models.Model):
    work_orders_number = models.ForeignKey(Work_Orders,verbose_name="İş Emri",on_delete=models.PROTECT,null=True)
    repair_orders_number = models.PositiveIntegerField(verbose_name="Tamir numarası",unique=True,blank=False,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)

    def __str__(self):
        return str(self.repair_orders_number)
    
class DisAssembly_Orders(models.Model):
    work_orders_number = models.ForeignKey(Work_Orders,verbose_name="İş Emri",on_delete=models.PROTECT,null=True)
    orders_number = models.PositiveIntegerField(verbose_name="Demontaj numarası",unique=True,blank=False,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=7,choices=STATUS_OTHER,default=DEFAULT_STATUS_OTHER)
    update_at =models.DateTimeField(auto_now=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)

    def __str__(self):
        return str(self.orders_number)
    