import requests, json
scanm = int(input("Введите максимальный ID пользователя для сканирования: "))
for i in range(1, scanm + 1):
    r = requests.get("http://shelter_online.vm-9d28b85f.na4u.ru:5000/api/update/" + str(i))
    if r:
        print(i, json.loads(r.text)["hero"]["name"])
    else:
        break
print("Итого просканировано:", i, "пользователей")
input()
