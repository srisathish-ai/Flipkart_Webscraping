from flask import Flask, request, render_template,url_for
from bs4 import BeautifulSoup as bs
import requests
import json
from mobileSearch import getMobileHTML
from laptopSearch import getLaptopHTML
from cameraSearch import getCameraHTML
from mobileFilter import mobileSoupToDataframe, brandname, ramsize, Min, Max, sorting
from laptopFilter import laptopSoupToDataframe
from cameraFilter import cameraSoupToDataframe

app = Flask(__name__,template_folder='templates/html')

@app.route('/mobiles',methods=['GET','POST'])
def mobiles():
    global brand,ram
    if request.method == 'POST':
        brand = brandname(request.form.get('brand'))
        ram = ramsize(request.form.get('ramsize'))
        MinBuget = Min(request.form.get('minbudget'))
        MaxBudget = Max(request.form.get('maxbudget'))
        sortBy = sorting(request.form.get('sortby'))
        htmlSourceCode = getMobileHTML(
            brand = brand,
            ram = ram,
            MinBudget = MinBuget,
            MaxBudget = MaxBudget,
            sortBy = sortBy
        )
        soup = bs(htmlSourceCode, 'html.parser')
        data = mobileSoupToDataframe(soup,ishome = False)
        header = ['Products','Prices','Ratings','Reviews','Storage','Display','Camera','ToView']
        return render_template('mobiles.html',headers = header,datas = data)
    else:
        htmlSourceCode = getMobileHTML()
        soup = bs(htmlSourceCode, 'html.parser')
        data = mobileSoupToDataframe(soup,ishome = False)
        header = ['Products','Prices','Ratings','Reviews','Storage','Display','Camera', 'ToView']
        return render_template('mobiles.html',headers = header,datas = data)


@app.route('/laptops',methods=['GET','POST'])
def laptops():
    if request.method == 'POST':
        brand = brandname(request.form.get('brand'))
        lapprocessor = request.form.get('lapprocessor')
        MinBuget = Min(request.form.get('minbudget'))
        MaxBudget = Max(request.form.get('maxbudget'))
        sortBy = sorting(request.form.get('sortby'))
        htmlSourceCode = getLaptopHTML(
            brand = brand,
            lapprocessor = lapprocessor,
            MinBudget = MinBuget,
            MaxBudget = MaxBudget,
            sortBy = sortBy
        )
        soup = bs(htmlSourceCode, 'html.parser')
        data = laptopSoupToDataframe(soup,ishome = False)
        header = ['Products','Prices','Ratings','Reviews','Processor','RAM','OS','ToView']
        return render_template('laptops.html',headers = header,datas = data)
    else:
        htmlSourceCode = getLaptopHTML()
        soup = bs(htmlSourceCode, 'html.parser')
        data = laptopSoupToDataframe(soup,ishome = False)
        header = ['Products','Prices','Ratings','Reviews','Processor','RAM','OS','ToView']
        return render_template('laptops.html',headers = header,datas = data)

@app.route('/camera',methods=['GET','POST'])
def cameras():
    if request.method == 'POST':
        htmlSourceCode = getCameraHTML()
        soup = bs(htmlSourceCode, 'html.parser')
        data = cameraSoupToDataframe(soup,ishome = False)
        header = ['Products','Prices','Ratings','Reviews','Storage','Display','Camera', 'ToView']
        return render_template('camera.html',headers = header,datas = data)
    else:
        htmlSourceCode = getCameraHTML()
        soup = bs(htmlSourceCode, 'html.parser')
        data = cameraSoupToDataframe(soup,ishome = False)
        header = ['Products','Prices','Ratings','Reviews','Pixels','Optical Zoom', 'ToView']
        return render_template('camera.html',headers = header,datas = data)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        MobileHtmlSourceCode = getMobileHTML()
        mob = bs(MobileHtmlSourceCode, 'html.parser')
        mobile = mobileSoupToDataframe(mob,ishome = True)
        mobHeader = ['Products','Prices','Ratings','Reviews','Storage','Display','Camera','ToView']

        LaptopHtmlSourceCode = getLaptopHTML()
        lap = bs(LaptopHtmlSourceCode, 'html.parser')
        laptop = laptopSoupToDataframe(lap, ishome = True)
        lapHeader = ['Products','Prices','Ratings','Reviews','Processor','RAM','OS','ToView']

        CameraHTMLSourceCode = getCameraHTML()
        cam = bs(CameraHTMLSourceCode, 'html.parser')
        camera = cameraSoupToDataframe(cam,ishome = True)
        camHeader = ['Products','Prices','Ratings','Reviews','Pixels','Optical Zoom', 'ToView']

        return render_template(
            'index.html',
            mobheaders = mobHeader,
            mobiles = mobile, 
            lapheaders = lapHeader,
            laptops = laptop,
            cameras = camera,
            camheaders = camHeader)


if __name__=='__main__':
    app.run(debug=True)