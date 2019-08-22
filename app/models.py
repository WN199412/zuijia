import datetime
from django.db import models

# Create your models here.
#用户列表
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=60)
    Realname = models.CharField(max_length=60)  #真实姓名
    password = models.CharField(max_length=32)
    type = models.IntegerField(default=0)#用户类型  0 普通 1 管理员
    email = models.CharField(max_length=30)
    sex = models.IntegerField(default=0) #0男  1女
    birthday = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    city = models.CharField(max_length=60,null=True)
    regtime = models.DateTimeField(default=datetime.datetime.now())  #注册时间
    # level = models.CharField(default='青铜',max_length=60) # 用户等级： 青铜 白银 黄金 钻石 王者
    regip = models.CharField(max_length=30)#注册ip
    logip = models.CharField(max_length=30)#登陆ip
    gold = models.IntegerField(default=10)#用户积分
    islog = models.IntegerField(default=1)#是否允许登陆  0 不允许
    lcon = models.CharField(default=0,max_length=200)#头像

    class Meta:
        db_table = 'user'

#管理员列表
class Manage(models.Model):
    mid = models.AutoField(primary_key=True)
    managername = models.CharField(max_length=30)
    managerpassword = models.CharField(max_length=30)
    sex = models.CharField(max_length=10,default=0,null=True)# 0保密 1 男 2 女
    type = models.IntegerField(default=0)  # 0 普通管理员 1 超级管理员
    old = models.CharField(max_length=10,default=0)
    iphone = models.CharField(max_length=30,default=0,null=True)
    email = models.CharField(max_length=30,null=True)
    qq = models.CharField(max_length=20,null=True)
    time = models.CharField(max_length=30,default=datetime.datetime.now())   #注册时间
    xinxi = models.CharField(max_length=500,null=True)  #备注信息
    istu = models.IntegerField(default=1)  #是否启用

    class Meta:
        db_table = 'manage'

# 订单列表
class Order(models.Model):
    oid = models.AutoField(primary_key=True)  #订单id
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)#用户id
    sid = models.IntegerField(null=True)#商品id
    orderid = models.IntegerField(null=True)#订单号
    much = models.IntegerField(null=True)#订单金额
    orderDate = models.CharField(max_length=30,null=True)#下单时间
    orderState = models.IntegerField(default=0,null=True)# 订单是否处理 1 处理  0 未处理 2 交易成功 3 交易失败
    kuainame = models.CharField(max_length=20,null=True)  #快递名称
    kuai = models.IntegerField(default=0)   #快递单号
    isfu = models.IntegerField(default=0)   #是否货到付款
    class Meta:
        db_table = 'order'

#订单所购买的商品表
class Xiang(models.Model):
    xid = models.AutoField(primary_key=True)
    oid = models.IntegerField(default=0)   #订单id
    sid = models.IntegerField(default=0)  #商品id

    class Meta:
        db_table = 'xiang'


#管理员登陆记录
class Mdelu(models.Model):
    id = models.AutoField(primary_key=True)
    mid = models.IntegerField(default=0,null=True)
    name = models.CharField(max_length=20,null=True)
    ip = models.CharField(max_length=20,null=True)
    time = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = 'mdelu'
#广告列表
class Ad(models.Model):
    aid = models.AutoField(primary_key=True)
    path = models.CharField(max_length=100)  #图片的路径
    link = models.CharField(max_length=50,null=True)  #链接
    order = models.IntegerField(default=0)  #显示顺序
    state = models.IntegerField(default=1)  #是否显示图片
    time = models.DateTimeField(max_length=100)

    class Meta:
        db_table = 'ad'

#收藏表
class Collection(models.Model):
    cid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #用户id
    gid = models.IntegerField() #商品id
    time = models.DateTimeField(max_length=100) #加入时间

    class Meta:
        db_table = 'collection'

#商品表
class Shangp(models.Model):
    cid = models.AutoField(primary_key=True)
    Ocategory = models.IntegerField(default=0) #商品一级分类
    Tcategory = models.IntegerField(default=0) #商品二级分类
    Scategory = models.IntegerField(default=0) #商品的三级分类
    name = models.CharField(max_length=100) #商品名称
    keyword = models.CharField(max_length=100)  #商品关键字
    bianhao = models.IntegerField(default=0)  #商品编号
    text = models.CharField(max_length=300) #商品简介
    price = models.FloatField(default=0) #商品的价格
    isshow = models.IntegerField(default=1) #是否展示
    number = models.IntegerField(default=0)  #商品数量
    soldnum = models.IntegerField(default=0)  #卖出数量
    llan = models.IntegerField(default=0) #商品浏览次数
    time = models.DateTimeField(default=datetime.datetime.now())
    path = models.CharField(max_length=50,default=0)  #图片路径

    class Meta:
        db_table = 'shangp'

#类别
class Category(models.Model):
    oid = models.AutoField(primary_key=True)
    oname = models.CharField(max_length=30) #名称
    cate = models.IntegerField(default=0) # 1 一级类别  2 二级类别 3 三级类别
    parentid = models.IntegerField(default=0)  #  父id
    zt = models.IntegerField(default=1)  #是否显示  1 显示  0  不显示
    path = models.CharField(max_length=100) #图片路径

    class Meta:
        db_table = 'goods'

#商品型号表
class Size(models.Model):
    sid = models.AutoField(primary_key=True)
    gid = models.IntegerField(default=0)  # 商品id
    md = models.IntegerField(default=0) #分类id
    xname = models.CharField(max_length=50,null=True) #型号名字
    path = models.CharField(max_length=100) #图片路径
    zh = models.IntegerField(default=1)  #是都启用  1 启用  0 禁用

    class Meta:
        db_table = 'size'

#商品展示图片表
class Details(models.Model):
    id = models.AutoField(primary_key=True)
    bh = models.IntegerField(default=0)  # 商品id
    path = models.CharField(max_length=100)  # 图片路径

    class Meta:
        db_table = 'details'
#订单地址表
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)  #用户id
    aname = models.CharField(max_length=15)  #姓名
    iphone = models.CharField(max_length=15)  #收件电话
    pro = models.CharField(max_length=30)  #地址省份
    city = models.CharField(max_length=30)  #城市
    area = models.CharField(max_length=30)   #区县
    disarea = models.CharField(max_length=30)  #配送区域
    detaddress = models.CharField(max_length=100)  #详细地址
    zipcode = models.IntegerField(default=0)  #邮政编码
    time = models.DateTimeField(max_length=30)  #添加时间
    isdef = models.IntegerField(default=1) #是否是默认地址  0 否 1 是

    class Meta:
        db_table = 'address'

#购物车列表
class Shopping(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #用户id
    cid = models.IntegerField(default=0)  #商品id
    sid = models.IntegerField(default=0)  #商品型号id
    time = models.DateTimeField(max_length=30)  #加入时间
    number = models.IntegerField(default=0)  #商品的件数

    class Meta:
        db_table = 'shopping'

#用户登陆记录表
class Log(models.Model):
    logid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30) #登陆的用户名
    logip = models.CharField(max_length=30) #登陆的ip地址
    time = models.DateTimeField(max_length=30) #登陆的时间

    class Meta:
        db_table = 'log'


#用户浏览记录
class track(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)  #用户 id
    sname = models.CharField(max_length=30,null=True)  #商品名称
    llan = models.IntegerField(default=0)  #商品的浏览次数
    time = models.DateTimeField(max_length=50)  #浏览时间

    class Meta:
        db_table = 'track'

#评价列表
class Eval(models.Model):
    eid = models.AutoField(primary_key=True)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,null=True)  #用户id
    sid = models.IntegerField(default=0) #评价商品的id
    text = models.CharField(max_length=500,null=True)# 评价内容
    path = models.CharField(max_length=50)  #评论图片的路径
    time = models.DateTimeField(max_length=30,null=True)  #评价的时间
    isli = models.IntegerField(default=0)  #是否浏览  0  为浏览   1  已经浏览
    tt = models.IntegerField(default=0)  #  0评论  1 回复 2投诉

    class Meta:
        db_table = 'eval'

#系统设置
class System(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,null=True)  #网站名称
    path = models.CharField(max_length=30,null=True)  #网站logo图片路径
    keyword = models.CharField(max_length=50,null=True)  #关键词
    filepath = models.CharField(max_length=50,null=True)  #文件的额路径
    nei = models.CharField(max_length=300,null=True)  #描述
    ban = models.CharField(max_length=100,null=True)   #底部版权
    bei = models.CharField(max_length=100,null=True)   #备案号

    class Meta:
        db_table = 'system'






