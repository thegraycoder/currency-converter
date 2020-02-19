from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import CURRENCY_CHOICES
from .utils import get_conversion

# Create your views here.


class CurrencyConvert(View):
    def get(self, request):
        try:
            base_currency = request.GET['base'].upper()
            query_currency = request.GET['query'].upper()
            query_amount = request.GET['amount']
            if base_currency not in CURRENCY_CHOICES or query_currency not in CURRENCY_CHOICES:
                raise ValueError('Invalid currency choice')
            result_amount = get_conversion(
                base_currency, query_currency, query_amount
            )
            return render(request, 'convert.html', context={
                "currency_options": CURRENCY_CHOICES,
                "amount": query_amount,
                "base": base_currency,
                "query": query_currency,
                "result": result_amount
            })
        except KeyError as ke:
            return redirect(f"/currency/convert?base={CURRENCY_CHOICES[0]}&query={CURRENCY_CHOICES[0]}&amount=0.0")
        except Exception as e:
            return HttpResponse(str(e))
