from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

# def testing(request):
#     mymembers = Member.objects.all().values()
#     template = loader.get_template('template.html')
#     context = {
#         'mymembers': mymembers
#     }
#     return HttpResponse(template.render(context, request))

def testing(request):
    # 1.
    # mymembers = Member.objects.filter(firstname='Kudratullo').values()
    
    # 2.
    # mymembers = Member.objects.filter( id = 7, firstname = "Jane").values()

    # 3.  way 1
    # mymembers = Member.objects.filter( id = 7).values() | Member.objects.filter(id = 8).values()
           
        #    way 2
    # mymembers = Member.objects.filter(Q(id = 4) | Q(id = 7))

    # 4
    mymembers = Member.objects.filter(firstname__icontains = 'l').values()

    template = loader.get_template('template.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))