from django.shortcuts import render
from board_cert.models import Board_member_details, Board_Certificate
from PIL import Image, ImageDraw, ImageFont
import base64
from io import BytesIO
from django.http import HttpResponse, FileResponse
import img2pdf
import pyqrcode 
# Create your views here.

def generate_board_certificate(request, slug):
    if request.method=='GET':
        board_data = Board_member_details.objects.get(slug=slug)
        board_certificate_data = Board_Certificate.objects.get(id=board_data.Event_Name_id)
        im = Image.open(board_certificate_data.image)
        d = ImageDraw.Draw(im)
        board_name_location = (board_certificate_data.board_name_location_x, board_certificate_data.board_name_location_y)
        designation_name_location = (board_certificate_data.boardposition_name_location_x, board_certificate_data.boardposition_name_location_y)
        text_color = (board_certificate_data.text_color_R, board_certificate_data.text_color_G, board_certificate_data.text_color_B)
        font = ImageFont.truetype(board_certificate_data.font_type, board_certificate_data.font_size)
        d.text(board_name_location, board_data.Full_Name, fill=text_color, font=font)
        d.text(designation_name_location, board_certificate_data.Event_Name, fill=text_color, font=font)
        url = pyqrcode.QRCode("http://127.0.0.1:8000/get_data/generate_board_certificate/"+str(slug))
        url.png('test.png', scale=1)
        qr = Image.open('test.png')
        qr = qr.resize((board_certificate_data.qr_code_size_x, board_certificate_data.qr_code_size_y))
        qr = qr.convert("RGBA")
        im = im.convert("RGBA")
        box = (board_certificate_data.qr_code_position_x, board_certificate_data.qr_code_position_y)
        #qr.crop(box)
        #region = im
        print(im)
        print(qr)
        im.paste(qr, box)
        #im.show()
        response = HttpResponse(content_type='image/png')
        im.save(response, "PNG")
        return response

def display_board_certificate(request, slug):
    if request.method=='GET':
        board_data = Board_member_details.objects.get(slug=slug)
        board_certificate_data = Board_Certificate.objects.get(id=board_data.Event_Name_id)
        return render(request, 'view_board_certificate.html', {"slug":slug})