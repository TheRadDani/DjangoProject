from django.shortcuts import render, get_object_or_404
from .models import Jobs

# Create your views here.
def juancito(request):
    jobs = Jobs.objects
    return render(request,'jobs/juancito.html',
    {'jobs':jobs})

def detail(request,job_id):
    job_detail = get_object_or_404(Jobs,pk=job_id)#primary key
    return render(request,'jobs/detail.html',{'job':job_detail})
    