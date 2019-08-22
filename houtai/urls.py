"""houtai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^$',views.login,name='login'),
    url(r'^index$', views.index,name='index'),
    url(r'^home$',views.home,name='home'),
    url(r'^Products_List$',views.Products_List,name='Products_List'),
    url(r'^picture_add$',views.picture_add,name='picture_add'),
    url(r'^Brand_Manage$',views.Brand_Manage,name='Brand_Manage'),
    url(r'^Category_Manage$',views.Category_Manage,name='Category_Manage'),
    url(r'^product-category-add$',views.productadd,name='productadd'),
    url(r'^advertising$',views.advertising,name='advertising'),
    url(r'^Sort_ads$',views.Sort_ads,name='Sort_ads'),
    url(r'^transaction$',views.transaction,name='transaction'),
    url(r'^Orderform$',views.Orderform,name='Orderform'),
    url(r'^Amounts$',views.Amounts,name='Amounts'),
    url(r'^member_Grading$',views.member_Grading,name='member_Grading'),
    url(r'^user_list$',views.user_list,name='user_list'),
    url(r'^integration$',views.integration,name='integration'),
    url(r'^Guestbook$',views.Guestbook,name='Guestbook'),
    url(r'^Feedback$',views.Feedback,name='Feedback'),
    url(r'^Systems$',views.Systems,name='Systems'),
    url(r'^admin_Competence$',views.admin_Competence,name='admin_Competence'),
    url(r'^administrator$',views.administrator,name='administrator'),
    url(r'^admin_info$',views.admin_info,name='admin_info'),
    url(r'^Order_handling$',views.Order_handling,name='Order_handling'),
    url(r'^order_detailed/(\d+)$',views.order_detailed,name='order_detailed'), #订单详情
    url(r'^member_show$',views.member_show,name='member_show'), #用户信息
    url(r'^Cover_management$',views.Cover_management,name='Cover_management'),
    url(r'^Competence$',views.Competence,name='Competence'), #添加权限
    url(r'^Brand_detailed$',views.Brand_detailed,name='Brand_detailed'),#品牌信息
    url(r'^Ads_list',views.Ads_list,name='Ads_list'), #广告列表
    url(r'^Add_Brand$',views.Add_Brand,name='Add_Brand'),#添加品牌
    url(r'^Feedback_2$',views.Feedback_2,name='Feedback_2'),
]
