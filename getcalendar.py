from requests_html import HTMLSession

url = "https://www.google.com/"

session = HTMLSession()

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1)

calendar_address = "https://cc.howardcountymd.gov/desktopmodules/EventPlannerModule/template/js/fullcalendar.js"