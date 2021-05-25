from django import forms
from . import models

class CustomerForm (forms.ModelForm):
    # class to store all the model form fields from models.py
    class Meta:
        model = models.Customer
        fields = ["name", "email", "address", "phone"]

class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = models.MoneyTransfer
        fields = [
            "Masukan_Nama_Penyetor",
            "Masukan_No_Akuns_Tujuan", 
            "Masukan_Jumlah_Uang_Dalam_USD"
        ]
