from django.shortcuts import render
from bill.models import Bill
# Create your views here.
from additionals.models import Additionals
from cheif.models import Cheif


def bill(request):
    aobj=Additionals.objects.all()
    for ao in aobj:
        obj = Bill()
        # obj.no=""
        obj.nameofexaminer=ao.name
        obj.nameofcollage = ao.collegename
        obj.category='additional'
        obj.total_no_of_paper = ao.totelpapers
        obj.mandatory_deduction = "25"
        obj.elligibel_no_of_papers=ao.totelpapers
        obj.remuneration = '900'
        obj.additional_maximum_chairman_fee = '1500'
        obj.remunerationfor_decussiom =900 + int(obj.total_no_of_paper)*35
        obj.totel = obj.remunerationfor_decussiom+1500+25
        obj.save()

    cobj = Cheif.objects.all()

    for ao in cobj:
            obj = Bill()
            # obj.no = ""
            obj.nameofexaminer = ao.name
            obj.nameofcollage = ao.collegename
            obj.category = 'chief'
            obj.total_no_of_paper = ao.totelpapers
            obj.mandatory_deduction = "35"
            obj.elligibel_no_of_papers = ao.totelpapers
            obj.remuneration = 'high'
            obj.additional_maximum_chairman_fee = '1500'
            obj.remunerationfor_decussiom = 1200 + int(obj.total_no_of_paper)*35
            obj.totel =  obj.remunerationfor_decussiom+1500+25
            obj.save()


    obbill=Bill.objects.all()
    context={
        'obj':obbill
    }

    return render(request, 'bill/bill.html',context)


# Re: *CLR* No of days x 600
# *Additionals* Discussion: 900 + No. Of papers* 35
# *Chief* Discussion: 1200 + Highest of additionals remuneration
# *Chairman* Discussion: 1500 + Chairman fee:2000 + Additional Remuneration