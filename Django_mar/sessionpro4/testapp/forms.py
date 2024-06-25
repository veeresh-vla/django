from django import forms
class AdditemForm(forms.Form):
    itemname=forms.CharField()
    quantity=forms.IntegerField()
