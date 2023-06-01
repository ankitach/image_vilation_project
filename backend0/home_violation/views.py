from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from home_violation.models import vid_stream_violations



# from django.template import loader
# Create your views here.
def home(request):
     return render(request, "home_violation/home.html")
def ppe(request):
     via1 = vid_stream_violations.objects.all()
     regid = loader.get_template('home_violation\Personal_Protective_Equipment\ppebase.html')
     context = {'via1':via1,}
     return HttpResponse(regid.render(context, request))