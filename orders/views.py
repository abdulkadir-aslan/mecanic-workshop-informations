from django.shortcuts import render,redirect,get_object_or_404,reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.models import Engine, Pump,İnvertory
from .forms import *
from django.http import JsonResponse, HttpResponse


#Work Orders
def all_work_orders(request):
    context ={
        "items":Work_Orders.objects.all().order_by("-id"),
    }
    return render(request,"orders/all_work_orders.html",context)

def workOrdersİnv(request):
    pos_id = request.GET.get('kuyu_numarasi', None)
    well_informations = İnvertory.objects.filter(well_number=pos_id)
    context = {}
    if not well_informations.exists():
        messages.add_message(
                            request,messages.WARNING,
                            'Kuyu numarası mevcut değil.')
        context['code'] = 404
    else:
        context['code'] = 202
        pos = well_informations[0]
        order = Work_Orders.objects.all().order_by("-id")
        context['order_number'] = order[0].work_orders_number + 1
        context['well_number'] = str(pos.well_number)
        context['contry'] = str(pos.get_contry_display())
        context['adress'] = str(pos.adress)
        context['disassembly_depth'] = str(pos.disassembly_depth)
        context['mounting_depth'] = str(pos.mounting_depth)
        context['tank_info'] = str(pos.get_tank_info_display())
        context['pipe_type'] = str(pos.pipe_type)
        context['cable'] = str(pos.cable)
        context['engine'] = str(pos.engine)
        context['pump'] = str(pos.pump)
        context['create_at'] = str(pos.create_at)
        context['engine_serial_number'] = str(pos.engine_serial_number)
        context['pump_serial_number'] = str(pos.pump_serial_number)
        context['flow'] = str(pos.flow)
        context['comment'] = str(pos.comment)
        context['id'] = pos.id  
    return JsonResponse(context)

def work_orders(request):
    item = Work_Orders.objects.all().order_by("-id")
    context ={
        "items":item.exclude(status=6)
    }
    if request.method == 'POST':
        try:
            a = Work_Orders.objects.exclude(status=6).get(invertory=request.POST["invertoryid"])
            messages.add_message(
                            request,messages.INFO,
                            f'*{a.invertory}* Kuyu numarası için Kapanmayan bir İş Emri mevcut.\n Mevcut iş Emri Üzerinde İşlem Yapabilirsiniz...')
            return redirect(work_orders)
        except:
            orders = Work_Orders(
            work_orders_number = item[0].work_orders_number + 1,
            invertory =İnvertory.objects.get(id = request.POST["invertoryid"]) ,
            status  = 1,
            job_done  = "İŞ EMRİ OLUŞTURULDU"
            )
            orders.save()
            if "save" in request.POST:
                orders.job_done += ",DEMONTAJ EMRİ OLUŞTURULDU"
                dorders=DisAssembly_Orders(
                    work_orders_number =orders,
                    orders_number = None
                )
                dorders.save()
                messages.add_message(
                            request,messages.SUCCESS,
                            'İş Emri Oluşturuldu, Demontaj Emri Verildi.')
            elif "assembly" in request.POST:
                orders.job_done += ",MONTAJ EMRİ OLUŞTURULDU"
                orders.status = 5
                morders=Assembly_Orders(
                    work_orders_number =orders,
                    orders_number = None
                )
                morders.save()
                messages.add_message(
                            request,messages.SUCCESS,
                            'İş Emri Oluşturuldu, Montaj Emri Verildi.')
            else:
                orders.job_done += ",YERİNDE DEMONTAJ MONTAJ EMRİ VERİLDİ"
                dorders=DisAssembly_Orders(
                    work_orders_number =orders,
                    orders_number = None
                )
                dorders.save()
                morders=Assembly_Orders(
                    work_orders_number =orders,
                    orders_number = None
                )
                morders.save()
                messages.add_message(
                            request,messages.SUCCESS,
                            'İş Emri Oluşturuldu, Yerinde Demontaj Montaj Emri Verildi.')
            orders.save()
            return redirect(work_orders)
    return render(request,"orders/work_orders.html",context)

def work_orders_id(request):
    pos_id = request.GET.get('id', None)
    pos = Work_Orders.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        messages.add_message(
                            request,messages.WARNING,
                            'Kuyu numarası mevcut değil.')
        context['code'] = 404
    else:
        context['code'] = 202
        pos = pos[0]
        context['order_number'] ="E" + str(pos.work_orders_number)
        context['well_number'] = str(pos.invertory)
        context['contry'] = str(pos.invertory.get_contry_display())
        context['adress'] = str(pos.invertory.adress)
        context['comment'] = str(pos.comment)
        context['fullname'] = "*"+str(pos.invertory.get_contry_display())+" "+str(pos.invertory.adress)+" "+str(pos.invertory)+"*<br> E" + str(pos.work_orders_number)
    return JsonResponse(context)

def updateWork_orders(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = Work_Orders.objects.get(id=request.POST.get('id'))
        pos = WorkOrdersForm(request.POST or None, instance=instance)
        pos.save()
        if "save" in request.POST:
            messages.success(request, "İş Emri Güncellendi")
        else:
            instance.status = 6
            instance.job_done += ",İŞ EMRİ KAPANDI"
            instance.save()
            messages.success(request, "İş Emri Kapandı.")
    except:
        messages.error(request, "Form Hatalı")
    return redirect(reverse('work_orders'))

def deleteWork_orders(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = Work_Orders.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "İş Emri Kaydı Silindi")
    except:
        messages.add_message(
                            request,messages.INFO, "Bu Kayıt Başka Tabloda Kullanılmakta")
    return redirect(reverse('work_orders'))

#Disassembly Orders
def disassemblyAll(request):
    orders = DisAssembly_Orders.objects.all().order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/disassembly/disassemblyAll.html", context)

def view_dissembly_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = DisAssembly_Orders.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['order_number'] ="E" + str(pos.work_orders_number)
        if pos.disassembly_orders_number is None:
            pass
        else:
            context['disassembly_orders_number'] =str(pos.disassembly_orders_number)
        context['well_number'] = str(pos.work_orders_number.invertory)
        context['contry'] = str(pos.work_orders_number.invertory.get_contry_display())
        context['adress'] = str(pos.work_orders_number.invertory.adress)
        context['comment'] = str(pos.comment)
    return JsonResponse(context)

def disassembly(request):
    orders = DisAssembly_Orders.objects.all().exclude(status=6).filter(status="active").order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/disassembly/disassembly_work_orders.html", context)

def updateDisassembly(request,id):
    instance = DisAssembly_Orders.objects.get(id=id)
    order = Work_Orders.objects.get(id=instance.work_orders_number.id)
    invertory = İnvertory.objects.get(id=instance.work_orders_number.invertory.id)
    form = OrderİnvertoryForm(request.POST or None, instance=invertory)
    form2 = WorkDisassemblyForm(request.POST or None, instance=instance)
    context = {
        "items" :instance,
        "form2":form2,
        "form" :form,
        "work_name":"Demontaj"
    }
    if request.method == "POST":
        if form2.is_valid():
            form2.save()
        else:
            messages.warning(request, form2.errors.as_ul())
            return render(request, "orders/update_order.html",context)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, form.errors.as_ul())
        
        if "close_and_new" in request.POST:
            order.job_done += f",DEMONTAJ(D{instance.orders_number}) EMRİ KAPANDI,YENİ DEMONTAJ EMRİ OLUŞTURULDU."
            instance.status = "passive"
            dorders=DisAssembly_Orders(
                    work_orders_number =instance.work_orders_number,
                    orders_number = None
                )
            dorders.save()
            messages.success(request, "İş Emri Kapandı;Yeni İş Emri Açıldı.")
        elif "close" in request.POST:
            instance.status = "passive"
            order.status = "6"
            order.job_done += ",DEMONTAJ EMRİ KAPANDI,İŞ EMRİ KAPANDI"
            messages.success(request, "İş Emri Kapandı,Demontaj İş Emri Kapandı")
        elif "workshop" in request.POST:
            instance.status = "passive"
            order.status = "2"
            order.job_done += ",DEMONTAJ YAPILDI,ATÖLYE'YE GELDİ"
            worders = Workshop_Orders(
                work_orders_number =instance.work_orders_number
            )
            try:
                workshop_number = Workshop_Orders.objects.all().order_by("-id")[0]
                worders.orders_number = workshop_number.orders_number + 1
            except (IndexError,TypeError):
                worders.orders_number = None
            worders.save()
            messages.add_message(
                                request,messages.SUCCESS,
                                f'İş Emri kaydı güncellendi.Atölye"ye gönderildi')

        else:
            messages.success(request, "Demontaj İş Emri Güncellendi")
        order.save()
        instance.save()
        return redirect ('disassembly')

    return render(request, "orders/update_order.html",context)


# def updateDisassembly(request):
#     if request.method != 'POST':
#         messages.error(request, "Access Denied")
#     try:
#         instance = DisAssembly_Orders.objects.get(id=request.POST.get('id'))
#         order = Work_Orders.objects.get(id=instance.work_orders_number.id)
#         pos = WorkDisassemblyForm(request.POST or None, instance=instance)
#         pos.save()
#         if "neworder" in request.POST:
#             order.job_done += f",DEMONTAJ(D{instance.disassembly_orders_number}) EMRİ KAPANDI,YENİ DEMONTAJ EMRİ OLUŞTURULDU."
#             dorders=DisAssembly_Orders(
#                     work_orders_number =instance.work_orders_number,
#                     disassembly_orders_number = None
#                 )
#             dorders.save()
#             messages.success(request, "İş Emri Kapandı;Yeni İş Emri Açıldı.")
#         elif "close" in request.POST:
#             order.status = "6"
#             order.job_done += ",DEMONTAJ EMRİ KAPANDI,İŞ EMRİ KAPANDI"
#             messages.success(request, "İş Emri Kapandı,Demontaj İş Emri Kapandı")
#         elif "workshop" in request.POST:
#             order.status = "2"
#             order.job_done += ",DEMONTAJ YAPILDI,ATÖLYE'YE GELDİ"
#             worders = Workshop_Orders(
#                 work_orders_number =instance.work_orders_number
#             )
#             try:
#                 workshop_number = Workshop_Orders.objects.all().order_by("-id")[0]
#                 worders.workshop_orders_number = workshop_number.workshop_orders_number + 1
#             except (IndexError,TypeError):
#                 worders.workshop_orders_number = None
#             worders.save()
#             messages.add_message(
#                                 request,messages.SUCCESS,
#                                 f'İş Emri kaydı güncellendi.Atölye"ye gönderildi')

#         else:
#             messages.success(request, "Demontaj İş Emri Güncellendi")
#         order.save()
#         instance.save()

#     except:
#         messages.warning(request, "İş Emri Daha Önce Kullanılmış")

#     return redirect(reverse('disassembly'))

def deleteDisassembly(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = DisAssembly_Orders.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Demontaj İş Emri Silindi.")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta.")

    return redirect(reverse('disassembly'))

#Workshop
def workshopyAll(request):
    orders = Workshop_Orders.objects.all().order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/workshop/workshopAll.html", context)

def view_workshop_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = Workshop_Orders.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['order_number'] ="E" + str(pos.work_orders_number)
        if pos.workshop_orders_number is None:
            pass
        else:
            context['workshop_orders_number'] =str(pos.workshop_orders_number)
        context['well_number'] = str(pos.work_orders_number.invertory)
        context['contry'] = str(pos.work_orders_number.invertory.get_contry_display())
        context['adress'] = str(pos.work_orders_number.invertory.adress)
        context['status'] = pos.work_orders_number.status
    return JsonResponse(context)

def workshop(request):
    orders = Workshop_Orders.objects.all().filter(work_orders_number__status=2).order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/workshop/workshop.html", context)

def updateworkshop(request,id):
    instance = Workshop_Orders.objects.get(id=id)
    order = Work_Orders.objects.get(id=instance.work_orders_number.id)
    invertory = İnvertory.objects.get(id=instance.work_orders_number.invertory.id)
    form = OrderİnvertoryForm(request.POST or None, instance=invertory)
    form2 = WorkshopForm(request.POST or None, instance=instance)
    context = {
        "items" :instance,
        "form2":form2,
        "form" :form,
        "work_name":"Atölye"
    }
    if request.method == "POST":
        if form2.is_valid():
            form2.save()
        else:
            messages.warning(request, form2.errors.as_ul())
            return render(request, "orders/update_order.html",context)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, form.errors.as_ul())
        if "repair" in request.POST:
           order.status = "3"
           order.job_done += ",TAMİRE GÖNDERİLDİ"
           rorder = Repair_Orders(
               work_orders_number = order,
               repair_orders_number=instance.orders_number
           )
           rorder.save()
           messages.success(request, "Tamir Emri Verildi.")
        elif "assembly" in request.POST:
           order.status = "5"
           order.job_done += ",MONTAJ EMRİ VERİLDİ"
           aorder = Assembly_Orders(
               work_orders_number = order,
               orders_number=None
           )
           aorder.save()
           messages.success(request, "Montaj Emri Verildi.")
       
        elif "close" in request.POST:
            order.status = "6"
            order.job_done += ",ATÖLYE EMRİ KAPANDI,İŞ EMRİ KAPANDI"
            messages.success(request, "İş Emri Kapandı,Atölye İş Emri Kapandı")
        else:
            messages.success(request, "İş Emri Güncellendi")
        order.save()
        instance.save()
        if order.status == "6" or order.status == "4":
            return redirect ('repair_come')
        else:
            return redirect ('workshop')

    return render(request, "orders/update_order.html",context)

# def updateworkshop(request):
#     if request.method != 'POST':
#         messages.error(request, "Access Denied")
#     try:
#         instance = Workshop_Orders.objects.get(id=request.POST.get('id'))
#         order = Work_Orders.objects.get(id=instance.work_orders_number.id)
#         pos = WorkshopForm(request.POST or None, instance=instance)
#         pos.save()
#         if "repair" in request.POST:
#            order.status = "3"
#            order.job_done += ",TAMİRE GÖNDERİLDİ"
#            rorder = Repair_Orders(
#                work_orders_number = order,
#                repair_orders_number=instance.workshop_orders_number
#            )
#            rorder.save()
#            messages.success(request, "Tamir Emri Verildi.")
#         elif "assembly" in request.POST:
#            order.status = "5"
#            order.job_done += ",MONTAJ EMRİ VERİLDİ"
#            aorder = Assembly_Orders(
#                work_orders_number = order,
#                assembly_orders_number=None
#            )
#            aorder.save()
#            messages.success(request, "Montaj Emri Verildi.")
#         else:
#             messages.success(request, "Demontaj İş Emri Güncellendi")
#         order.save()
#         instance.save()

#     except:
#         messages.warning(request, "İş Emri Daha Önce Kullanılmış")

#     return redirect(reverse('workshop'))

def deleteWorkshop(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = Workshop_Orders.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Atölye İş Emri Silindi.")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta.")

    return redirect(reverse('workshop'))

#repair_come
def repair_come(request):
    orders = Workshop_Orders.objects.all().filter(work_orders_number__status=4).order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/workshop/workshop.html", context)

#Repair
@login_required(login_url="login")
def repair_orders(request):
    context ={
        "items":Repair_Orders.objects.all().filter(work_orders_number__status=3).order_by("-id"),
    }
    return render(request,"orders/repair/repair_orders.html",context)

def repairAll(request):
    orders = Repair_Orders.objects.all().order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/repair/repairAll.html", context)

def view_repair_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = Repair_Orders.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['repair_orders_number'] =str(pos.repair_orders_number)
        context['order_number'] ="E" + str(pos.work_orders_number)
        context['repair_orders_number'] =str(pos.repair_orders_number)
        context['well_number'] = str(pos.work_orders_number.invertory.well_number)
        context['contry'] = str(pos.work_orders_number.invertory.get_contry_display())
        context['adress'] = str(pos.work_orders_number.invertory.adress)
        context['disassembly_depth'] = str(pos.work_orders_number.invertory.disassembly_depth)
        context['mounting_depth'] = str(pos.work_orders_number.invertory.mounting_depth)
        context['tank_info'] = str(pos.work_orders_number.invertory.get_tank_info_display())
        context['pipe_type'] = str(pos.work_orders_number.invertory.pipe_type)
        context['cable'] = str(pos.work_orders_number.invertory.cable)
        context['engine'] = str(pos.work_orders_number.invertory.engine)
        context['engine_id'] = str(pos.work_orders_number.invertory.engine.id)
        context['pump'] = str(pos.work_orders_number.invertory.pump)
        context['create_at'] = str(pos.create_at)
        context['comment'] = str(pos.comment)
        context['engine_serial_number'] = str(pos.work_orders_number.invertory.engine_serial_number)
        context['pump_serial_number'] = str(pos.work_orders_number.invertory.pump_serial_number)
        context['flow'] = str(pos.work_orders_number.invertory.flow)
    return JsonResponse(context)

def repair(request):
    orders = Repair_Orders.objects.all().filter(work_orders_number__status=3).order_by("-id")
    context = {
        'items': orders,
        'engine': RepairStock.objects.all().filter(stock__gte=1)
    }
    return render(request, "orders/repair/repair.html", context)

def updaterepair(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = Repair_Orders.objects.get(id=request.POST.get('id'))
        instance.comment = request.POST["comment"]
        order = Work_Orders.objects.get(id=instance.work_orders_number.id)
        inventory = İnvertory.objects.get(id = order.invertory.id)
        form = ReapirForm(request.POST or None, instance=inventory)
        if order.status == "3":
            order.status = "4"
            order.job_done += ",TAMİRDEN GELDİ"
        if form.has_changed():
            instance.comment += "\n "+str(inventory.engine) + " / "+str(inventory.engine_serial_number)+ "  Motor Tamir Deposundan Değiştirildi."
            form.save()
            
        instance.save()
        order.save()
        messages.add_message(
                                request,messages.SUCCESS,
                                f'İş Emri kaydı güncellendi.Atölyeye gönderildi')
    except:
        messages.warning(request, "İş Emri Daha Önce Kullanılmış")

    return redirect(reverse('repair'))

def deleteRepair(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = Repair_Orders.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Tamir İş Emri Silindi.")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta.")

    return redirect(reverse('repair'))

#Assembly
def assemblyAll(request):
    orders = Assembly_Orders.objects.all().order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/assembly/assemblyAll.html", context)

def view_assembly_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = Assembly_Orders.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['orders_number'] =str(pos.orders_number)
    return JsonResponse(context)

def assembly(request):
    orders = Assembly_Orders.objects.all().exclude(work_orders_number__status=6).filter(status = "active").order_by("-id")
    context = {
        'items': orders
    }
    return render(request, "orders/assembly/assembly.html", context)

def updateassembly(request,id):
    instance = Assembly_Orders.objects.get(id=id)
    order = Work_Orders.objects.get(id=instance.work_orders_number.id)
    invertory = İnvertory.objects.get(id=instance.work_orders_number.invertory.id)
    form = OrderİnvertoryForm(request.POST or None, instance=invertory)
    form2 = WorkshopForm(request.POST or None, instance=instance)
    context = {
        "items" :instance,
        "form2":form2,
        "form" :form,
        "work_name":"Montaj"
    }
    if request.method == "POST":
        if form2.is_valid():
            form2.save()
        else:
            messages.warning(request, form2.errors.as_ul())
            return render(request, "orders/update_order.html",context)
        if form.is_valid():
            form.save()
        else:
            messages.warning(request, form.errors.as_ul())
        if "newassembly" in request.POST:
            order.job_done += f",MONTAJ(M{instance.orders_number}) EMRİ KAPANDI,YENİ MONTAJ EMRİ OLUŞTURULDU."
            instance.status = "passive"
            aorders=Assembly_Orders(
                work_orders_number =instance.work_orders_number,
                orders_number = None
            )
            aorders.save()
            messages.success(request, "İş Emri Kapandı;Yeni İş Emri Açıldı.")
        elif "assembly" in request.POST:
            instance.status = "passive"
            order.status = "6"
            order.job_done += ",MONTAJ EMRİ KAPANDI,İŞ EMRİ KAPANDI"
            messages.success(request, "İş Emri Kapandı,Montaj İş Emri Kapandı")
        else:
            messages.add_message(
                    request,messages.SUCCESS    ,
                            "Düzenleme Başarılı" )
        order.save()
        instance.save()
        return redirect ('assembly')

    return render(request, "orders/update_order.html",context)


# def updateassembly(request,id):
#     instance = Assembly_Orders.objects.get(id=id)
#     order = Work_Orders.objects.get(id=instance.work_orders_number.id)
#     invertory = İnvertory.objects.get(id=instance.work_orders_number.invertory.id)
#     form = OrderİnvertoryForm(request.POST or None, instance=invertory)
#     context = {
#         "items" :instance,
#         "form" :form,
#     }
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             if "newassembly" in request.POST:
#                 order.job_done += f",MONTAJ(M{instance.assembly_orders_number}) EMRİ KAPANDI,YENİ MONTAJ EMRİ OLUŞTURULDU."
#                 instance.status = "passive"
#                 aorders=Assembly_Orders(
#                     work_orders_number =instance.work_orders_number,
#                     assembly_orders_number = None
#                 )
#                 aorders.save()
#                 messages.success(request, "İş Emri Kapandı;Yeni İş Emri Açıldı.")
#             elif "assembly" in request.POST:
#                 instance.status = "passive"
#                 order.status = "6"
#                 order.job_done += ",MONTAJ EMRİ KAPANDI,İŞ EMRİ KAPANDI"
#                 messages.success(request, "İş Emri Kapandı,Montaj İş Emri Kapandı")
#             else:
#                 messages.add_message(
#                         request,messages.SUCCESS    ,
#                                 "Düzenleme Başarılı" )
#             order.save()
#             instance.save()
#             return redirect ('assembly')
#         else:
#             messages.add_message(
#                     request,messages.WARNING,
#                             " Form hatalı giriş yapıldı." )
    
#     return render(request, "orders/assembly/update_assembly.html",context)


def deleteAssembly(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = Assembly_Orders.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Atölye İş Emri Silindi.")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta.")

    return redirect(reverse('assembly'))



