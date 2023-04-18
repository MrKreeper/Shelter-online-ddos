import requests, random, keyboard, time, pyautogui, os.path

if not os.path.exists("users.csv"):
    with open("users.csv", "a", encoding="utf-8") as f:
        f.write("Никнейм;Почта;Персонаж;Пароль\n")

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

print("Shelter Online reg master, 1.0")
print("Создана в исключительно образовательных целях\n")
print("Чтобы включить программу, нажмите Ctrl+S")
print("Чтобы активировать регистрацию, нажмите Ctrl+B, предварительно открыв поле для логина во вкладке для регистрации")
print("Чтобы остановить программу, зажмите Shift и не отпускайте, пока текст не перестанет вводиться")
starts = False
alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789"
p = False
DELAY = 0.4
with open("users.csv", "a", encoding="utf-8") as f:
    while True:
        if starts:
            if keyboard.is_pressed("shift"):
                break
            if keyboard.is_pressed("ctrl+b"):
                p = True
            if p:
                user = rand_user()
                keyboard.write(user["username"])
                time.sleep(DELAY)
                keyboard.send("enter")
                keyboard.write(user["email"])
                time.sleep(DELAY)
                keyboard.send("enter")
                keyboard.write(user["personage_name"])
                time.sleep(DELAY)
                keyboard.send("enter")
                keyboard.write(user["password"])
                time.sleep(DELAY * 1.5)
                keyboard.send("enter")
                keyboard.write(user["password2"])
                time.sleep(DELAY)
                keyboard.send("enter")
                time.sleep(DELAY)
                keyboard.send("ctrl+l")
                time.sleep(DELAY)
                keyboard.write("http://shelter_online.vm-9d28b85f.na4u.ru:5000/signup")
                time.sleep(DELAY)
                keyboard.send("enter")
                time.sleep(DELAY * 2)
                pyautogui.click()
                f.write(user["username"] + ";" + user["email"] + ";" + user["personage_name"] + ";" + user["password"] + "\n")
        elif keyboard.is_pressed("ctrl+s"):
            starts = True
        
