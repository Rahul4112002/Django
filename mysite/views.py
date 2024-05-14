from django.shortcuts import render , redirect
from django.http import HttpResponseRedirect,HttpResponse
from features.models import Features
def homePage(request):
    featuresData = Features.objects.all()
    if request.method == 'GET':
        ft = request.GET.get('featurename')
        if ft != None:
            featuresData = Features.objects.filter(feature_title__icontains= ft)
    data = {
        'featuresData': featuresData,
        'ft' : ft,
    }
    return render(request,'index.html',data)

def team(request):
    return render(request,'team.html')

def contact(request):
    try:
        if request.method == 'POST':
            fname = request.POST.get('first-name'),
            lname = request.POST.get('last-name')
            return HttpResponseRedirect('/')
    except:
        pass
    return render(request,'contact.html')

def submitform(request):
    return HttpResponse(request)
    
def calculator(request):
    data = {}
    try:
        c=''
        if request.method=='POST':
            n1 = eval(request.POST.get('first-number'))
            n2 = eval(request.POST.get('second-number'))
            opr = request.POST.get('operations')
            if opr == '+':
                c = n1+n2
            elif opr == '-':
                c = n1-n2
            elif opr == '*':
                c = n1*n2
            elif opr == '/':
                c = n1/n2
            data = {
                'n1' : n1,
                'n2' : n2,
                'c' : c,
            }
        
    except:
        c = 'Invalid Inputs....'
    print(c)
    return render(request,"calculator.html",data)

def marksheet(request):
    data = {}
    try:
        total = ''
        percentage = ''
        grade = ''
        if request.method == 'POST':
            s1 = eval(request.POST.get('subject1'))
            s2 = eval(request.POST.get('subject2'))
            s3 = eval(request.POST.get('subject3'))
            s4 = eval(request.POST.get('subject4'))
            s5 = eval(request.POST.get('subject5'))
            total = s1+s2+s3+s4+s5
            percentage = (total/500) * 100
            if percentage >= 90:
                grade = "A"
            elif percentage < 90 and percentage >= 80:
                grade = "B"
            elif percentage < 80 and percentage >= 70:
                grade = "C"
            elif percentage < 70 and percentage >= 50:
                grade = 'D'
            else:
                grade = 'Fail' 
            data = {
                's1': s1,
                's2': s2,
                's3': s3,
                's4': s4,
                's5': s5,
                'total': total,
                'percentage': percentage,
                'grade': grade
            }
    except:
        pass
    return render(request,'marksheet.html',data)

def evenodd(request):
    data = {}
    try:
        if request.POST.get('number') == '':
            return render(request,'evenodd.html',{'error' : True})
        ans = ''
        n = eval(request.POST.get('number'))
        if n%2 == 0:
            ans = "EVEN"
        else:
            ans = 'ODD'
        data = {
            'n': n,
            'ans': ans,
        }
    except:
        pass
    return render(request,'evenodd.html',data)