#!/usr/bin/python3

import glob

from flask import Flask, render_template, request
from pygame import mixer

sound_files_root_location = '/home/pi/Music/'
current_playing_sound_name = ''
volume = 0.5

app = Flask(__name__)


@app.route('/')
def list_available_sounds():
    available_sounds = glob.glob(sound_files_root_location + "*.mp3")
    available_sounds_file_names = []
    for sound in available_sounds:
        available_sounds_file_names.append(sound.replace(sound_files_root_location, "").replace(".mp3", ""))
    return render_template(template_name_or_list="home.html",
                           sounds=available_sounds_file_names,
                           current_playing_sound_name=current_playing_sound_name,
                           volume=volume)


@app.route('/start', methods=['POST'])
def start_playing_sound():
    global current_playing_sound_name
    sound_name = request.args.get('soundName', '')
    current_playing_sound_name = sound_name
    mixer.music.set_volume(volume)
    mixer.music.load("/home/pi/Music/" + current_playing_sound_name + ".mp3")
    mixer.music.play()
    return current_playing_sound_name


@app.route('/resume', methods=['POST'])
def resume_playing_sound():
    mixer.music.unpause()
    return current_playing_sound_name


@app.route('/pause', methods=['POST'])
def pause_playing_sound():
    mixer.music.pause()
    return current_playing_sound_name


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
