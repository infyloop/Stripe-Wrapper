# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from sales.forms import SalePaymentForm
from sales.forms import SubscriptionPaymentForm, SubscriptionCreationForm


def charge(request):
    if request.method == "POST":
        form = SalePaymentForm(request.POST)
        if form.is_valid():   # charges the card
            return HttpResponse("Success! We've charged your card!")
    else:
        form = SalePaymentForm()
    return render_to_response("charge.html",
                              RequestContext(request, {'form': form, 'button_text': "Pay!!"}))


def create(request):
    if request.method == "POST":
        form = SubscriptionCreationForm(request.POST)
        if form.is_valid():   # charges the card
            return HttpResponse("Success! We've creted the subscription plan!")
    else:
        form = SubscriptionCreationForm()
    return render_to_response("charge.html",
                              RequestContext(request, {'form': form, 'button_text': "Create a plan!"}))


def subscribe(request):
    if request.method == "POST":
        form = SubscriptionPaymentForm(request.POST)
        if form.is_valid():   # charges the card
            return HttpResponse("Success! you have been successfully subscribed to our Plan!!")
    else:
        form = SubscriptionPaymentForm()
    return render_to_response("charge.html",
                    RequestContext(request, {'form': form, 'button_text': "Subscribe!"}))
