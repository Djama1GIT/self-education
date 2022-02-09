import requests
r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")
while r.text[:2] != "We":
    r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/"+r.text)
print(r.text)