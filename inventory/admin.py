from django.contrib import admin
from .models import *

# Register your models here.
class Blockİnvertory(admin.ModelAdmin):
    search_fields = ("well_number","tank_info")
    list_filter = ("well_number","tank_info")
    list_display = ("well_number","contry","adress",
                "disassembly_depth",
                "mounting_depth",
                "tank_info",
                "pipe_type",
                "cable",    
                "create_at",
                "flow",
                "comment",
    )

class BlockEngine(admin.ModelAdmin):
    search_fields = ("engine_power",
        "engine_mark",
    )
    list_filter = ("engine_power",
        "engine_mark",
    )
    list_display = (
        "engine_type",
        "engine_power",
        "engine_mark",
        "comment",
    )
class BlockPump(admin.ModelAdmin):
    search_fields = ("pump_type",
        "number_stages",
)
    list_filter = ("pump_type",
        "number_stages",
        "pump_mark",
)
    list_display = (
        "pump_type",
        "number_stages",
        "pump_mark",
        "comment",
    )


admin.site.register(RepairStock)
admin.site.register(TwondPumpStock)
admin.site.register(TwondEngineStock)
admin.site.register(Power)
admin.site.register(ZeroEngineStock)
admin.site.register(ZeroOtherStock)
admin.site.register(ZeroPumpStock)
admin.site.register(Mark)
admin.site.register(Engine,BlockEngine)
admin.site.register(Pump,BlockPump)
admin.site.register(İnvertory,Blockİnvertory)