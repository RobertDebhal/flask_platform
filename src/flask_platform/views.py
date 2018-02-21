from flask import render_template
from flask_platform import app
from systeminfo import main as sysinfo

@app.route('/')
def get_systeminfo():
    return "The platform is " + sysinfo.get_platform_info()