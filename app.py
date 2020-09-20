#!/usr/bin/python3

import glob

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from pygame import mixer
from mutagen.mp3 import MP3

from sound import Sound

sound_files_root_location = '/home/pi/Music/'
selected_sound_name = ''
volume = 0.5


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def list_available_sounds():
    available_sound_file_names = glob.glob(sound_files_root_location + "*.mp3")
    available_sounds = []
    for sound_absolute_path in available_sound_file_names:
        sound_file_name = sound_absolute_path.replace(sound_files_root_location, "").replace(".mp3", "")
        file_info = MP3(sound_absolute_path)
        sound = Sound(sound_file_name, int(file_info.info.length))
        available_sounds.append(sound)

    return render_template(template_name_or_list="home.html",
                           sounds=available_sounds,
                           selected_sound_name=selected_sound_name,
                           volume=volume)


@app.route('/start', methods=['POST'])
def start_playing_sound():
    global selected_sound_name
    sound_name = request.args.get('soundName', '')
    selected_sound_name = sound_name
    mixer.music.set_volume(volume)
    mixer.music.load("/home/pi/Music/" + selected_sound_name + ".mp3")
    mixer.music.play()
    return selected_sound_name


@app.route('/resume', methods=['POST'])
def resume_playing_sound():
    mixer.music.unpause()
    return selected_sound_name


@app.route('/pause', methods=['POST'])
def pause_playing_sound():
    mixer.music.pause()
    return selected_sound_name


@app.route('/volume-down', methods=['POST'])
def volume_down():
    global volume
    if volume > 0:
        change_volume_by_and_set(-0.05)
    return str(volume)


@app.route('/volume-up', methods=['POST'])
def volume_up():
    global volume
    if volume < 1:
        change_volume_by_and_set()
    return str(volume)


def change_volume_by_and_set(delta=0.05):
    global volume
    volume += delta
    volume = round(volume, 2)
    mixer.music.set_volume(volume)


if __name__ == '__main__':
    mixer.init()
    app.run(debug=True, port=80, host='0.0.0.0')
