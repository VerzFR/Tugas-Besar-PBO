from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from profiles.models import Status 
import random
from django.contrib import messages
from django.contrib.auth.models import User

def randomGen():
    # return a 11 digit random number
    return int(random.uniform(10000000000, 99999999999))

def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user) # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen() # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/profile.html", {"curr_user": curr_user})

def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.MoneyTransfer.objects.get(Masukan_Nama_Penyetor=request.user)
            dest_user_acc_num = curr_user.Masukan_No_Akuns_Tujuan

            temp = curr_user # NOTE: Delete this instance once money transfer is done
            
            dest_user = models.Status.objects.get(account_number=dest_user_acc_num) # FIELD 1
            transfer_amount = curr_user.Masukan_Jumlah_Uang_Dalam_USD # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user) # FIELD 3

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

            temp.delete() # NOTE: Now deleting the instance for future money transactions

        return redirect("profiles/profile.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "profiles/money_transfer.html", {"form": form})

def loan(request):
    return render(request, "profiles/loans.html")

def settings(request):
    return render(request, "profiles/settings.html")

def edit_details(request):
    if request.method == "POST":
        # POST actions for CustomerForms
        try:
            curr_user = models.Customer.objects.get(user_name=request.user)
            form = forms.CustomerForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.CustomerForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()  
        
        # POST actions for Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect("profiles/edit_details.html")
    
    else: # GET actions
        try:
            curr_user = models.Customer.objects.get(user_name=request.user)
            form1 = forms.CustomerForm(instance=curr_user) # basic details
        except:
            form1 = forms.CustomerForm()


        # change password
        form3 = PasswordChangeForm(request.user)

        dici = {"form1": form1, "form3": form3}
        return render(request, "profiles/edit_details.html", dici)

def delete_account(request):
    try:
        u = User.objects.get(username = akunusername)
        u.delete()
        messages.success(request, "The user is deleted")
    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")    
        return render(request, 'index.html')

    except Exception as e: 
        return render(request, 'index.html')
    return render(request, "index.html")
