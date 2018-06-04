from django.conf.urls import url,include
from django.contrib import admin
import bankapp.views as bankappViews

urlpatterns = [
    url(r'^account/$', bankappViews.AccountView.as_view()),
    url(r'^account/deposit/$', bankappViews.AccountMoneyDeposit.as_view()),
    url(r'^account/withdrawl/$', bankappViews.AccountMoneyWithdrawl.as_view())
]
 
