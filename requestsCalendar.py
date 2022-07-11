import webbrowser
import requests

class MyCalendar:
    def __init__(self):
        my_url = "https://cc.howardcountymd.gov/Calendar"
        my_browser = webbrowser.open(my_url)
        