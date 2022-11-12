from django.urls import  path
from inventory.views import *

urlpatterns = [
    #mark
    path("marka_ekle",newMark,name="mark_add"),
    path("mark_delete/<int:myid>/",markDelete,name="mark_delete"),
    #power
    path("guc_ekle",newPower,name="power_add"),
    path("power_delete/<int:myid>/",powerDelete,name="power_delete"),
    #power
    path("pompa_ekle",newPump,name="pump_add"),
    path("pump_delete/<int:myid>/",pumpDelete,name="pump_delete"),
    #engine
    path("motor_ekle",newEngine,name="engine_add"),
    path("engine_delete/<int:myid>/",engineDelete,name="engine_delete"),
    
    #İnvertory
    path("",invertory,name="invertory"),
    path("id",view_invertory_by_id,name="invertory_id"),
    path("update",updateİnvertory,name="updateİnvertory"),
    path("delete",deleteİnvertory,name="deleteİnvertory"),
   
    #TwondStore
    path("2._el_depo",twondstore,name="twondstore"),
    path("2._el_motor",twondEngine,name="twondEngine"),
    path("2._el_motor_id",view_twondEngine_by_id,name="twondEngine_id"),
    path("2._el_motor/update",updateTwondEngine,name="updateTwondEngine"),
    path("2._el_motor/delete",deleteTwondEngine,name="deleteTwondEngine"),
    path("2._el_pompa",twondPump,name="twondPump"),
    path("2._el_pompa_id",view_twondPump_by_id,name="twondPump_id"),
    path("2._el_pompa/update",updateTwondPump,name="updateTwondPump"),
    path("2._el_pompa/delete",deleteTwondPump,name="deleteTwondPump"),
    # Repair Store
    path("tamir_depo",repairstore,name="repairstore"),
    path("tamir_motor",repairEngine,name="repairEngine"),
    path("tamir_motor_id",view_repair_by_id,name="repairEngine_id"),
    path("tamir_motor/update",updateRepairEngine,name="updateRepairEngine"),
    path("tamir_motor/delete",deleteRepairEngine,name="deleteRepairEngine"),
    
    #Zero Store
    path("depo",store,name="store"),
    path("sifir_motor",zeroEngine,name="zeroEngine"),
    path("sifir_motor_id",view_zeroEngine_by_id,name="zeroEngine_id"),
    path("sifir_motor/update",updateZeroEngine,name="updateZeroEngine"),
    path("sifir_motor/delete",deleteZeroEngine,name="deleteZeroEngine"),
    path("sifir_pompa",zeroPump,name="zeroPump"),
    path("sifir_pompa_id",view_zeroPump_by_id,name="zeroPump_id"),
    path("sifir_pompa/update",updateZeroPump,name="updateZeroPump"),
    path("sifir_pompa/delete",deleteZeroPump,name="deleteZeroPump"),
    path("sifir_diğer_malzeme",other,name="other"),
    path("sifir_diğer_malzeme_id",view_zeroOther_by_id,name="zeroOther_id"),
    path("sifir_diğer_malzeme/update",updateOther,name="updateOther"),
    path("sifir_diğer_malzeme/delete",deleteOther,name="deleteOther"),
     
]