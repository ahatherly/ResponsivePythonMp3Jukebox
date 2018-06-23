from flask import Flask, render_template, url_for, send_from_directory, request, redirect
import subprocess, time
from filesystem import FSBrowser
from coverart import CoverArt
import urllib.parse

application = Flask(__name__)
home_directory = "/media/FreeAgent_Drive/mp3s"
fileBrowser = FSBrowser(home_directory)
coverartdownloader = CoverArt()

@application.route("/")
def index():
    fileBrowser.setPath("")
    return showContents()

@application.route("/browse")
def browse():
    new_path = request.args.get('dir', '')
    if new_path != None:
        fileBrowser.setPath(new_path)
    return showContents()

@application.route("/play")
def play():
    path = request.args.get('dir', '')
    filename = request.args.get('file', '')
    fileBrowser.setPath(path)
    return send_from_directory(fileBrowser.getFullPath(), filename)

@application.route("/thumb")
def thumb():
    path = request.args.get('dir', '')
    filename = request.args.get('file', '')
    fileBrowser.setPath(path)
    return send_from_directory(fileBrowser.getFullPath(), filename)

@application.route("/coverart")
def coverart():
    path = request.args.get('dir', '')
    fileBrowser.setPath(path)
    result=fileBrowser.getArtistAlbum()
    #coverart.getCoverArt(result['artist'], result['album'])
    return render_template('cover-art.html', path=fileBrowser.getPath(), parent=fileBrowser.getParent(), artist=result['artist'], album=result['album'])

@application.route("/getcover")
def getcover():
    artist = request.args.get('artist', '')
    album = request.args.get('album', '')
    coverartdownloader.getCoverArt(artist, album)
    return render_template('cover-art.html', path=fileBrowser.getPath(), parent=fileBrowser.getParent(), artist=artist, album=album, cover=True)

@application.route("/confirmcover")
def confirmcover():
    path=fileBrowser.getPath()
    fileBrowser.copyCover()
    return redirect("/browse?dir="+urllib.parse.quote_plus(fileBrowser.getPath()), code=302)

@application.route("/tempcover")
def tempcover():
    return send_from_directory("/tmp", "cover.jpg")

def showContents():
    directories = fileBrowser.getDirectories()
    thumb = fileBrowser.getCurrentDirThumb()
    files = fileBrowser.getFiles()
    return render_template('index.html', directories=directories, files=files, thumb=thumb, path=fileBrowser.getPath(), parent=fileBrowser.getParent())



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
