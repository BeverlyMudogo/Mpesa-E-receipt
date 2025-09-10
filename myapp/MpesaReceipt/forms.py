from django import forms

class MpesaPaymentForm(forms.Form):
    Mpesa_sms_field=forms.CharField(
        widget=forms.Textarea
        (attrs={
            'placeholder':'Paste your Mpesa SMS here', 
            'rows':10, 
            'cols':40
            })
        )