from django.shortcuts import render
from upload_data.models import ParticipantData, Certificate
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
from django.http import HttpResponse
# Create your views here.

def generate_certificate(request, id):
    if request.method=='GET':
        user_data = ParticipantData.objects.get(id=id)
    
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
        response = HttpResponse(content_type='image/png')
        im.save(response, "PNG")

        return response

def display_certificate(request, id):
    if request.method=='GET':
        user_data = ParticipantData.objects.get(id=id)
    
        #print(user_data.Full_Name)
        #print(user_data.Event_Name)
        certificate_data = Certificate.objects.get(id=user_data.Event_Name_id)
        return render(request, 'view_certificate.html', {"id":id})
