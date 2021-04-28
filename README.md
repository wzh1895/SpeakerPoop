# SpeakerPoop

This script prevents your Bluetooth speaker from automatically turning off.

You need to keep this script running in a terminal, so that it can periodically play a short white noise to keep the speaker active. I made this less boring by displaying a random Chinese Tang poet line every time it plays the noise.

Credit for the Tang poetry collection goes to:
https://github.com/chinese-poetry/chinese-poetry, which is made public under the MIT licence.

## Dependencies

`pip install playsound`

For mac users, pyobjc is necessary to use `playsound`

`pip install pyobjc`

## How to use

`python poop.py`

Then keep the terminal window open.

## Licence

This project is made public under the MIT licence.
