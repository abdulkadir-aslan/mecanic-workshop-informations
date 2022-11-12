from django import forms
from django.forms import ModelForm
from .models import *

class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = ['engine_mark',]
        
        widgets = {
            'engine_mark': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marka'},)
        }
        
        
class PowerForm(ModelForm):
    class Meta:
        model = Power
        fields = ['engine_power',]
        widgets = {
            'engine_power': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Güç'},)
        }

class PumpForm(ModelForm):
    class Meta:
        model = Pump
        fields = ['pump_type','pump_breed',
                  'number_stages','pump_mark','comment']
        widgets = {
            'pump_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pompa Tipi'},),
            'pump_breed': forms.Select(attrs={'class': 'form-select'},),
            'number_stages': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Kademe Sayısı'},),
            'pump_mark': forms.Select(attrs={'class': 'form-select'},),
            'comment':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Açıklama','rows':'2'},)
        }
class EngineForm(ModelForm):
    class Meta:
        model = Engine
        fields = ['engine_type','engine_power',
                'engine_mark','comment']
        widgets = {
            'engine_type': forms.Select(attrs={'class': 'form-select'},),
            'engine_power': forms.Select(attrs={'class': 'form-select'},),
            'engine_mark': forms.Select(attrs={'class': 'form-select'},),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Açıklama','rows':'2'},)
        }
        
class İnvertoryForm(ModelForm):
    class Meta:
        model = İnvertory
        fields = ["well_number","contry","adress","disassembly_depth",
                "mounting_depth","tank_info",
                "pipe_type","cable",
                "engine","pump",
                "engine_serial_number","pump_serial_number",
                "flow","comment"]
        widgets = {
            "well_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'kuyu numarası'},),
            "contry": forms.Select(attrs={'class': 'form-select'},),
            "adress": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'adres'},),
            "disassembly_depth": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Demonj Derinliği'},),
            "mounting_depth": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Montaj Derinliği'},),
            "tank_info": forms.Select(attrs={'class': 'form-select'},),
            "pipe_type": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Boru Tipi'},),
            "cable": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kablo'},),
            "engine": forms.Select(attrs={'class': 'form-select'},),
            "pump": forms.Select(attrs={'class': 'form-select'},),
            "engine_serial_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Motor Seri Numarası'},),
            "pump_serial_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pompa SeriNumarası'},),
            "flow": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Debi'},),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Açıklama','rows':'2'},)
        }

#-------------------------Store-------------

class ZeroEngineForm(ModelForm):
    class Meta:
        model = ZeroEngineStock
        fields = ['engine','engine_serial_number',
            'quantity']
        widgets = {
            'engine': forms.Select(attrs={'class': 'form-select'},),
            'engine_serial_number':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seri Numarası'},),
            'quantity':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miktar'},),
        }

class ZeroPumpForm(ModelForm):
    class Meta:
        model = ZeroPumpStock
        fields = ['pump','pump_serial_number',
            'quantity']
        widgets = {
            'pump': forms.Select(attrs={'class': 'form-select'},),
            'pump_serial_number':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seri Numarası'},),
            'quantity':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miktar'},),
        }
    # def as_myp(self):
    #     "Returns this form rendered as HTML <p>s."
    #     return self._html_output(
    #         normal_row = '<div class="mb-3 col-md-4"> %(label)s %(field)s%(help_text)s </div>',
    #         error_row = '%s',
    #         row_ender = '</p>',
    #         help_text_html = ' <span class="helptext">%s</span>',
    #         errors_on_separate_row = True)

class ZeroOtherForm(ModelForm):
    class Meta:
        model = ZeroOtherStock
        fields = ['category','subcategory',
            'quantity']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kategori'},),
            'subcategory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alt Kategori'},),
            'quantity':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miktar'},),
        }
        
class TwondEngineForm(ModelForm):
    class Meta:
        model = TwondEngineStock
        fields = ['engine','engine_serial_number',
            'quantity']
        widgets = {
            'engine': forms.Select(attrs={'class': 'form-select'},),
            'engine_serial_number':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seri Numarası'},),
            'quantity':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miktar'},),
        }

class TwondPumpForm(ModelForm):
    class Meta:
        model = TwondPumpStock
        fields = ['pump','pump_serial_number',
            'quantity']
        widgets = {
            'pump': forms.Select(attrs={'class': 'form-select'},),
            'pump_serial_number':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seri Numarası'},),
            'quantity':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miktar'},),
        }
        
class RepairStockForm(ModelForm):
    class Meta:
        model = RepairStock
        fields = ['engine','engine_serial_number',
            'quantity']
        widgets = {
            'engine': forms.Select(attrs={'class': 'form-select'},),
            'engine_serial_number':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Seri Numarası'},),
            'quantity':  forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miktar'},),
        }