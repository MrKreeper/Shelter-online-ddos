import os, os.path
ind = 5329
with open("Title.html", "r", encoding="utf-8") as f:
    s = f.read()
while True:
    user = int(input("Введите уникальный ID пользователя: "))
    if not os.path.exists(str(user)):
        with open(str(user) + ".html", "w", encoding="utf-8") as f:
            f.write(s[:5330] + str(user) + s[5330:])
        path = os.path.join(os.getcwd(), f"{user}.html")
        print(os.system("\"" + path + "\""))
