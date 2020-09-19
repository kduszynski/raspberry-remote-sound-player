# raspberry-remote-sound-player

## Technology
* Python 3
* Flask > 1.1
* Jinja 2 templates
* HTML
* CSS
* jQuery

## Run
Execute `python3 app.py`

## Useful
To mount raspberry onto UNIX
`sudo sshfs -o allow_other,default_permissions user@address:/ /mnt/raspberry`

## Create app as service
Create file `my_project.service` in `/etc/systemd/system/` with below content:
```
[Unit]
Description=My Project
After=network.target

[Service]
WorkingDirectory=/home/pi/project/
ExecStart=/usr/bin/python /home/pi/project/script.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Run:

`sudo systemctl start my_project`    
`sudo systemctl status my_project`

Setup to auto startup after reboot:

`sudo systemctl enable my_project`