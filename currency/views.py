from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import CURRENCY_CHOICES
from .utils import get_conversion

# Create your views here.


class CurrencyConvert(View):
    def get(self, request):
        """
        The view that renders HTML page to convert currencies
        :param request: The request contains of params: base, query and amount
        :return: HTML template running with Jinja Engine
        """
        try:
            # base: currency to convert from
            base_currency = request.GET['base'].upper()
            # query: currency to convert to
            query_currency = request.GET['query'].upper()
            # amount: amount to be converted
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
        except KeyError:
            # In case the user sends a bad request, i.e. without the params, redirect him to a default page!
            return redirect(f"/currency/convert?base={CURRENCY_CHOICES[0]}&query={CURRENCY_CHOICES[0]}&amount=0.0")
        except Exception as e:
            return HttpResponse(str(e))
