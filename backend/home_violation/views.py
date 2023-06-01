from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from home_violation.models import vid_stream_violations, vid_stream_cameras
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q


# from django.template import loader
# Create your views here.
def home(request):
     return render(request, "home/home.html")
#---------------------table logic--------------------------------
def ppe(request):
     
     via1 = vid_stream_violations.objects.all()
     count = vid_stream_violations.objects.all().count()
     # count_time = vid_stream_violations.objects.all().count()
     
     paginator = Paginator(via1, 10)
     page_number =request.GET.get('page')
     via1 = paginator.get_page(page_number)

     loc1 = vid_stream_cameras.objects.all()

     context = {'via1':via1,'count': count, 'loc1':loc1}
     return render(request, 'Personal_Protective_Equipment/ppe.html', context )
    
     
#-----------------------end table logic--------------------------------
def camera1(request):
     return render(request, 'Camera-1/')


def ppe_filter(request):
    if request.method == 'POST':
        viol_Camera_id = request.POST['viol_Camera_id']
        via1 = vid_stream_violations.objects.all()
        if viol_Camera_id:
            via1 = via1.filter(viol_Camera_id__name__icontains = viol_Camera_id)
        context = {
            'via1': via1
        }
        return render(request, 'Personal_Protective_Equipment/ppe.html', context)

    elif request.method == 'GET':
        return render(request, 'Personal_Protective_Equipment/ppe.html')
    else:
        return HttpResponse('An Exception Occurred')
   