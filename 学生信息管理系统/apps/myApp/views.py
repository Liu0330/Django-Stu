from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import  Grades

# Create your views here.
from django.http import  HttpResponse
def index(request):
    return render(request, r'myapp/index.html')
def detail(request,num,num2):
    return HttpResponse('detail-%s-%s'%(num,num2))



def grades(request):
    #去模板里取数据
    gradesList = Grades.objects.all()[0:10] #需要限制？？？？？？？？
    #将数据传递给模板,模板再渲染页面，将渲染好的页面返回浏览器
    return render(request,'myapp/grades.html',{"grades":gradesList})
from .models import  Students
def students(request):
    #去模板里取数据
    studentsList = Students.objects.all()[0:10000] #需要限制？？？？？？？？
    #将数据传递给模板,模板再渲染页面，将渲染好的页面返回浏览器
    return render(request,'myapp/students.html',{"students":studentsList})
def gradesStudents(request,num):
    grade= Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request,'myapp/students.html',{'students':studentsList})