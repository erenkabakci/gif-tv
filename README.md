# gif-tv

gif-tv is a simple python project to make great use of unused screens. It fetches random `y` rated gif and presents as  fullscreen on a desired display. Counter for the refresh is currently `5` mins.

## Installation and Running

### Requirements

- `Python` > `3.0`
- `selenium` follow the steps [here](http://selenium-python.readthedocs.io/installation.html)
- `requests` (use `pip install requests`)
- `Chrome webdriver` https://sites.google.com/a/chromium.org/chromedriver/downloads don't forget to hook it to your `PATH`

### To Run

Simply use `python giphy.py` in the directory.

v0 runs in a loop and doesn't support args. To stop, either quit the browser or use `pkill -f giphy.py`

Enjoy !
