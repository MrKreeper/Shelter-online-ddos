import requests, random, keyboard, time, pyautogui, os.path
import lxml.html
from lxml import html

if not os.path.exists("users.csv"):
    with open("users.csv", "a", encoding="utf-8") as f:
        f.write("Nickname;Email;Personage name;Password\n")

def rand_user():
    res = {}
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    res["username"] = "".join([random.choice(alp) for i in range(random.randint(1, 12))])
    res["email"] = "".join([random.choice(alp) for i in range(random.randint(4, 12))]) + "@" + "".join([random.choice(alp) for i in range(random.randint(1, 6))]) + "." + "".join([random.choice(alp[:-9]) for i in range(random.randint(2, 5))]).replace(" ", "")
    res["personage_name"] = "".join([random.choice(alp) for i in range(random.randint(1, 18))])
    res["password"] = "".join([random.choice(alp) for i in range(random.randint(5, 12))])
    res["password2"] = res["password"]
    res["submit"] = "Submit"
    return res

print("Shelter Online reg master, 2.0")
print("Создана в исключительно образовательных целях\n")

alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'DNT': '1'
}

with open("users.csv", "a", encoding="utf-8") as f:
    session = requests.session()
    session.headers = headers
    while True:
        user = rand_user()
        start = time.time()
        page = lxml.html.fromstring(session.get('http://shelter_online.vm-9d28b85f.na4u.ru:5000/signup').content)
        form = page.forms[0]
        form.fields["username"] = user["username"]
        form.fields['email'] = user["email"]
        form.fields["personage_name"] = user["personage_name"]
        form.fields['password'] = user["password"]
        form.fields['password2'] = user["password2"]
        if keyboard.is_pressed("shift"): break
        r = session.post("http://shelter_online.vm-9d28b85f.na4u.ru:5000/signup", data=form.form_values())
        if r:
            f.write(user["username"] + ";" + user["email"] + ";" + user["personage_name"] + ";" + user["password"] + "\n")
        print(r, user["username"], user["password"], (time.time() - start) * 1000 // 1, "ms")
        if keyboard.is_pressed("shift"): break
