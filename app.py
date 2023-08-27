
# coding=utf-8
import sys
import os, shutil
import glob
import re
import numpy as np
import cv2
from flask import jsonify

# Flask utils
from flask import Flask,flash, request, render_template,send_from_directory
from werkzeug.utils import secure_filename


# Define a flask app
app = Flask(__name__, static_url_path='')
app.secret_key = os.urandom(24)

app.config['CARTOON_FOLDER'] = 'cartoon_images'
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/uploads/<filename>')
def upload_img(filename):
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/cartoon_images/<filename>')
def cartoon_img(filename):
    
    return send_from_directory(app.config['CARTOON_FOLDER'], filename)


def cartoonize_2(img):

    # Convert the input image to gray scale 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # stylization of image
    
    return img

def cartoonize_3(img):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image
    
   G = cv2.blur(img,(10,10)) 
   
   return G

def cartoonize_4(img):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image
    
    edges = cv2.Canny(img, 100, 200)
    return edges

def cartoonize_5(img, brightness, contrast):

    out = cv2.addWeighted( img, contrast, img, 0, brightness)

    return out

def cartoonize_6(img):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image
    
    dst = cv2.rotate(img, cv2.ROTATE_180)
    
    return dst

def cartoonize_7(img):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image
    
    dst = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    
    return dst    

def cartoonize_8(img):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image
    
    dst = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    return dst     

def cartoonize_9(img, h, w):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image

    dst = cv2.resize(img, (int(w), int(h)))
    
    return dst       
    

def cartoonize_10(img, vh, hh, vw, hw):

    # Convert the input image to gray scale 
    
    
    # pencil sketch  of image
    
    dst = img[int(vh):int(hh), int(vw):int(hw)]
    
    return dst         


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        f = request.files['file']
        num_tasks = int(request.form.get('num_tasks'))
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        file_name = os.path.basename(file_path)
        img = cv2.imread(file_path)
        final_cartoonized = img.copy()

        for i in range(1, num_tasks + 1):
            style = request.form.get(f'style_task_{i}')
            if style:
                if style == "Style2":
                    final_cartoonized = cartoonize_2(final_cartoonized)
                elif style == "Style3":
                    final_cartoonized = cartoonize_3(final_cartoonized)
                elif style == "Style4":
                    final_cartoonized = cartoonize_4(final_cartoonized)
                elif style == "Style5":
                    brightness = float(request.form.get(f'style_task_{i}_brightness_value'))
                    contrast = float(request.form.get(f'style_task_{i}_contrast_value'))
                    final_cartoonized = cartoonize_5(final_cartoonized, brightness, contrast)
                elif style == "Style6":
                    final_cartoonized = cartoonize_6(final_cartoonized)
                elif style == "Style7":
                    final_cartoonized = cartoonize_7(final_cartoonized)
                elif style == "Style8":
                    final_cartoonized = cartoonize_8(final_cartoonized)
                elif style == "Style9":
                    h = float(request.form.get(f'style_task_{i}_h_value'))
                    w = float(request.form.get(f'style_task_{i}_w_value'))
                    final_cartoonized = cartoonize_9(final_cartoonized, h, w)
                elif style == "Style10":
                    vh = float(request.form.get(f'style_task_{i}_vh_value'))
                    hh = float(request.form.get(f'style_task_{i}_hh_value'))
                    vw = float(request.form.get(f'style_task_{i}_vw_value'))
                    hw = float(request.form.get(f'style_task_{i}_hw_value'))
                    final_cartoonized = cartoonize_10(final_cartoonized, vh, hh, vw, hw)

        final_cartoon_fname = f'{file_name}_final_cartoon.jpg'
        final_cartoon_path = os.path.join(basepath, 'cartoon_images', secure_filename(final_cartoon_fname))
        cv2.imwrite(final_cartoon_path, final_cartoonized)

        return render_template('predict.html', file_name=file_name, final_cartoon_file=os.path.basename(final_cartoon_path))

    return ""


if __name__ == '__main__':
        app.run(debug=True, host="localhost", port=8080)

