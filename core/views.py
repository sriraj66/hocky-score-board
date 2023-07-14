from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    context = {
        "matches":Match.objects.all()
    }
    return render(request,'index.html',context)


def update_panel(request,id):
    match = Match.objects.get(id=id)

    
    if request.method == 'GET':
        try:
            
            return JsonResponse({
                "t_1" : match.t_1,
                "t_2":match.t_2,
                "t_s_1":match.t_s_1,
                "t_s_2":match.t_s_2,
                "quater":match.quater,
                "min":"{:02d}".format(match.timer.min),
                "sec":"{:02d}".format(match.timer.sec),
                
                "t_1_c":match.t_1_c,
                "t_2_c":match.t_2_c,
                "t_c":match.t_c,
                "s_c":match.s_c,
                "q_c":match.q_c,
                "b_g":match.b_g,
            })
        except Match.DoesNotExist:
            return JsonResponse({"t_1" : "-",
                "t_2":"-",
                "t_s_1":"-",
                "t_s_2":"-",
                "quater":"Q1",
                "min":"00",
                "sec":"00",
                
                "t_1_c":"skyblue",
                "t_2_c":"green",
                "t_c":"greay",
                "s_c":"yellow",
                "q_c":"red"})
    else:
        return JsonResponse({"Error":"Not Found"})

def dash(request,id):
    match = Match.objects.get(id=id)

    context = {
        "match":match
    }

    return render(request,'dash.html',context)


def control(request,id):
    match = Match.objects.get(id=id)
    context = {
        'match':match
    }
    return render(request,'control.html',context)

def create_match(request):
    if request.POST:
        obj = Match()
        timer = Timer()
        timer.save()
        obj.timer = timer
        obj.save()
        return redirect('control',obj.id)
    return redirect("index")

def update_details(request,id):
    match = Match.objects.get(id=id)

    if request.POST:

        match.t_1 = request.POST.get("t_1",match.t_1)
        match.t_2 = request.POST.get("t_2",match.t_2)
        match.t_s_1 = request.POST.get("t_s_1",match.t_s_1)
        match.t_s_2 = request.POST.get("t_s_2",match.t_s_2)
        match.min = request.POST.get("min",match.min)
        match.sec = request.POST.get("sec",match.sec)
        match.quater = request.POST.get("quater",match.quater)

        match.save()
        print("SAVED")
    
    return redirect("control",match.id)


def update_color(request,id):
    match = Match.objects.get(id=id)

    if request.POST:

        match.t_1_c = request.POST.get("t_1_c",match.t_1_c)
        match.t_2_c = request.POST.get("t_2_c",match.t_2_c)
        match.t_c = request.POST.get("t_c",match.t_c)
        match.s_c= request.POST.get("s_c",match.s_c)
        match.q_c = request.POST.get("q_c",match.q_c)
        match.b_g = request.POST.get("b_g",match.b_g)
        
        match.save()
    
    return redirect("control",match.id)

@csrf_exempt
def start_timer(request,id):

    match = Match.objects.get(id=id)
    print("Start_timer")
    if request.method == 'POST':
        sec = int(match.min) * 60 + int(match.sec)
        match.timer.sec = match.sec
        match.timer.min = match.min
        match.timer.total_sec = sec

        match.timer.is_running = True
        match.timer.is_pause = False
        match.timer.save()
        match.save()

        return JsonResponse({"min":match.timer.min,"sec":match.timer.sec,"is_running":match.timer.is_running,"is_pause":match.timer.is_pause})

    return JsonResponse({"error":"Invalid Request"})

def update_timer(request,id):
    match = Match.objects.get(id=id)
    print("PAUSE : ",match.timer.is_pause)
    if request.method == 'GET' and match.timer.is_running:
        if match.timer.is_pause == False:
            match.timer.total_sec-=1
        if match.timer.total_sec<0:
            match.timer.is_running = False
        match.timer.min = match.timer.total_sec // 60 
        match.timer.sec = match.timer.total_sec % 60
    
        match.timer.save()

    return JsonResponse({"min":match.timer.min,"sec":match.timer.sec,"is_running":match.timer.is_running,"is_pause":match.timer.is_pause})

def reset_timer(request,id):
    match = Match.objects.get(id=id)
    if request.method == 'GET':
        sec = int(match.min) * 60 + int(match.sec)
        match.timer.sec = match.sec
        match.timer.min = match.min
        match.timer.total_sec = sec
        match.timer.is_pause = True
        match.timer.save()

    return JsonResponse({"min":match.timer.min,"sec":match.timer.sec,"is_running":match.timer.is_running,"is_pause":match.timer.is_pause})


def stop_timer(request,id):
    match = Match.objects.get(id=id)
    if request.method == 'GET' and match.timer.is_running:
        match.timer.min = match.timer.total_sec // 60 
        match.timer.sec = match.timer.total_sec % 60
        
        match.timer.is_running = False

        match.timer.save()

        return JsonResponse({"min":match.timer.min,"sec":match.timer.sec,"is_running":match.timer.is_running,"is_pause":match.timer.is_pause})

    return JsonResponse({"error":"Invalid Request"})

def pause_timer(request,id):
    match = Match.objects.get(id=id)
    
    if request.method == 'GET' and match.timer.is_running:
        match.timer.min = match.timer.total_sec // 60 
        match.timer.sec = match.timer.total_sec % 60
        print("Done")    
        match.timer.is_running =True
        match.timer.is_pause = True

        match.timer.save()
        match.save()

        return JsonResponse({"min":match.timer.min,"sec":match.timer.sec,"is_running":match.timer.is_running,"is_pause":match.timer.is_pause})

    return JsonResponse({"error":"Invalid Request"})


def resume_timer(request,id):
    match = Match.objects.get(id=id)
    if request.method == 'GET' and match.timer.is_running:
        match.timer.min = match.timer.total_sec // 60 
        match.timer.sec = match.timer.total_sec % 60
        
        match.timer.is_running =True
        match.timer.is_pause = False

        match.timer.save()

        return JsonResponse({"min":match.timer.min,"sec":match.timer.sec,"is_running":match.timer.is_running,"is_pause":match.timer.is_pause})

    return JsonResponse({"error":"Invalid Request"})

