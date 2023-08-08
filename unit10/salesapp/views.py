from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import SalesModel

# Create your views here.
class init(ListView):
    template_name = 'init.html'
    model = SalesModel

class detail(ListView):
    template_name ='detail.html'
    model = SalesModel
    context = {'object_list': model.objects.all(),}
    print('called detail')

    def post(self, request, *args, **kwargs):
        print('called post')
        result = SalesModel.objects.get(merchandise=request.POST.get('merchandise'))
        amout = int(request.POST.get('amout'))
        
        goods = request.session.get('goods')
        if  goods is None and amout != 0:
            goods = {
                    result.merchandiseID:{
                    'merchandise': result.merchandise,
                    'amout': amout,
                    'totalPrice': result.unitPrice * amout,
                    }
            }
        elif goods is not None and amout != 0:
            if result.merchandiseID in goods:
                goods[result.merchandiseID]['amout'] = amout
                goods[result.merchandiseID]['totalPrice'] = result.unitPrice * amout

            else:
                goods.update({
                    result.merchandiseID:{
                        'merchandise': result.merchandise,
                        'amout': amout,
                        'totalPrice': result.unitPrice * amout,
                    }
                })
        elif amout == 0:
            del goods[result.merchandiseID]
        
        request.session['goods'] = goods
        self.context.update({'goods':goods})
        print(self.context)
        return render(request, 'detail.html', self.context)
    
    def get(self, request, *args, **kwargs):
        print(request.GET.get('del'))
        if request.GET.get('del') is None:
            return render(request, 'detail.html', self.context)
        else:
            delMerchandiseID = list(self.context['goods'].keys())[int(request.GET.get('del'))]
            del self.context['goods'][delMerchandiseID]
            request.session['goods'] = self.context['goods']
            print(self.context)
            return render(request, 'detail.html', self.context)

class result(ListView):
    template_name = 'result.html'
    model = SalesModel
    def get(self, request, *args, **kwargs):
        print('called result get')
        import time
        print(dict(request.session))
        request.session.update({'salesid':int(time.time())})
        return render(request, 'result.html', dict(request.session))
