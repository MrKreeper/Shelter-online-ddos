import os, os.path, requests, json
ind = 5318
ind1 = 573
s = """<!DOCTYPE html>
<!-- saved from url=(0052)http://shelter_online.vm-9d28b85f.na4u.ru:5000/index -->
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <title>Title</title>
    <link rel="stylesheet" href="./Title_files/index.css">
</head>
<body>
<div class="wrapper">
    <header>
    <div class="head_font">Shelter online</div>
    <a href="http://shelter_online.vm-9d28b85f.na4u.ru:5000/personage/current_user.id"></a><div class="name_font"><a href="http://shelter_online.vm-9d28b85f.na4u.ru:5000/personage/current_user.id"></a>
    <a href="http://shelter_online.vm-9d28b85f.na4u.ru:5000/logout">Выйти</a>
    </div>
    </header>

    <div class="element" id="hero_container">
        <h1> Герой </h1>
        <div id="hero">
        <div class="base_font">
          <div id="hero_name"></div>
          <div> Здоровье: <span id="hero_hp"> </span> из <span id="hero_max_hp"> </span> </div>               
          <div> Сила: <span id="strength"> </span>  </div>
          <div> Восприятие: <span id="perception"> </span> </div>
          <div> Выносливость: <span id="endurance"> </span> </div>
          <div> Харизма: <span id="charisma"> </span>  </div>
          <div> Интелект: <span id="intellect"> </span> </div>
          <div> Ловкость: <span id="agility"> </span> </div>
          <div> Удача: <span id="luck"> </span> </div>
            <br>
          <div> Аптечки: <span id="stimpacks"> </span>  </div>
          <div> Золото: <span id="money"> </span> </div>
          <div> Опыт: <span id="experience"> </span>  </div>
</div>
        </div>
    </div>

    <div class="element" id="feed_container">
      <h1> Новости </h1>
        <div class="base_font">
      <div id="feed">
      </div>
            </div>
    </div>

    <div class="element" id="enemy_container">
        <h1> Враг </h1>
        <div class="base_font">
        <div id="enemy">
          <div> Враг: <span id="enemy_name"> </span></div>
          <div> Здоровье: <span id="enemy_hp"> </span> из <span id="enemy_max_hp"> </span> </div>

        </div>
            </div>
    </div>
</div>

<footer>
    <div class="base_font">
        <ul>
            Разработчики:
           <li>Заитов Илья <a href="https://t.me/ilia_zaitov">tg</a></li>
           <li>Чепелев Иван <a href="https://t.me/Lazyy_ivan">tg</a></li>
           <li>Игуменцев Григорий <a href="https://t.me/alerdGG">tg</a></li>
           <li>Левин Александр <a href="https://discordapp.com/users/851338239508086815/">ds</a></li>
           <li>Куликов Егор <a href="https://t.me/Tynisdez">tg</a></li>
           <li>Дунин Дмитрий <a href="https://t.me/">tg</a></li>
        </ul>

    </div>

<script src="./Title_files/embed.js.Без названия"></script>
<iframe src="./Title_files/saved_resource.html" frameborder="0" name="ya-form-64170cd902848f1ef878c4a1" width="650" style="height: 145px;"></iframe>

<div class="center">Все права защищены ©2023
<img src="./Title_files/real-it.jpg">

</div>
</footer>




<script>
    function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

function response_handler(str_response) {
    let json_response = JSON.parse(str_response)
    console.log(json_response)
    let txt = json_response.message
    let feed = document.getElementById("feed");
    let news_div=document.createElement("div");
    news_div.classList.add("news");
    news_div.innerHTML=txt;
    let news_divs=document.getElementsByClassName('news');
    if (news_divs.length>5) {
        news_divs[0].remove();
    }
    feed.append(news_div)
    let hero = json_response.hero


    if (hero.state == 'battle') {
        let enemy = json_response.enemy
        document.getElementById('enemy_name').innerHTML=enemy.name
        document.getElementById('enemy_max_hp').innerHTML=enemy.max_hp
        document.getElementById('enemy_hp').innerHTML=enemy.hp
    }

    let hero_div=document.getElementById('hero_hp');
    hero_div.innerHTML=hero.hp;
    //добавить имя героя
    hero_div=document.getElementById('hero_max_hp');
    hero_div.innerHTML=hero.max_hp;
    hero_div=document.getElementById('strength');
    hero_div.innerHTML=hero.strength;
    hero_div=document.getElementById('perception');
    hero_div.innerHTML=hero.perception;
    hero_div=document.getElementById('endurance');
    hero_div.innerHTML=hero.endurance;
    hero_div=document.getElementById('charisma');
    hero_div.innerHTML=hero.charisma;
    hero_div=document.getElementById('intellect');
    hero_div.innerHTML=hero.intellect;
    hero_div=document.getElementById('agility');
    hero_div.innerHTML=hero.agility;
    hero_div=document.getElementById('luck');
    hero_div.innerHTML=hero.luck;
    hero_div=document.getElementById('experience');
    hero_div.innerHTML=hero.experience;
    hero_div=document.getElementById('money');
    hero_div.innerHTML=hero.money;
    hero_div=document.getElementById('stimpacks');
    hero_div.innerHTML=hero.stimpacks;




}

setInterval(() => httpGetAsync('http://shelter_online.vm-9d28b85f.na4u.ru:5000/api/update/',response_handler),3000);

</script>

</body></html>"""
while True:
    user = int(input("Введите уникальный ID пользователя: "))
    if not os.path.exists(str(user)):
        r = requests.get("http://shelter_online.vm-9d28b85f.na4u.ru:5000/api/update/" + str(user))
        nickname = json.loads(r.text)["hero"]["name"]
        with open(str(user) + ".html", "w", encoding="utf-8") as f:
            f.write(s[:ind1] + nickname + s[ind1:ind] + str(user) + s[ind:])
        path = os.path.join(os.getcwd(), f"{user}.html")
        print(os.system("\"" + path + "\""))
    os.system("cls")
