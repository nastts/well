from flask import Flask
import random
app = Flask(__name__)
random_facts = [
    "Самая длинная змея в мире - анаконда, которая может достигать длины до 9 метров.",
    "Вселенная состоит преимущественно из темной материи и темной энергии, которые до сих пор остаются загадкой для ученых.",
    "Человеческое сердце создает достаточно давления, чтобы выбросить кровь на расстояние до 10 метров.",
    "Кофеин - это наркотик, который стимулирует центральную нервную систему и может вызывать зависимость.",
    "Пингвины не могут летать, но они отлично плавают и ныряют.",
    "Более половины всех видов животных на Земле - это насекомые.",
    "Гепард - самое быстрое сухопутное животное, способное развивать скорость до 100 км/ч за несколько секунд."
]
@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">Посмотреть случайный факт!</a> <br> <a href="/password">сгенерировать пароль!</a>'

@app.route("/random_fact")
def fact():
    return f'<p>{random.choice(random_facts)}</p>'
@app.route("/password")
def password():
    print('ГЕНЕРАТОР ПАРОЛЕЙ')
    a = ['+', 'a', 'h', 'B', 'C', '1', '=', 'Z', 'T']
    b = ['v', '-', 'b', 'i', 'D', '4', '6', '7', 'W']
    c = ['p', 'w', '*', 'c', 'j', 'E', '2', '3', '5']
    d = ['I', 'q', 'x', '9', 'd', 'k', 'F', '@', 'U']
    e = ['J', 'M', 'r', 'y', '0', '?', 'l', 'G', '8']
    q = ['K', '#', 'N', 's', 'z', 'V', 'e', 'n', 'H']
    u = ['L', '/', 'Q', 'O', 't', 'A', 'X', 'f', 'o']
    w = ['!', '$', 'R', 'S', 'P', 'u', '&', 'Y', 'g']
    
    password = random.choice(a) + random.choice(b) + random.choice(c) + random.choice(d) + random.choice(e) + random.choice(q) + random.choice(u) + random.choice(w)
    return f'<p>Ваш пароль: {password}</p>'
    
        

app.run(debug=True)