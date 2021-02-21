from django.shortcuts import render
from upload_data.models import ParticipantData, Certificate
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
from django.http import HttpResponse, FileResponse
import img2pdf
import pyqrcode
#import qrcode
# Create cyour views here.

def generate_certificate(request, slug):
    if request.method=='GET':
        user_data = ParticipantData.objects.get(slug=slug)
    
        #print(user_data.Full_Name)
        #print(user_data.Event_Name)
        certificate_data = Certificate.objects.get(id=user_data.Event_Name_id)
        #print(certificate_data.image)
        im = Image.open(certificate_data.image)
        d = ImageDraw.Draw(im)
        location = (100, 398)
        text_color = (0, 137, 209)
        font = ImageFont.truetype("arial.ttf", 120)
        d.text(location, user_data.Full_Name, fill=text_color, font=font)
        url = pyqrcode.QRCode("http://127.0.0.1:8000/get_data/generate_certificate/"+str(slug))
        url.png('test.png', scale=5)
        qr = Image.open('test.png')
        qr = qr.convert("RGBA")
        im = im.convert("RGBA")
        box = (0, 0, 265, 265)
        #qr.crop(box)
        #region = im
        print(im)
        print(qr)
        im.paste(qr, box)
        #im.show()
        response = HttpResponse(content_type='image/png')
        im.save(response, "PNG")
        return response

def convert_certificate_to_pdf(request, slug):
     if request.method=='GET':
        user_data = ParticipantData.objects.get(slug=slug)
    
        #print(user_data.Full_Name)
        #print(user_data.Event_Name)
        certificate_data = Certificate.objects.get(id=user_data.Event_Name_id)
        #print(certificate_data.image)
        im = Image.open(certificate_data.image)
        #print(im)
        d = ImageDraw.Draw(im)
        location = (100, 398)
        text_color = (0, 137, 209)
        font = ImageFont.truetype("arial.ttf", 120)
        d.text(location, user_data.Full_Name, fill=text_color, font=font)
        Imgfile = im.convert("RGB")
        #pdf_bytes = img2pdf.convert(im)
        #print(pdf_bytes)
        #response = HttpResponse(content_type='application/pdf')
        #response['Content-Disposition'] = 'inline; filename=' + str(user_data.Full_Name) + '.pdf'
        
        img_bytes = BytesIO()
        Imgfile.save(img_bytes, "PDF")
        img_bytes = img_bytes.getvalue()
        #print(img_bytes)
        response = HttpResponse(img_bytes , content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=' + str(user_data.Full_Name) + '.pdf'
        
        return response


def display_certificate(request, slug):
    if request.method=='GET':
        user_data = ParticipantData.objects.get(slug=slug)
    
        #print(user_data.Full_Name)
        #print(user_data.Event_Name)
        certificate_data = Certificate.objects.get(id=user_data.Event_Name_id)
        return render(request, 'view_certificate.html', {"slug":slug})
