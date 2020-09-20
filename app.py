#!/usr/bin/python3

import glob

from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from pygame import mixer
from mutagen.mp3 import MP3

from sound import Sound, PlayingSoundState

sound_files_root_location = '/home/pi/Music/'
selected_sound_name = ''
volume = 0.5

app = Flask(__name__)
Bootstrap(app)
sound_state: PlayingSoundState = None


@app.route('/')
def list_available_sounds():
    available_sound_file_names = glob.glob(sound_files_root_location + "*.mp3")
    available_sounds = []
    for sound_absolute_path in available_sound_file_names:
        sound_file_name = sound_absolute_path.replace(sound_files_root_location, "").replace(".mp3", "")
        file_info = MP3(sound_absolute_path)
        sound = Sound(sound_file_name, int(file_info.info.length))
        available_sounds.append(sound)

    available_sounds.sort(key=lambda s: s.name.lower())

    return render_template(template_name_or_list="home.html",
                           sounds=available_sounds,
                           current_sound_state=sound_state,
                           volume=volume)


@app.route('/start', methods=['POST'])
def start_playing_sound():
    global sound_state

    selected_sound_name = request.args.get('soundName', '')
    sound_file_location = "/home/pi/Music/" + selected_sound_name + ".mp3"
    sound_state = PlayingSoundState(name=selected_sound_name, duration=int(MP3(sound_file_location).info.length))
    mixer.music.set_volume(volume)
    mixer.music.load(sound_file_location)
    mixer.music.play()
    return jsonify(sound_state.__dict__)


@app.route('/resume', methods=['POST'])
def resume_playing_sound():
    global sound_state

    mixer.music.unpause()
    sound_state.playing = True
    return jsonify(sound_state.__dict__)


@app.route('/pause', methods=['POST'])
def pause_playing_sound():
    global sound_state

    mixer.music.pause()
    sound_state.playing = False
    return jsonify(sound_state.__dict__)


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
