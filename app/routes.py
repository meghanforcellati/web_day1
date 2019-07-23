from flask import render_template, request, redirect
from app import app
from app.models import model, formopener
from app import dicts


birthmonth_dict=dicts.birthmonth_dict
birthmonth_img=dicts.birthmonth_img
#The dicts file contains all the birthmonths/image url's. 

@app.route('/birthStone', methods=['GETS', 'POST'])
def birthStone():
    if request.method=='GET':
        return "You're at the wrong page."
    else:
        userdata=request.form
        birthmonth=userdata['birthmonth'].lower().strip()
        if birthmonth in birthmonth_dict:
            return render_template('results.html', birthmonth=userdata['birthmonth'], birthstone=birthmonth_dict[birthmonth], imsr=birthmonth_img[birthmonth])
        else:
            return render_template('results.html', birthmonth="INVALID", 
            birthstone="INVALID", imsr="")

#about pg is the main page 
@app.route('/about')
def about():
    return render_template('about.html')

#index is the page where you go for the birthstone form. 
@app.route('/index')
def index():
    return render_template('index.html')
