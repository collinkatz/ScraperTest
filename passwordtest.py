from requests_html import HTMLSession
from requests_html import HTML

doc_file = open("index.html", "r")
doc = doc_file.read()

script_file = open("testinput.js", "r")
script = script_file.read()

session = HTMLSession()

# url = "https://www.google.com/"

# r = session.get(url)
r = HTML(html=doc)

# r.html.render(sleep=1, keep_page=True, scrolldown=1)
r.render(script=script, reload=False)

# succ = r.html.find(".SuUcIb")
correct = r.find("#correct", first=True)

print(correct.text)
