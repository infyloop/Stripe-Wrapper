from django.db import models

import settings


class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)
        # bring in stripe, and get the api key from settings.py
        import stripe
        stripe.api_key = settings.STRIPE_API_KEY
        self.stripe = stripe
    # store the stripe charge id for this sale
    charge_id = models.CharField(max_length=32)
    # you could also store other information about the sale
    # but I'll leave that to you!

    def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
        if self.charge_id:   # don't let this be charged twice!
            return False, Exception(message="Already charged.")
        try:
            response = self.stripe.Charge.create(
                amount=price_in_cents,
                currency="usd",
                card={
                    "number": number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc,
                },
                description='Thank you for your purchase!')
            self.charge_id = response.id
        except self.stripe.CardError, ce:
            # charge failed
            return False, ce
        return True, response

    def subscribe(self, number, exp_month, exp_year, cvc):
        try:
            response = self.stripe.Customer.create(
                card={
                    "number": number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc,
                    },
                plan="Gold",
                email="payinguser@example.com",
                description="Thanks for subscribing")
            self.charge_id = response.id
        except self.stripe.CardError, ce:
            return False, ce
        return True, response

    def create(self, plan_name, plan_id, monthly_charge):
        response = self.stripe.Plan.create(
        amount=monthly_charge,
        interval='month',
        name=plan_name,
        currency="usd",
        id=plan_id,
        description="You have created a plan with name " + plan_name + "and id " + plan_id)
        self.charge_id = response.id
        return True, response
