from requests_html import HTMLSession
from requests_html import HTML
from pyquery import PyQuery as pq

url = "https://www.google.com/"

session = HTMLSession()

# r = session.get(url)

# r.html.render(sleep=1, keep_page=True, scrolldown=1)

# calendar_address = "https://cc.howardcountymd.gov/desktopmodules/EventPlannerModule/template/js/fullcalendar.js"
calendar_address = "https://cc.howardcountymd.gov/Calendar"
calendar_query_script = open("hocoCalendarQuery.js", "r")
calendar_query = calendar_query_script.read()
# print(divMain("#calendar").text()) #.fullCalendar(calendar_query)

# calendar_page = session.get(calendar_address)
# calendar_page.html.render(sleep=1, keep_page=True, scrolldown=1, script=calendar_query)
