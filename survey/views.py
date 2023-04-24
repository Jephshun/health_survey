from django.shortcuts import render
from .forms import MyForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.
def index(request):
    #collect form data
    if request.method == 'POST':
       generate_pdf(request.POST)
    return render(request,'survey/index.html')

def generate_pdf(pdf_data):
    c = canvas.Canvas('test.pdf')
    c.drawString(100,50, f"7. Does your current solution adhere to the Data Protection act? {pdf_data['q4']}")
    c.drawString(100,40, f"8. What are the challenges you currently face with your existing offering or method(s) of managing your facilities data? {pdf_data['challenges']}")

    c.showPage()
    c.save()
    return HttpResponse("Hello")

# generate_pdf(c)

