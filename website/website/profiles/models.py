from django.db import models
import datetime

class Customer (models.Model): 
    name = models.CharField(max_length = 50, default = None)
    email = models.EmailField(default = None)
    address = models.CharField(max_length=50, default=None)
    phone = models.IntegerField (default=0)
    user_name = models.CharField(max_length = 150, default = None)

class Status (models.Model):
    account_number = models.IntegerField(default=0)
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)

class MoneyTransfer(models.Model):
    Masukan_Nama_Penyetor = models.CharField(max_length = 150, default = None)
    Masukan_No_Akuns_Tujuan = models.IntegerField()
    Masukan_Jumlah_Uang_Dalam_USD = models.IntegerField()

