from types import SimpleNamespace


kitch="""
/kitchen1 - Европейская кухня👱🏻
/kitchen2 - Кавказская кухня🧔🏻
/kitchen3 - Турецкая кухня🧑🏻
"""
sht= """
Кухня:
европейская, немецкая
Средний счет:
800–1000 сом на человека
Количество мест:
200 мест
Дополнительно:
Wi-Fi, спортивные трансляции, танцпол
Живая, фоновая музыка
Парковка неохраняемая, бесплатная
Телефон:
+996(555)78-70-25
"""
arz = """
Кухня:
европейская, восточная
Средний счет:
800-1000 сом на человека
Количество мест:
150 мест
Дополнительно:
Красивая и уютная летняя площадка,
Большая парковка с услугами парковщика,
Детская зона
Телефон:
+996550696697
"""
crostini="""
Кухня:
европейская, средиземноморская
Средний счет:
1200-1500 сом на человека
Количество мест:
100 мест
Дополнительно:
Wi-Fi, танцпол,
Детское меню,
Фоновая музыка
Телефон:
+996(312)66-93-35
"""
nani="""
Кухня:
Грузинская
Средний счет:
400-600 сом на человека
Количество мест:
150 мест
Дополнительно:
Wi-Fi, кальян,
Бесплатная парковка
Телефон:
+996(701)10-01-35
"""
plen="""
Кухня:
Кавказская, кыргызская
Средний счет:
200-300 сом на человека
Количество мест:
40 мест
Дополнительно:
Wi-Fi, 
Проведение праздников,
Бесплатная парковка,
Фоновая музыка
Телефон:
+996(555)74-42-44
"""
hachap="""
Кухня:
Грузинская 
Средний счет:
300-400 сом на человека
Количество мест:
100 мест
Дополнительно:
Wi-Fi, 
Доставка
Телефон:
+996(505)83-57-77
"""
ocak="""
Кухня:
Тупецкая 
Средний счет:
300-500 сом на человека
Количество мест:
70 мест
Дополнительно:
Wi-Fi, кальян,
Фоновая музыка
Телефон:
+996(555)67-33-41
"""
huzur="""
Кухня:
Тупецкая 
Средний счет:
300-400 сом на человека
Количество мест:
150 мест
Дополнительно:
Wi-Fi,
Фоновая музыка
Телефон:
+996(772)53-38-49
"""
nuri="""
Кухня:
Тупецкая 
Средний счет:
300-500 сом на человека
Количество мест:
150-180 мест
Дополнительно:
Wi-Fi,
Десткая площадка,
Фоновая музыка
Телефон:
+996(707)51-51-05
"""
sin="""
Средняя оценка посетителей: 
4.4
Телефон:
0312 312 054
"""
brod="""
Средняя оценка посетителей: 
4.6
Телефон:
0709 777 733
"""
dor="""
Средняя оценка посетителей: 
4.7
Телефон:
0312 623 000
"""
i="""
Средняя оценка посетителей: 
4.9
Телефон:
0312 299 494
"""
alatoo="""
Средняя оценка посетителей: 
4.3
Телефон:
0312 661 957
"""
auto="""
Описание:
Автокинотеатр - это кинотеатр для автомобилистов под открытым небом.
Здесь вы можете посмотреть наиболее интересные фильмы на большом экране. 
Телефон:
0706 203 090
"""
mus="""
Описание:
Музей является главной художественной сокровищницей Кыргызстана. 
Картинная галерея, позднее переименованная в Киргизский государственный музей изобразительных искусств, 
была открыта 1 января 1935 года.
Телефон: 
0312 621 641
"""
anv="""
Описание:
Мы используем full-body VR — технологию отслеживания движений головы,
рук, корпуса и ног. Попробуйте, и вы сразу почувствуете разницу!
Телефон:
0550 044 666
"""
il="""
Описание:
Интерактивный арт центр 'Иллюзион' уже в полной мере радует своих гостей. 
А фотоальбомы наших посетителей пополняются новыми уникальными фотографиями.
"""
theatre="""
Описание:
Киргизский национальный академический театр оперы и балета им. 
Абдыласа Малдыбаева — театр оперы и балета в городе Бишкек, единственный оперный театр Киргизии
Телефон:
0312621619
"""
zoo="""
Описание:
В Зоомузее представлены все основные типы и классы животного мира. 
Можно ознакомиться с фауной Тянь-Шаня, заказать экскурсию. Имеется богатая коллекция птиц, бабочек.
Телефон: 
0312 641 980
"""
mag="""
Описание:
Magic City - это уникальная детская площадка в Бишкеке площадью 7 000 м2, 
на территории которой Вы и Ваши дети найдут развлечения на любой вкус.
"""
fun="""
Описание:
FunCity является незаменимым местом для любителей развлечений, 
в котором продуманы и реализованы все детали и имеются игровые площадки соответствующие мировым стандартам.
"""
kat="""
Описание:
Если Ты активен и любишь проводить выходные с семьей или с друзьями, с пользой для здоровья, тогда приходи!
Телефон:
(0312) 449-519 
"""
smile="""
Описание:
Спортивный батутный комплекс "Smile" это - свободные прыжки на батуте,
акробатические тренировки, скаладром, боулдеринг стена, веревочный городок. 
proJumping - фитнес, развлечение, праздники, групповые программы.
Телефон:
0556 466 420
"""
sport="""
Описание:
Спортивный комплекс "T-CLUB" - это комплекс, объединивший в себе крытый теннисный клуб с покрытием хард, 
поле для игры в мини-футбол и женский фитнес-клуб Lovely MAMA. 
Общая площадь - 4000 кв.м.
Телефон:
0770891464
"""
strel="""
Описание:
Что может быть лучшим лекарством от стресса, лучшим средством сплочения коллектива, чем яркий стрелковый праздник? 
Масса новых впечатлений, адреналин - и полная безопасность. Наши инструкторы специально проследят, 
чтобы все стрелки остались целыми,невредимыми и довольными. Развлечение для настоящих мужчин!
Телефон:
0999 919 919
"""