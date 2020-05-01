from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.db.models import Q
from .forms import 自定义注册表单
from .models import 普通会员表
from HomeworkPublish.models import Homework
from upload.models import userfile
from .models import course
from .models import stucourse
from .models import asscourse
# Create your views here.

def 主页(request):
    if request.user.is_authenticated:
        mycourse=course.objects.filter(teacherName = request.user.username)
        sc = stucourse.objects.filter(studentName = request.user.username)
        ac = asscourse.objects.filter(assistantName = request.user.username)
        hw=Homework.objects.all()
        uf=userfile.objects.all()
        us=普通会员表.objects.all()
        nowu=普通会员表.objects.get(昵称 = request.user.username)
        request.session['role']=nowu.身份
        context={'hw':hw,'uf':uf,'us':us,'mycourse':mycourse,'sc':sc,'ac':ac}
        return render(request, 'Login/home.html',context)
    else:
        return render(request,'Login/home.html')



def 登录(request):
    if request.method == 'POST':
        用户 = authenticate(request,username=request.POST['用户名'] ,password=request.POST['密码'] )
        if 用户 is None:
            return render(request, 'Login/login.html',{'错误':'该用户名不存在或密码错误!'})
        else:
            login(request,用户)
            return redirect('Login:主页')
            
    else:
        return render(request, 'Login/login.html')


def 登出(request):
    try:
        del request.session['role']
    except KeyError:
        pass
    logout(request)
    return redirect('Login:主页')


def 注册(require):
    if require.method == 'POST':
        注册表单 = 自定义注册表单(require.POST)
        if 注册表单.is_valid():
            注册表单.save()
            用户 = authenticate(username=注册表单.cleaned_data['username'] ,password=注册表单.cleaned_data['password1'] )
            用户.email = 注册表单.cleaned_data['email']
            普通会员表(用户=用户,昵称=注册表单.cleaned_data['昵称'],身份=注册表单.cleaned_data['身份']).save()
            login(require,用户)
            return redirect('Login:主页')
    else:
        注册表单 = 自定义注册表单()

    内容 = {'注册表单':注册表单}
    return render(require, 'Login/register.html', 内容)


def upload(request,id):
    uf=userfile()
    if request.method == "POST":
        uf.username = request.user.username
        uf.courseNum = id
        uf.headImg = request.FILES.get('tttt',None)
        uf.save()
        return HttpResponse('upload ok!')
    return render(request,'Login/upload.html',{'uf':uf})

def addcourse(request):
    Nowcourse = course()
    if request.method == "POST":
        Nowcourse.teacherName = request.user.username
        Nowcourse.courseNum = request.POST['courseNum']
        Nowcourse.courseName = request.POST['courseName']
        Nowcourse.save()
        return HttpResponse('添加成功')
    return render(request,'Login/addcourse.html',{'Nowcourse':Nowcourse})

def joincourse(request):
    search = request.GET.get('search')
    if search:
        target = course.objects.filter(
            Q(courseNum__icontains=search)
        )
    else:
        search=''
        target =  course.objects.all()
    join = request.GET.get('join')
    if join:
        joinCourse = stucourse()
        joinCourse.studentName = request.user.username
        joinCourse.thecourse = target[0]
        joinCourse.save()
    context = {'search':search,'target':target}
    return render(request,"Login/joincourse.html",context)


def coursedetail(request,id):
    mycourse=course.objects.get(id = id)
    sc = stucourse.objects.filter( thecourse_id = id)
    hw=Homework.objects.filter(courseNum = id)
    context = {'mycourse':mycourse,'sc':sc,'hw':hw}
    return render(request,'Login/coursedetail.html',context)

def coursedelete(request,id):
    target = course.objects.get(id=id)
    target.delete()
    return HttpResponse("已删除课程")

def addassistant(request,id):
    assistant = asscourse()
    Course = course.objects.get(id=id)
    if request.method == "POST":
        assistant.assistantName = request.POST['assistantName']
        assistant.thecourse = Course
        assistant.save()
        return HttpResponse('添加成功')
    return render(request,'Login/addassistant.html',{'Course':Course})

