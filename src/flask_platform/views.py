from flask_platform import app
import systeminfo as sysinfo

@app.route('/')
def get_systeminfo():
    return "The platform is " + sysinfo.get_platform_info()