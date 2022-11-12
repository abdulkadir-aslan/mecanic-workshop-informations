from django.db import models


CONTRY = (
    ('akçakale','AKÇAKALE'),
    ('eyyübiye','EYYÜBİYE'),
    ('birecik','BİRECİK'),
    ('bozova','BOZOVA'),
    ('ceylanpınar','CEYLANPINAR'),
    ('halfeti','HALFETİ'),
    ('haliliye','HALİLİYE'),
    ('harran','HARRAN'),
    ('hilvan','HİLVAN'),
    ('karaköprü','KARAKÖPRÜ'),
    ('siverek','SİVEREK'),
    ('suruç','SURUÇ'),
    ('viranşehir','VİRANŞEHİR'),
)

Tank = (
    ("1","TANK"),
    ("2","ŞEBEKE"),
    ("3","HAVUZ"),
    ("4","DEPO"),
    ("5","BOŞTA"),
    ("6","AYAKLI DEPO"),
)

ENGİNE_TYPE = (
    ("1",'3"'),
    ("2",'4"'),
    ("3",'5"'),
    ("4",'6"'),
    ("5",'7"'),
    ("6",'8"'),
    ("7",'9"'),
    ("8",'10"'),
    ("9",'11"'),
)
BREED = (
    ("1","KROM"),
    ("2","NORİL"),
    ("3","DÖKÜM"),
)

class Mark(models.Model):
    engine_mark = models.CharField(verbose_name="Marka",unique=True,max_length=50,null=False,blank=False)
    def __str__(self):
        return self.engine_mark
    
class Power(models.Model):
    engine_power = models.FloatField(verbose_name="Motor Gücü",unique=True,null=False,blank=False)
    def __str__(self):
        return str(self.engine_power)
    
class Engine(models.Model):
    engine_type = models.CharField(verbose_name="Motor Tipi",choices=ENGİNE_TYPE,max_length=4,null=False,blank=False)
    engine_power = models.ForeignKey(Power,verbose_name="Motor Gücü",on_delete=models.PROTECT,null=True)
    engine_mark = models.ForeignKey(Mark,verbose_name="Marka",on_delete=models.PROTECT,null=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)
    
    def __str__(self):
        return str(self.engine_power) +'HP - '+ str(self.engine_mark) 
    
    class Meta:
        ordering = ("engine_power__engine_power",)
        
class Pump(models.Model):
    pump_type = models.CharField(verbose_name="Tipi",max_length=25,null=False,blank=False)
    pump_breed = models.CharField(verbose_name="Cinsi",choices=BREED,max_length=5,null=False,blank=False)
    number_stages = models.PositiveIntegerField(verbose_name="Kademe Sayısı",default=0,null=False,blank=False)
    pump_mark = models.ForeignKey(Mark,verbose_name="Pompa Markası",on_delete=models.PROTECT,null=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)
    
    def __str__(self):
        return self.pump_type +"-"+ str(self.number_stages)
    
    class Meta:
        ordering = ("pump_type",)
    

class İnvertory(models.Model):
    well_number = models.CharField(verbose_name="Kuyu Numarası",max_length=100,unique=True,null=True,blank=False)
    contry = models.CharField(verbose_name="iLÇE",null=False,choices=CONTRY,max_length=11,blank=False)
    adress = models.CharField(verbose_name="Adres",max_length=50,null=False,blank=False)
    disassembly_depth = models.PositiveIntegerField(verbose_name="Demontaj Derinliği",blank=False,null=False)
    mounting_depth = models.PositiveIntegerField(verbose_name="Montaj Derinliği",blank=False,null=False)
    tank_info = models.CharField(verbose_name="Depo Bilgisi",choices=Tank,max_length=11,null=False,blank=False)
    pipe_type = models.CharField(verbose_name="Boru Tipi",max_length=50,null=False,blank=False)
    cable = models.CharField(verbose_name="Kablo",max_length=15,null=False,blank=False)
    engine = models.ForeignKey(Engine,verbose_name="Motor",on_delete=models.PROTECT,null=True)
    pump = models.ForeignKey(Pump,verbose_name="Pompa",on_delete=models.PROTECT,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now=True)
    engine_serial_number = models.CharField(verbose_name="Motor Seri Numarası",max_length=50,null=False,blank=True)
    pump_serial_number = models.CharField(verbose_name="Pompa SeriNumarası",max_length=50,null=False,blank=True)
    flow = models.CharField(verbose_name="Debi",max_length=50,null=False,blank=True)
    comment = models.TextField(verbose_name="Açıklama",blank=True)
    
    def save(self, *args, **kwargs):
        self.adress = self.adress.upper() 
        return super(İnvertory, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.well_number)
    
    class Meta:
        ordering = ("well_number",)

# from .models import İnvertory   
class ZeroEngineStock(models.Model):
    engine = models.ForeignKey(Engine,verbose_name="Motor",on_delete=models.PROTECT,null=True)
    engine_serial_number = models.CharField(verbose_name="Motor Seri Numarası",max_length=50,null=False,blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Miktar",default=0,blank=False,null=False)
    stock = models.PositiveIntegerField(verbose_name="Stok",default=0,blank=True,null=False)
    
    def __str__(self):
        return str(self.engine)
    
    def save(self, *args, **kwargs):
        # stocks = İnvertory.objects.filter(engine=self.engine)
        # if len(stocks) > 0 :
        #     aa = sum([item.mounting_depth for item in stocks])
        #     if (self.quantity - aa) > 0 :
        #         self.stock = (self.quantity - aa)
        #     else:
        #         self.stock = 0
        # else:
        self.stock = self.quantity 
        return super(ZeroEngineStock, self).save(*args, **kwargs)

class ZeroPumpStock(models.Model):
    pump = models.ForeignKey(Pump,verbose_name="Pompa",on_delete=models.PROTECT,null=True)
    pump_serial_number = models.CharField(verbose_name="Pompa Seri Numarası",max_length=50,null=False,blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Miktar",default=0,blank=False,null=False)
    stock = models.PositiveIntegerField(verbose_name="Stok",default=0,blank=True,null=False)
            
    def __str__(self):
        return str(self.pump)
    
    def save(self, *args, **kwargs):
        # stocks = İnvertory.objects.filter(pump=self.pump)
        # if len(stocks) > 0 :
        #     aa = sum([item.mounting_depth for item in stocks])
        #     if (self.quantity - aa) > 0 :
        #         self.stock = (self.quantity - aa)
        #     else:
        #         self.stock = 0
        # else:
        self.stock = self.quantity 
        return super(ZeroPumpStock, self).save(*args, **kwargs)
    

class ZeroOtherStock(models.Model):
    category = models.CharField(verbose_name="Kategori",max_length=50,null=False,blank=False)
    subcategory = models.CharField(verbose_name="Alt Kategori",max_length=50,null=False,blank=False)
    quantity = models.PositiveIntegerField(verbose_name="Miktar",default=0,blank=False,null=False)
    stock = models.PositiveIntegerField(verbose_name="Stok",default=0,blank=True,null=False)
    
    def __str__(self):
        return self.category +" "+ self.subcategory
    
    def save(self, *args, **kwargs):
        # stocks = İnvertory.objects.filter(engine=self.engine)
        # if len(stocks) > 0 :
        #     aa = sum([item.mounting_depth for item in stocks])
        #     if (self.quantity - aa) > 0 :
        #         self.stock = (self.quantity - aa)
        #     else:
        #         self.stock = 0
        # else:
        self.stock = self.quantity 
        return super(ZeroOtherStock, self).save(*args, **kwargs)
 
class TwondEngineStock(models.Model):
    engine = models.ForeignKey(Engine,verbose_name="Motor",on_delete=models.PROTECT,null=True)
    engine_serial_number = models.CharField(verbose_name="Motor Seri Numarası",max_length=50,null=False,blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Miktar",blank=False,null=False)
    stock = models.PositiveIntegerField(verbose_name="Stok",default=0,blank=True,null=False)
    
    def __str__(self):
        return str(self.engine)
    def save(self, *args, **kwargs):
        self.stock = self.quantity 
        return super(TwondEngineStock, self).save(*args, **kwargs)

class TwondPumpStock(models.Model):
    pump = models.ForeignKey(Pump,verbose_name="Pompa",on_delete=models.PROTECT,null=True)
    pump_serial_number = models.CharField(verbose_name="Pompa Seri Numarası",max_length=50,null=False,blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Miktar",blank=False,null=False)
    stock = models.PositiveIntegerField(verbose_name="Stok",default=0,blank=True,null=False)
    
    def __str__(self):
        return str(self.pump)
    def save(self, *args, **kwargs):
        self.stock = self.quantity 
        return super(TwondPumpStock, self).save(*args, **kwargs)
 
class RepairStock(models.Model):
    engine = models.ForeignKey(Engine,verbose_name="Motor",on_delete=models.PROTECT,null=True)
    engine_serial_number = models.CharField(verbose_name="Motor Seri Numarası",max_length=50,null=False,blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Miktar",blank=False,null=False)
    stock = models.PositiveIntegerField(verbose_name="Stok",default=0,blank=True,null=False)
    
    def __str__(self):
        return str(self.engine)
    def save(self, *args, **kwargs):
        self.stock = self.quantity 
        return super(RepairStock, self).save(*args, **kwargs)
