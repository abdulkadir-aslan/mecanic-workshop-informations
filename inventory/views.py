from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib import messages
from .models import Power, İnvertory,Mark,Engine
from django.db.models import ProtectedError
from .forms import *
from django.http import JsonResponse, HttpResponse




def newMark(request):
    if request.method == "POST":
        form = MarkForm(request.POST)
        try:
            if form.is_valid():
                item = form.save()
                messages.add_message(
                        request,messages.SUCCESS,
                        f'*{ form.data["engine_mark"] }* Kayıt başarılı.')
                return redirect ('mark_add')
            else:
                messages.warning(request,form.errors.as_ul())
        except Exception:
            messages.add_message(
                        request,messages.WARNING,
                        f'*{ form.data["engine_mark"] }* Bu Marka alanına sahip değer zaten mevcut')
    else:
        form = MarkForm() 
    
    context ={
        'items': Mark.objects.all().order_by("-id"),
        'form':form 
    }
    return render(request,"invertory/new_mark.html",context)

def markDelete(request,myid):
    mark = Mark.objects.get(id=myid)
    try:
        mark.delete()
        messages.add_message(
                            request,messages.SUCCESS,
                            f'*{ mark.engine_mark }* Markası silindi.')
    except ProtectedError:
        messages.add_message(
                            request,messages.WARNING,
                            f'*{ mark.engine_mark }* Markası diğer tablolarda kullanılmakta.' )
    return redirect('mark_add')

def newPower(request):
    if request.method == "POST":
        form = PowerForm(request.POST)
        try:
            if form.is_valid():
                item = form.save()
                messages.add_message(
                        request,messages.SUCCESS,
                        f'*{ form.data["engine_power"] }* Kayıt başarılı.')
                return redirect ('power_add')
            else:
                messages.add_message(
                        request,messages.WARNING,form.errors.as_ul())
        except Exception:
            messages.add_message(
                        request,messages.WARNING,
                        f'*{ form.data["engine_power"] }* Bu Güç değerine sahip değer zaten mevcut')
    else:
        form = PowerForm() 
    context ={
        'items': Power.objects.all().order_by("-id"),
        'form':form
    }
    return render(request,"invertory/new_power.html",context)

def powerDelete(request,myid):
    mark = Power.objects.get(id=myid)
    try:
        mark.delete()
        messages.add_message(
                            request,messages.SUCCESS,
                            f'*{ mark.engine_power }* Güç değeri silindi.')
    except ProtectedError:
        messages.add_message(
                            request,messages.WARNING,
                            f'*{ mark.engine_power }* Güç değeri diğer tablolarda kullanılmakta.' )
    return redirect('power_add')


def newPump(request):
    if request.method == "POST":
        form = PumpForm(request.POST)
        try:
            if form.is_valid():
                item = form.save()
                messages.add_message(
                        request,messages.SUCCESS,
                        f'*{ form.data["pump_type"] }-{ form.data["number_stages"] }* Kayıt başarılı.')
                return redirect ('pump_add')
            else:
                messages.add_message(
                        request,messages.WARNING,form.errors.as_ul())
        except Exception:
            messages.add_message(
                        request,messages.WARNING,
                        f'*{ form.data["pump_type"] }-{ form.data["number_stages"] }* Bu Pompa alanına sahip Kayıt zaten mevcut')
    else:
        form = PumpForm() 
    context ={
        'items': Pump.objects.all().order_by("-id"),
        'form' : form
    }
    return render(request,"invertory/new_pump.html",context)

def pumpDelete(request,myid):
    mark = Pump.objects.get(id=myid)
    try:
        mark.delete()
        messages.add_message(
                            request,messages.SUCCESS,
                            f'*{ mark.pump_type }-{ mark.number_stages}* Pompa kaydı silindi.')
    except ProtectedError:
        messages.add_message(
                            request,messages.WARNING,
                            f'*{ mark.pump_type }-{ mark.number_stages}* Pompası diğer tablolarda kullanılmakta.' )
    return redirect('pump_add')


def newEngine(request):
    if request.method == "POST":
        form = EngineForm(request.POST)
        try:
            if form.is_valid():
                item = form.save()
                messages.add_message(
                        request,messages.SUCCESS,
                        f'Kayıt başarılı.')
                return redirect ('engine_add')
            else:
                messages.add_message(
                        request,messages.WARNING,form.errors.as_ul())
        except Exception:
            pass
    else:
        form = EngineForm() 
    context ={
        'items': Engine.objects.all().order_by("-id"),
        'form':form
    }
    return render(request,"invertory/new_engine.html",context)

def engineDelete(request,myid):
    mark = Engine.objects.get(id=myid)
    try:
        mark.delete()
        messages.add_message(
                            request,messages.SUCCESS,
                            f'*{ mark.engine_power } HP * Motor kaydı silindi.')
    except ProtectedError:
        messages.add_message(
                            request,messages.WARNING,
                            f'*{ mark.engine_power } HP * Motoru diğer tablolarda kullanılmakta.' )
    return redirect('engine_add')

#İnvertory

def view_invertory_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = İnvertory.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.well_number)+" Numaralı Kuyu"
        previous = İnvertoryForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def invertory(request):
    inventory = İnvertory.objects.order_by('-id').all()
    form = İnvertoryForm(request.POST or None)
    context = {
        'inventory': inventory,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
            return redirect(reverse('invertory'))
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "invertory/invertory.html", context)

def updateİnvertory(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = İnvertory.objects.get(id=request.POST.get('id'))
        pos = İnvertoryForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, f"*{instance.well_number}* Numaralı Kuyu Kaydı Güncellendi")
    except:
        messages.warning(request, "Kuyu Numarası Daha Önce Kullanıldı.")

    return redirect(reverse('invertory'))

def deleteİnvertory(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = İnvertory.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Kuyu Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('invertory'))

# --------------------------- Store --------------------------

def store(request):
    context ={
        'engine': ZeroEngineStock.objects.all().filter(stock__gt = 0).order_by("-id"),
        'pump': ZeroPumpStock.objects.all().filter(stock__gt = 0).order_by("-id"),
        'other': ZeroOtherStock.objects.all().filter(stock__gt = 0).order_by("-id"),
    }
    return render(request,"store/zero/zero.html",context)

#Zero Engine
def view_zeroEngine_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = ZeroEngineStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.engine)
        previous = ZeroEngineForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def zeroEngine(request):
    engine = ZeroEngineStock.objects.order_by('-id').all()
    form = ZeroEngineForm(request.POST or None)
    context = {
        'engine': engine,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/zero/engine.html", context)

def updateZeroEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = ZeroEngineStock.objects.get(id=request.POST.get('id'))
        pos = ZeroEngineForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Motor Kaydı Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('zeroEngine'))

def deleteZeroEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = ZeroEngineStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Motor Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('zeroEngine'))

#Zero Pump
def view_zeroPump_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = ZeroPumpStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.pump)
        previous = ZeroPumpForm(instance=pos)
        context['form'] = previous.as_p()
    return JsonResponse(context)

def zeroPump(request):
    pump = ZeroPumpStock.objects.order_by('-id').all()
    form = ZeroPumpForm(request.POST or None)
    context = {
        'pump': pump,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/zero/pump.html", context)

def updateZeroPump(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = ZeroPumpStock.objects.get(id=request.POST.get('id'))
        pos = ZeroPumpForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Pompa Kaydı Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('zeroPump'))

def deleteZeroPump(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = ZeroPumpStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Pompa Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('zeroPump'))

def view_zeroOther_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = ZeroOtherStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos)
        previous = ZeroOtherForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def other(request):
    engine = ZeroOtherStock.objects.order_by('-id').all()
    form = ZeroOtherForm(request.POST or None)
    context = {
        'engine': engine,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/zero/other.html", context)

def updateOther(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = ZeroOtherStock.objects.get(id=request.POST.get('id'))
        pos = ZeroOtherForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Kayıt Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('other'))

def deleteOther(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = ZeroOtherStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Kayıt Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('other'))

#TWOND
def twondstore(request):
    context ={
        'engine': TwondEngineStock.objects.all().filter(stock__gt = 0).order_by("-id"),
        'pump': TwondPumpStock.objects.all().filter(stock__gt = 0).order_by("-id"),
    }
    return render(request,"store/twond/home.html",context)
#Two Engine
def view_twondEngine_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = TwondEngineStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.engine)
        previous = TwondEngineForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def twondEngine(request):
    engine = TwondEngineStock.objects.order_by('-id').all()
    form = TwondEngineForm(request.POST or None)
    context = {
        'engine': engine,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/twond/engine.html", context)

def updateTwondEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = TwondEngineStock.objects.get(id=request.POST.get('id'))
        pos = TwondEngineForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Motor Kaydı Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('twondEngine'))

def deleteTwondEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = TwondEngineStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Motor Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('twondEngine'))

#Two Pump
def view_twondPump_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = TwondPumpStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.pump)
        previous = TwondPumpForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def twondPump(request):
    pump = TwondPumpStock.objects.order_by('-id').all()
    form = TwondPumpForm(request.POST or None)
    context = {
        'pump': pump,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/twond/pump.html", context)

def updateTwondPump(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = TwondPumpStock.objects.get(id=request.POST.get('id'))
        pos = TwondPumpForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Pompa Kaydı Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('twondPump'))

def deleteTwondPump(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = TwondPumpStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Pompa Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('twondPump'))

#ENGİNE
def twondstore(request):
    context ={
        'engine': TwondEngineStock.objects.all().filter(stock__gt = 0).order_by("-id"),
        'pump': TwondPumpStock.objects.all().filter(stock__gt = 0).order_by("-id"),
    }
    return render(request,"store/twond/home.html",context)
#Two Engine
def view_twondEngine_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = TwondEngineStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.engine)
        previous = TwondEngineForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def twondEngine(request):
    engine = TwondEngineStock.objects.order_by('-id').all()
    form = TwondEngineForm(request.POST or None)
    context = {
        'engine': engine,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/twond/engine.html", context)

def updateTwondEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = TwondEngineStock.objects.get(id=request.POST.get('id'))
        pos = TwondEngineForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Motor Kaydı Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('twondEngine'))

def deleteTwondEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = TwondEngineStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Motor Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('twondEngine'))

# REPAİR

def repairstore(request):
    context ={
        'engine': RepairStock.objects.all().filter(stock__gt = 0).order_by("-id"),
    }
    return render(request,"store/repair/home.html",context)
#Two Engine
def view_repair_by_id(request):
    pos_id = request.GET.get('id', None)
    pos = RepairStock.objects.filter(id=pos_id)
    context = {}
    if not pos.exists():
        context['code'] = 404
    else:
        context['code'] = 200
        pos = pos[0]
        context['fullname'] = str(pos.engine)
        previous = RepairStockForm(instance=pos)
        context['form'] = str(previous.as_p())
    return JsonResponse(context)

def repairEngine(request):
    engine = RepairStock.objects.order_by('-id').all()
    form = RepairStockForm(request.POST or None)
    context = {
        'engine': engine,
        'form1': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt Başarılı")
        else:
            messages.error(request, "Form Hatalı")
    return render(request, "store/repair/engine.html", context)

def updateRepairEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        instance = RepairStock.objects.get(id=request.POST.get('id'))
        pos = RepairStockForm(request.POST or None, instance=instance)
        pos.save()
        messages.success(request, "Motor Kaydı Güncellendi")
    except:
        messages.error(request, "Form Hatalı")

    return redirect(reverse('repairEngine'))

def deleteRepairEngine(request):
    if request.method != 'POST':
        messages.error(request, "Access Denied")
    try:
        pos = RepairStock.objects.get(id=request.POST.get('id'))
        pos.delete()
        messages.success(request, "Motor Kaydı Silindi")
    except:
        messages.error(request, "Bu Kayıt Başka Tabloda Kullanılmakta")

    return redirect(reverse('repairEngine'))

