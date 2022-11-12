from multiprocessing.spawn import import_main_path
from django.urls import path
from .views import *

urlpatterns = [
    path('yeni_iş_emri', workOrdersİnv, name="workOrdersİnv"),
    path("tüm_is_emirleri",all_work_orders,name="all_work_orders"),
    path("bekleyen_isler",work_orders,name="work_orders"),
    path("id",work_orders_id,name="work_orders_id"),
    path("update",updateWork_orders,name="updateWork_orders"),
    path("delete",deleteWork_orders,name="deleteWork_orders"),
    #Disassembly
    path('tüm_demontaj_emirleri', disassemblyAll, name="disassemblyAll"),
    path("demontaj",disassembly,name="disassembly"),
    path("demontaj/id",view_dissembly_by_id,name="disassembly_id"),
    path("demontaj/update/<int:id>/",updateDisassembly,name="updateDisassembly"),
    path("demontaj/delete",deleteDisassembly,name="deleteDisassembly"),
    #repair
    path("tamir_iş_emirleri",repair_orders,name="repair_orders"),
    path("tüm_tamir",repairAll,name="repairAll"),
    path("tamir",repair,name="repair"),
    path("tamir/id",view_repair_by_id,name="repair_id"),
    path("tamir/update",updaterepair,name="updaterepair"),
    path("tamir/delete",deleteRepair,name="deleteRepair"),
    #workshop
    path("tüm_atölye",workshopyAll,name="workshopyAll"),
    path("atölye",workshop,name="workshop"),
    path("atölye/tamirden_geldi",repair_come,name="repair_come"),
    path("atölye/id",view_workshop_by_id,name="workshop_id"),
    path("atölye/update/<int:id>/",updateworkshop,name="updateworkshop"),
    path("atölye/delete",deleteWorkshop,name="deleteWorkshop"),
   #Assembly
    path("tüm_montaj",assemblyAll,name="assemblyAll"),
    path("montaj",assembly,name="assembly"),
    path("montaj/id",view_assembly_by_id,name="assembly_id"),
    path("montaj/update/<int:id>/",updateassembly,name="updateassembly"),
    path("montaj/delete",deleteAssembly,name="deleteAssembly"),

]

