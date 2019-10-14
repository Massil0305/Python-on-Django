from django.shortcuts import render

import sys
from subprocess import run,PIPE


def button(request):
    import requests	
    return render(request, 'home.html')

def output(request):
    import requests
    data=requests.get("http://www.oracle.com")
    print(data.text)
    data=data.text
    return render(request, 'home.html',{'data':data})

def external(request):
    import requests
    inp= request.POST.get('param')
    out= run([sys.executable,'number-2-words.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request, 'home.html',{'data1':out.stdout})
