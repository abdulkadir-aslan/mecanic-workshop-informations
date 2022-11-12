from django import forms
from django.forms import ModelForm
from inventory.models import *
from orders.models import Assembly_Orders, DisAssembly_Orders, Repair_Orders, Work_Orders, Workshop_Orders

class WorkOrdersForm(ModelForm):
    class Meta:
        model = Work_Orders
        fields = ["comment",]
        
class WorkDisassemblyForm(ModelForm):
    class Meta:
        model = DisAssembly_Orders
        fields = ["orders_number","comment",]

class WorkshopForm(ModelForm):
    class Meta:
        model = Workshop_Orders
        fields = ["orders_number","comment",]

class ReapirForm(ModelForm):
    class Meta:
        model = İnvertory
        fields = ["engine","engine_serial_number"]

class AssemblyForm(ModelForm):
    class Meta:
        model = Assembly_Orders
        fields = ["orders_number","comment",]


class OrderİnvertoryForm(ModelForm):
    class Meta:
        model = İnvertory
        fields = ["disassembly_depth",
                "mounting_depth","tank_info",
                "pipe_type","cable",
                "engine","pump",
                "engine_serial_number","pump_serial_number",
                "flow"]
        widgets = {
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
        }
