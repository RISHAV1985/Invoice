from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas  

# Create your views here.
def home(request):
    return render(request,'home.html')

def add(request):
     
    val1=int(request.POST["prod"])
    val2=int(request.POST["amount"])
    res=val1 * val2
    return render(request,"result.html", {'result':res})

def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return render(request,'result.html')