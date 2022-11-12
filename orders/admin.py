from django.contrib import admin
from .models import *

class BlockWorkOrders(admin.ModelAdmin):
    search_fields = ("work_orders_number",
        "invertory",
    )
    list_filter = ("status",
        "create_at",
    )
    list_display = ("work_orders_number","invertory","job_done",
                    "status","comment","create_at","update_at")

class BlockAssembly_Orders(admin.ModelAdmin):
    search_fields = ("orders_number",
        "work_orders_number",
    )
   
    list_display = ("work_orders_number","orders_number","status",
                    "create_at","update_at")

class BlockDisAssembly_Orders(admin.ModelAdmin):
    search_fields = ("orders_number",
        "work_orders_number",
    )
   
    list_display = ("work_orders_number","orders_number",
                    "create_at","update_at")
    
admin.site.register(DisAssembly_Orders,BlockDisAssembly_Orders)
admin.site.register(Assembly_Orders,BlockAssembly_Orders)
admin.site.register(Work_Orders,BlockWorkOrders)
admin.site.register(Workshop_Orders)
admin.site.register(Repair_Orders)
