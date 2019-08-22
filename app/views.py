import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import datetime
# Create your views here.
from django.urls import reverse

from YJ import youjian
from app.models import User, Manage, Order, Mdelu, track, Ad, Category, Shangp, Details, Size, System, Eval, Xiang,Address


def index(request):
    name = request.session.get('key', None)
    num = Order.objects.filter(orderState=0).__len__()
    num2 = Eval.objects.filter(isli=0).__len__()
    num3 = User.objects.filter(gold__lt=100).__len__()
    su = num + num2 + num3
    man = Manage.objects.get(managername=name)
    type = man.type
    return render(request,'index.html',context={'name':name,'num':num,'num2':num2,'num3':num3,'su':su,'type':type})


def home(request):
    num = User.objects.all().aggregate(Count('uid'))
    num = num['uid__count']
    num1 = Order.objects.all().aggregate(Count('oid'))
    num1 = num1['oid__count']
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    ip = request.META['REMOTE_ADDR']
    return render(request,'home.html',context={'num1':num1,'num':num,'date':date,'time':time,'ip':ip})


def Products_List(request):
    shuju = Shangp.objects.values().all()
    shuju1 = Category.objects.values().all()
    num = Shangp.objects.all().aggregate(Count('cid'))
    num = num['cid__count']
    xd = request.POST.getlist("xuanzhong")
    anniu = request.POST.get("删除")
    if anniu:
        for id in xd:
            s = Shangp.objects.get(cid=id)
            s.delete()
    tt = request.POST.get('aa')
    if tt == "启用":
        id = request.POST.get("xuan")
        pi = Shangp.objects.get(cid=id)
        pi.isshow = 1
        pi.save()
    if tt == "停用":
        id = request.POST.get("xuan")
        pi = Shangp.objects.get(cid=id)
        pi.isshow = 0
        pi.save()

    return render(request,'Products_List.html',context={'shuju':shuju,'num':num,'shuju1':shuju1})


def picture_add(request):
    shuju = Category.objects.values().all()
    if request.method == "POST":
        name = request.POST.get("name")
        id1 = request.POST.get("id1")
        id2 = request.POST.get("id2")
        bianhao = request.POST.get("bian")
        pp = request.POST.get("price")
        key = request.POST.get("keyword")
        beizhu = request.POST.get("beizhu" )
        photo = request.FILES.get("upload")
        path = os.path.join(os.getcwd(), 'static\\upload')
        pathname = os.path.join(path, photo.name)
        path1 = default_storage.save(pathname, ContentFile(photo.read()))
        pathname2 = os.path.join('static/upload', photo.name).replace('\\', '/')
        mm = Shangp(name=name,Ocategory=id1,Tcategory=id2,bianhao=bianhao,price=pp,keyword=key,text=beizhu,isshow=0)
        mm.save()
        hh = Details(bh=bianhao,path=pathname2)
        hh.save()
    return render(request,'picture_add.html',context={'shuju':shuju})


def Brand_Manage(request):
    num = Shangp.objects.all().aggregate(Count('cid'))
    num = num['cid__count']
    num2 = Shangp.objects.filter(keyword="最家").__len__()
    num3 = num - num2
    shuju = Size.objects.values().all()
    shuju1 = Shangp.objects.values().all()
    xx = request.POST.getlist("xuanzhong")
    for i in xx:
        s = Size.objects.get(sid=i)
        s.delete()
    tt = request.POST.get('aa')
    if tt == "启用":
        id = request.POST.get("xuan")
        pi = Size.objects.get(sid=id)
        pi.zh = 1
        pi.save()
    if tt == "停用":
        id = request.POST.get("xuan")
        pi = Size.objects.get(sid=id)
        pi.zh = 0
        pi.save()
    return render(request,'Brand_Manage.html',context={'shuju':shuju,'shuju1':shuju1,'num':num,'num2':num2,'num3':num3})


def Category_Manage(request):
    shuju = Category.objects.values().all()
    return render(request,'Category_Manage.html',context={'shuju':shuju})


def productadd(request):
    name = request.POST.get("product-category-name")
    order = request.POST.get("parentid")
    cat = request.POST.get("jibie")
    ztt = request.POST.get("chack")
    photo = request.FILES.get("upload")
    if ztt == "增加":
        path = os.path.join(os.getcwd(), 'static\\upload')
        pathname = os.path.join(path, photo.name)
        path1 = default_storage.save(pathname, ContentFile(photo.read()))
        pathname2 = os.path.join('static/upload', photo.name).replace('\\', '/')
        c = Category(oname=name,cate=cat,path=pathname2,parentid=order)
        c.save()
    if ztt == "禁用":
        c = Category.objects.get(oname=name)
        c.zt = 0
        c.save()
    if ztt == "删除":
        c = Category.objects.get(oname=name)
        c.delete()

    return render(request,'product-category-add.html')


def advertising(request):
    num = Ad.objects.all().aggregate(Count('aid'))
    num = num['aid__count']
    order = request.POST.get("排序")
    link = request.POST.get("地址")
    state = request.POST.get("form-field-radio1")
    photo = request.FILES.get("upload")
    time = datetime.datetime.now()
    xd = request.POST.getlist("check_box_list")
    for id in xd:
        pi = Ad.objects.get(aid=id)
        pi.delete()

    if photo:
        path = os.path.join(os.getcwd(), 'static\\upload')
        pathname = os.path.join(path, photo.name)
        path1 = default_storage.save(pathname,ContentFile(photo.read()))
        pathname2 = os.path.join('static/upload', photo.name).replace('\\', '/')
        u1 = Ad(path=pathname2,order=order,link=link,state=state,time=time)
        u1.save()
    shuju = Ad.objects.values().all()
    tt = request.POST.get("aa")
    norder = request.POST.get("norder")
    if tt == "显示":
        id = request.POST.get("xuan")
        pi = Ad.objects.get(aid=id)
        pi.state = 1
        pi.save()
    if tt == "隐藏":
        id = request.POST.get("xuan")
        pi = Ad.objects.get(aid=id)
        pi.state = 0
        pi.save()
    if tt == "修改":
        id = request.POST.get("xuan")
        pi = Ad.objects.get(aid=id)
        pi.order = norder
        pi.save()
    return render(request,'advertising.html',context={'shuju':shuju,'num':num})


def Sort_ads(request):
    return render(request,'Sort_ads.html')


def transaction(request):
    ding = Order.objects.values().all()
    money = Order.objects.aggregate(Sum('much'))
    money = money['much__sum']   #订单总金额
    num = Order.objects.aggregate(Count('oid'))
    num = num['oid__count']   #订单总数
    num1 = Order.objects.filter(orderState=2).__len__() #交易成功
    num2 = Order.objects.filter(orderState=3).__len__() #交易失败
    bun = Order.objects.filter(orderState=3).aggregate(Sum('much'))
    bun = bun['much__sum']  #退款金额
    return render(request,'transaction.html',context={'money':money,'num':num,'num1':num1,'num2':num2,'bun':bun})


def Orderform(request):
    num = Order.objects.all().aggregate(Count('oid'))
    num = num['oid__count']
    shuju = Order.objects.values().all()
    shuju1 = Xiang.objects.values().all()
    shuju2 = Shangp.objects.values().all()
    shuju3 = User.objects.values().all()
    return render(request,'Orderform.html',context={'num':num,"shuju":shuju,"shuju1":shuju1,"shuju2":shuju2,"shuju3":shuju3})


def Amounts(request):
    return render(request,'Amounts.html')

def member_Grading(request):
    shuju = User.objects.values().all()
    num = User.objects.all().aggregate(Count('uid'))
    num = num['uid__count']
    num1 = User.objects.all().filter(gold__lt=100).count()
    num2 = User.objects.all().filter(gold__gt=100,gold__lt=400).count()
    num3 = User.objects.all().filter(gold__gt=400,gold__lt=1000).count()
    num4 = User.objects.all().filter(gold__gt=1000,gold__lt=2000).count()
    num5 = User.objects.all().filter(gold__gt=2000,gold__lt=5000).count()
    num6 = User.objects.all().filter(gold__gt=10000).count()
    if request.method == 'POST':

        tt = request.POST.get('aa')
        if tt == "修改":
            id = request.POST.get("check")
            gg = request.POST.get("norder"+id)
            print(gg)
            pi = User.objects.get(uid=id)
            print(pi)
            pi.gold = gg
            pi.save()
    return render(request,'member_Grading.html',context={'shuju':shuju,'num':num,'num1':num1,'num2':num2,'num3':num3,'num4':num4,'num5':num5,'num6':num6,})


def user_list(request):
    num = User.objects.all().aggregate(Count('uid'))
    num = num['uid__count']
    shuju = User.objects.values().all()
    name = request.POST.get("用户名")
    word = request.POST.get("用户密码")
    rname = request.POST.get("真实姓名")
    sex = request.POST.get("form-field-radio")
    iphpne = request.POST.get("移动电话")
    email = request.POST.get("电子邮箱")
    islog = request.POST.get("form-field-radio1")
    if name:
        u1 = User(username=name,password=word,Realname=rname,sex=sex,phone=iphpne,email=email,islog=islog)
        u1.save()
    xd = request.POST.getlist("check_box_list")
    for id in xd:
        u = User.objects.get(uid=id)
        u.delete()
    tt = request.POST.get('aa')
    if tt == "启用":
        id = request.POST.get("xuan")
        pi = User.objects.get(uid=id)
        pi.islog = 1
        pi.save()
    if tt == "停用":
        id = request.POST.get("xuan")
        pi = User.objects.get(uid=id)
        pi.islog = 0
        pi.save()

    return render(request,'user_list.html',context={'shuju':shuju,'num':num})


def integration(request):
    num = track.objects.all().aggregate(Count('tid'))
    num = num['tid__count']
    jilu = track.objects.values().all()
    didan = Order.objects.values().all()
    shuju = User.objects.values().all()
    return render(request,'integration.html',context={'jilu':jilu,'shuju':shuju,'num':num,'didan':didan})


def Guestbook(request):
    shuju = Eval.objects.values().all()
    shuju1 = User.objects.values().all()
    num = Eval.objects.all().aggregate(Count('eid'))
    num = num['eid__count']
    xd = request.POST.getlist("xuan")
    for id in xd:
        e = Eval.objects.get(eid=id)
        e.delete()
    tt = request.POST.get('aa')
    if tt == "已浏览":
        id = request.POST.get("xuanze")
        pi = Eval.objects.get(eid=id)
        pi.isli = 1
        pi.save()
    if request.POST:
        huifu = request.POST.get('huifu')
        id = request.POST.get("xuanze")
        if id:
            en = User.objects.get(uid=id)
            email = en.email
            youjian(email, huifu)
    return render(request,'Guestbook.html',context={'shuju':shuju,'shuju1':shuju1,'num':num})


def Feedback(request):
    num = Eval.objects.filter(tt=2).all().aggregate(Count('eid'))
    num = num['eid__count']
    shuju = Eval.objects.filter(tt=2).values().all()
    shuju1 = User.objects.values().all()
    if request.method == 'POST':
        tt = request.POST.get('aa')
        if tt == "已浏览":
            id = request.POST.get("xuanze")
            pi = Eval.objects.get(eid=id)
            ll = pi.eid
            print(ll)
            pi.isli = 1
            pi.save()
        hh = request.POST.get('hh')
        zh = request.POST.get("删除")
        if zh == "删除":
            de = Eval.objects.get(eid=hh)
            de.delete()
        huifu = request.POST.get('huifu')
        id = request.POST.get("xuanze")
        if id:
            en = User.objects.get(uid=id)
            email = en.email
            youjian(email,huifu)

    return render(request,'Feedback.html',context={'shuju':shuju,'shuju1':shuju1,'num':num })


def Systems(request):
    if request.method == "POST":
        name = request.POST.get("wzna")
        photo = request.FILES.get("photo")
        keyword = request.POST.get("key")
        pa = request.POST.get("path")
        mi = request.POST.get("neirong")
        ban = request.POST.get("banquan")
        bei = request.POST.get("beian")
        if photo:
            path = os.path.join(os.getcwd(), 'static\\upload')
            pathname = os.path.join(path, photo.name)
            path1 = default_storage.save(pathname, ContentFile(photo.read()))
            pathname2 = os.path.join('static/upload', photo.name).replace('\\', '/')
            ss = System(name=name,path=pathname2,keyword=keyword,filepath=pa,nei=mi,ban=ban,bei=bei)
            ss.save()
    return render(request,'Systems.html')


def admin_Competence(request):
    shuju = Manage.objects.values().all()
    id = request.POST.get("id")
    ty = request.POST.get("xiugai")


    if request.method == 'POST':
        mm = Manage.objects.get(mid=id)
        mm.type = ty
        mm.save()

    return render(request,'admin_Competence.html',context={'shuju':shuju})


def administrator(request):
    num = Manage.objects.all().aggregate(Count('mid'))
    ss = Manage.objects.all().filter(type=1).count()
    ss2 = Manage.objects.all().filter(type=0).count()
    num = num['mid__count']
    shuju = Manage.objects.values().all()
    uname = request.POST.get("user-name")
    upassword = request.POST.get("userpassword")
    upassword2 = request.POST.get("newpassword2")
    usex = request.POST.get("form-field-radio")
    uiphone = request.POST.get("user-tel")
    uemil = request.POST.get("email")
    uxx = str(request.POST.get("text"))
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    utime = date + ' '+ time
    name11 = request.session.get('key')
    if uname and upassword and uxx:
        if upassword == upassword2:
            m1 = Manage(managername=uname,managerpassword=upassword,sex=usex,iphone=uiphone,email=uemil,xinxi=uxx,time=utime,type=0)
            m1.save()
    xd = request.POST.getlist("check_box_list")
    for id in xd:
        u = Manage.objects.get(mid=id)
        u.delete()
    tt = request.POST.get('aa')
    if tt == "启用":
        id = request.POST.get("xuan")
        pi = Manage.objects.get(mid=id)
        pi.istu = 1
        pi.save()
    if tt == "停用":
        id = request.POST.get("xuan")
        pi = Manage.objects.get(mid=id)
        pi.istu = 0
        pi.save()
    return render(request,'administrator.html',context={'shuju':shuju,'num':num,'name11':name11,'ss':ss,'ss2':ss2})


def admin_info(request):
    mm = request.session.get('key')
    shuju1 = Mdelu.objects.values().all()
    shuju = Manage.objects.get(managername=mm)
    name = shuju.managername
    t = shuju.type
    if t == 1:
        t = '超级无敌管理员'
    elif t == 0:
        t = '管理员'
    elif t == 2:
        t = '低级管理员'
    sex =shuju.sex
    old = shuju.old
    iphone = shuju.iphone
    email = shuju.email
    qq = shuju.qq
    time = shuju.time
    if sex == '0':
        sex = '保密'
    if sex == '1':
        sex = '男'
    if sex == '2':
        sex = '女'
    nm = request.POST.get('用户名')
    if nm:
        shuju.managername = nm
        shuju.save()
    xb = request.POST.get('form-field-radio')
    if xb:
        shuju.sex = xb
        shuju.save()
    nl = request.POST.get('年龄')
    if nl:
        shuju.old = nl
        shuju.save()
    dh = request.POST.get('移动电话')
    if dh:
        shuju.iphone = dh
        shuju.save()
    yj = request.POST.get('电子邮件')
    if yj:
        shuju.email = yj
        shuju.save()
    q = request.POST.get('QQ')
    if q:
        shuju.qq = q
        shuju.save()
    word = request.POST.get('原密码')
    if word == shuju.managerpassword:
        new = request.POST.get("新密码")
        new2 = request.POST.get("再次确认密码")
        if new == new2:
            shuju.managerpassword = new
            shuju.save()
        else:
            flag = 2
    else:
        flag = 1
    return render(request,'admin_info.html',context={'shuju1':shuju1,'name':name,'sex':sex,'old':old,'iphone':iphone,'email':email,'qq':qq,'time':time,'t':t,'flag':flag})


def login(request):
    name = request.POST.get('username')
    word = request.POST.get('password')
    shuju = Manage.objects.values()
    mm = shuju.values()
    hh = mm.values('managername')
    aa = {'managername':name}
    print(hh)
    if aa in hh:
        l = Manage.objects.get(managername=name)
        uname = l.managername
        uword = l.managerpassword
        if name == uname and word == uword:
            n = Manage.objects.filter(managername=name).get()
            id = n.mid
            mdelu = Mdelu()
            mdelu.mid = id
            mdelu.name = name
            ip = request.META['REMOTE_ADDR']
            mdelu.ip = ip
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            time = datetime.datetime.now().strftime('%H:%M:%S')
            mdelu.time = str(date) + ' '+str(time)
            mdelu.save()
            request.session['key'] = name
            return redirect('index')
        return render(request, 'login.html')
    else:
        return render(request,'login.html')


def Order_handling(request):
    num = Order.objects.all().aggregate(Count('oid'))
    num = num['oid__count']
    shuju = Order.objects.values().all()
    shuju1 =Xiang.objects.values().all()
    shuju2 = Shangp.objects.values().all()
    shuju3 = User.objects.values().all()

    if request.method == "POST":
        zz = request.POST.get("mmmm")
        if zz == "提交":
            kuai = request.POST.get("kuai")
            hao = request.POST.get('hao')
            fu = request.POST.get("checkbox")
            id = request.POST.get('xuan')
            pi = Order.objects.get(oid=id)
            pi.orderState = 1
            pi.kuainame = kuai
            pi.kuai = hao
            pi.isfu = fu
            pi.save()
        if zz == "xiang":
            id = request.POST.get('xuan')
            request.session['chuan'] = id
            mm = request.session.get("chuan")

    return render(request,'Order_handling.html',context={'shuju':shuju,'shuju1':shuju1,'shuju2':shuju2,'num':num,'shuju3':shuju3})


def order_detailed(request,id):
    shuju = Order.objects.get(oid=id)
    shuju2 = Xiang.objects.filter(oid=id).values().all()
    shuju3 = Shangp.objects.values().all()
    shuju4 = Details.objects.values().all()
    shuju5 = Address.objects.values().all()
    return render(request,'order_detailed.html',context={'shuju':shuju,'shuju2':shuju2,'shuju3':shuju3,'shuju4':shuju4,'shuju5':shuju5})


def member_show(request):
    return render(request,'member_show.html')


def Cover_management(request):
    return render(request,'Cover_management.html')


def Competence(request):
    return render(request,'Competence.html')


def Brand_detailed(request):
    return render(request,'Brand_detailed.html')


def Ads_list(request):
    return render(request,'Ads_list.html')


def Add_Brand(request):
    if request.method == 'POST':
        shid = request.POST.get("shangpin")
        xid = request.POST.get("xinghao")
        photo = request.FILES.get("photo")
        xn = request.POST.get("xname")
        if photo:
            path = os.path.join(os.getcwd(), 'static\\upload')
            pathname = os.path.join(path, photo.name)
            path1 = default_storage.save(pathname, ContentFile(photo.read()))
            pathname2 = os.path.join('static/upload', photo.name).replace('\\', '/')
            s = Size(gid=shid,md=xid,path=pathname2,xname=xn)
            s.save()
        sh = request.POST.get("sh")
        photo2 = request.POST.get("photo2")
        if photo2:
            path = os.path.join(os.getcwd(), 'static\\upload')
            pathname = os.path.join(path, photo2.name)
            path1 = default_storage.save(pathname, ContentFile(photo2.read()))
            pathname2 = os.path.join('static/upload', photo2.name).replace('\\', '/')
            dd = Details(bh=sh,path=pathname2)
            dd.save()
    return render(request,'Add_Brand.html')


def Feedback_2(request):
    num = Eval.objects.filter(tt=0).all().aggregate(Count('eid'))
    num = num['eid__count']
    shuju = Eval.objects.filter(tt=0).values().all()
    shuju1 = User.objects.values().all()
    if request.method == 'POST':
        tt = request.POST.get('aa')
        if tt == "已浏览":
            id = request.POST.get("xuanze")
            pi = Eval.objects.get(eid=id)
            pi.isli = 1
            pi.save()
        hh = request.POST.get('hh')
        zh = request.POST.get("删除")
        if zh == "删除":
            de = Eval.objects.get(eid=hh)
            de.delete()
        huifu = request.POST.get('huifu')
        id = request.POST.get("xuanze")
        if id:
            en = User.objects.get(uid=id)
            email = en.email
            youjian(email, huifu)

    return render(request, 'Feedback_2.html', context={'shuju': shuju, 'shuju1': shuju1, 'num': num})