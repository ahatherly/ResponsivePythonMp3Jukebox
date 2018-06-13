from flask import Flask, render_template, url_for, send_from_directory, request
import subprocess, time
from filesystem import FSBrowser

application = Flask(__name__)
home_directory = "/media/FreeAgent_Drive/mp3s"
fileBrowser = FSBrowser(home_directory)

@application.route("/")
def index():
    fileBrowser.setPath("")
    return showContents()

@application.route("/browse")
def browse():
    new_path = request.args.get('dir', '')
    fileBrowser.setPath(new_path)
    return showContents()

@application.route("/play")
def play():
    path = request.args.get('dir', '')
    filename = request.args.get('file', '')
    fileBrowser.setPath(path)
    return send_from_directory(fileBrowser.getFullPath(), filename)

def showContents():
    directories = fileBrowser.getDirectories()
    files = fileBrowser.getFiles()
    return render_template('index.html', directories=directories, files=files, path=fileBrowser.getPath(), parent=fileBrowser.getParent())

"""
@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@application.route("/start/<pattern>")
def start(pattern):
    stop()
    subprocess.call(["/home/pi/led-strip-pi/led.sh", "start", pattern])
    return "Activated!"

@application.route("/off")
def off():
    subprocess.call(["/home/pi/led-strip-pi/led.sh", "stop"])
    return "All off!"

def stop():
    subprocess.call(["/home/pi/led-strip-pi/led.sh", "stop"])
    time.sleep(0.5)

@application.route("/rgb/<r>/<g>/<b>")
def rgb(r, g, b):
    stop()
    subprocess.call(["/home/pi/led-strip-pi/led.sh", "start", r, g, b])
    return "Activated!"
"""

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5555, debug=True)
