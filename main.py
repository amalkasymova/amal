import re
from telegram import ( 
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    chat,
    replymarkup
)
import telegram
from telegram.ext import (
    CallbackContext, 
    Updater, 
    CommandHandler, 
    PicklePersistence, 
    Filters, 
    MessageHandler,
    updater,
    CallbackQueryHandler
)
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
from menu import main_menu_keyboard
from credentials import TOKEN
from key_bottons import main_menu
from message import sht, arz, crostini, kitch, nani, plen, hachap, ocak, huzur, nuri, sin, brod, dor, i, alatoo, mus, auto, anv, il, mag, theatre, zoo, fun, kat, smile, sport, strel


def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEDUadhl3oEHnxrZtIFM8g5H7Q2OiZnSgACWg8AAsFkiUtoBn1ASv7hiCIE'
    )
    update.message.reply_text(
        "Добро пожаловать, {username}😃! Выберите вид отдыха \ развлечения".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )


def euro():

    keyboard = [
        [InlineKeyboardButton("Ресторан Штайнброй🍽", callback_data='штайнброй')],
        [InlineKeyboardButton("Ресторан Arzu Style🍽", callback_data='арзу')],
        [InlineKeyboardButton("Ресторан Crostini🍽", callback_data='кростини')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1
def kavkaz():

    keyboard = [
        [InlineKeyboardButton("Кафе Нани Бишкек🍽", callback_data='Кафе Нани Бишкек')],
        [InlineKeyboardButton("Кафе Кавказская пленница🍽", callback_data='Кафе Кавказская пленница')],
        [InlineKeyboardButton("Хачапурная №1🍽", callback_data='Хачапурная №1')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1
def turk():

    keyboard = [
        [InlineKeyboardButton("Ожак Кебап🍽", callback_data='Ожак Кебап')],
        [InlineKeyboardButton("Хузур🍽", callback_data='Хузур')],
        [InlineKeyboardButton("Нури Уста🍽", callback_data='Нури Уста')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1
def kino():

    keyboard = [
        [InlineKeyboardButton("Кинотеатр Синематика Бишкек Парк🎥", callback_data='синематика')],
        [InlineKeyboardButton("Кинотеатр Broadway🎥", callback_data='бродвэй')],
        [InlineKeyboardButton("Кинотеатр Cinematica DordoiPlaza🎥", callback_data='дордой')],
        [InlineKeyboardButton("Кинотеатр IMAX🎥", callback_data='аймакс')],
        [InlineKeyboardButton("Кинотеатр 'Ала-Тоо'🎥", callback_data='алатоо')],
        [InlineKeyboardButton("Автокинотеатр🎥🚘", callback_data='авто')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1

def kult():

    keyboard = [
        [InlineKeyboardButton("Mузей изобразительных искусств🏛🎨", callback_data='нац')],
        [InlineKeyboardButton("Зоологический музей🏛🌳", callback_data='зоо')],
        [InlineKeyboardButton("Театр оперы и балета🏛🩰🎼", callback_data='театр')],
    
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1
def kids():

    keyboard = [
        [InlineKeyboardButton("Иллюзион Парк Развлечений🎠", callback_data='иллюзион')],
        [InlineKeyboardButton("Magic City🎠", callback_data='магик')],
        [InlineKeyboardButton("Fun City🎠", callback_data='фан')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1
def active():

    keyboard = [
    
        [InlineKeyboardButton("Каток Городской⛸", callback_data='каток')],
        [InlineKeyboardButton("Smile🤹🏻‍♀️", callback_data='смайл')],
        [InlineKeyboardButton("Спортивный комплекс T-CLUB🏸", callback_data='спорт')],
        [InlineKeyboardButton("Спортивно Стрелковый Комплекс 9*19🔫", callback_data='стрел')],
        [InlineKeyboardButton("ANVIO - клуб виртулальной реальности👀", callback_data='анвио')],
        
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    return reply_markup1



def kitchen1(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Топ 3 заведения с европейской кухней🍴",
        reply_markup=euro()
    )
def kitchen2(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Топ 3 заведения с кавказской кухней🍴",
        reply_markup=kavkaz()
    )
def kitchen3(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Топ 3 заведения с турецкой кухней🍴",
        reply_markup=turk()
    )
def kino_choose(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Топ 5 кинотеатров города🎬",
        reply_markup=kino()
    )
def kult_choose(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Выберите культурный центр🏛 ",
        reply_markup=kult()
    )
def kids_choose(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Выберите развлечение для детей👧🏻👦🏼 ",
        reply_markup=kids()
    )
def active_choose(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Выберите вид активного отдыха🏃🏻",
        reply_markup=active()
    )

CAFE_REGEX= r"(?=("+(main_menu[0]) + r"))"
KINO_REGEX= r"(?=("+(main_menu[1]) + r"))"
KULT_REGEX= r"(?=("+(main_menu[2]) + r"))"
PRIRODA_REGEX= r"(?=("+(main_menu[3]) + r"))"
KIDS_REGEX= r"(?=("+(main_menu[4]) + r"))"
BRON_REGEX= r"(?=("+(main_menu[5]) + r"))"


def kitchen(update: Update, context: CallbackContext):
    info = re.match(CAFE_REGEX, update.message.text)
    update.message.reply_text(
        kitch,
        
    )

def kino_go(update: Update, context: CallbackContext):
    info = re.match(KINO_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите кинотеатр",
        reply_markup=kino()
    )
def kult_go(update: Update, context: CallbackContext):
    info = re.match(KULT_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите  культурный центр",
        reply_markup=kult()
    )
def kids_go(update: Update, context: CallbackContext):
    info = re.match(KULT_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите развлечение для детей ",
        reply_markup=kids()
    )
def active_go(update: Update, context: CallbackContext):
    info = re.match(KULT_REGEX, update.message.text)
    update.message.reply_text(
        "Выберите вид активного отдыха",
        reply_markup=active()
    )
def zapisat(update: Update, context:CallbackContext):
    z = update.message.text
    print(z[:5])
    if z[:5] == 'Бронь':
        context.bot.send_message(
            chat_id = '@caffe_for', 
            text = z
        )

def zapis(update: Update, context: CallbackContext):
    info=re.match(BRON_REGEX, update.message.text)
    update.message.reply_text(
        'Забронировать столик\nПример: "Бронь:\n 1.Имя🗣\n 2.Hомер телефона☎️\n 3.Hазвание заведения🏢\n 4.Kоличество гостей👥"'
    )

def kino_finish(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'синематика':
        msg =  context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = sin,
            
            
        )
        query.message.reply_location(
            latitude=42.874481804326564, 
            longitude= 74.59113822023333,
            reply_to_message_id=msg.message_id,
            reply_markup=kino()
        )
    if query.data == 'бродвэй':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = brod,
            
        )
        query.message.reply_location(
            latitude=42.85604051822263,
            longitude=74.5851750981417,
            reply_to_message_id=msg.message_id,
            reply_markup=kino()
        )
    if query.data == 'дордой':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = dor,
            
        )
        query.message.reply_location(
            latitude=42.87611375973482, 
            longitude=74.61901202779183,
            reply_to_message_id=msg.message_id,
            reply_markup=kino()
        )
    if query.data == 'аймакс':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = i,
            
        )
        query.message.reply_location(
            latitude=42.8341672836298, 
            longitude=74.62043723906825,
            reply_to_message_id=msg.message_id,
            reply_markup=kino()
        )
    if query.data == 'алатоо':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = alatoo,
            
        )
        query.message.reply_location(
            latitude=42.876168858158884, 
            longitude=74.60741666940719,
            reply_to_message_id=msg.message_id,
            reply_markup=kino()
        )
    if query.data == 'авто':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = auto,
            
        )
        query.message.reply_location(
            latitude=42.80528705730703,
            longitude=74.57928439116917,
            reply_to_message_id=msg.message_id,
            reply_markup=kino()
        )
    if query.data == 'штайнброй':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = sht,
            
        )
        query.message.reply_location(
            latitude=42.86703402056113,
            longitude=74.62305883991145,
            reply_to_message_id=msg.message_id,
            reply_markup=euro()
        )
    if query.data == 'арзу':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = arz,
            
        )
        query.message.reply_location(
            latitude=42.87895681598019,
            longitude=74.59642168465354,
            reply_to_message_id=msg.message_id,
            reply_markup=euro()
        )
    if query.data == 'кростини':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = crostini
        )
        query.message.reply_location(
            latitude=42.87963958880446,
            longitude=74.61203929814246,
            reply_to_message_id=msg.message_id,
            reply_markup=euro()
        )

    if query.data == 'Кафе Нани Бишкек':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = nani
        )
        query.message.reply_location(
            latitude=42.834058553311394,
            longitude=74.63084078279456,
            reply_to_message_id=msg.message_id,
            reply_markup=kavkaz()
        )
    if query.data == 'Кафе Кавказская пленница':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = plen
        )
        query.message.reply_location(
            latitude=42.87382035518623,
            longitude= 74.60119979814236,
            reply_to_message_id=msg.message_id,
            reply_markup=kavkaz()
        )
    if query.data == 'Хачапурная №1':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = hachap
        )
        query.message.reply_location(
            latitude=42.829490652422905, 
            longitude=74.62213432512122,
            reply_to_message_id=msg.message_id,
            reply_markup=kavkaz()
        )

    if query.data == 'Ожак Кебап':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = ocak
        )
        query.message.reply_location(
            latitude=42.875346, 
            longitude=74.615399,
            reply_to_message_id=msg.message_id,
            reply_markup=kavkaz()
        )
    if query.data == 'Хузур':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = huzur
        )
        query.message.reply_location(
            latitude=42.87895681598019,
            longitude=74.59642168465354,
            reply_to_message_id=msg.message_id,
            reply_markup=kavkaz()
        )
    if query.data == 'Нури Уста':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = nuri
        )
        query.message.reply_location(
            latitude=42.871908,
            longitude=74.581097,
            reply_to_message_id=msg.message_id,
            reply_markup=kavkaz()
        )
    if query.data == 'нац':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = mus
        )
        query.message.reply_location(
            latitude=42.87876988935866, 
            longitude= 74.61090751348894,
            reply_to_message_id=msg.message_id,
            reply_markup=kult()
        )
    if query.data == 'зоо':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = zoo
        )
        query.message.reply_location(
            latitude=42.87876988935866, 
            longitude= 74.61090751348894,
            reply_to_message_id=msg.message_id,
            reply_markup=kult()
        )
    if query.data == 'анвио':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = anv
        )
        query.message.reply_location(
            latitude=42.873068755760805, 
            longitude= 74.63368429814226,
            reply_to_message_id=msg.message_id,
            reply_markup=active()
        )
    if query.data == 'иллюзион':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = il
        )
        query.message.reply_location(
            latitude=42.85890136774165, 
            longitude= 74.61008876459846,
            reply_to_message_id=msg.message_id,
            reply_markup=kids()
        )
    if query.data == 'театр':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = theatre
        )
        query.message.reply_location(
            latitude=42.87796114715061,
            longitude= 74.61275032694044,
            reply_to_message_id=msg.message_id,
            reply_markup=kult()
        )
    if query.data == 'магик':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = mag
        )
        query.message.reply_location(
            latitude= 42.85643099825967, 
            longitude= 74.62512139810312,
            reply_to_message_id=msg.message_id,
            reply_markup=kids()
        )
    if query.data == 'фан':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = fun
        )
        query.message.reply_location(
            latitude= 42.874749254959355,
            longitude= 74.59043576930571,
            reply_to_message_id=msg.message_id,
            reply_markup=kids()
        )

    if query.data == 'каток':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = kat
        )
        query.message.reply_location(
            latitude= 42.85853393149338, 
            longitude= 74.66536954046859,
            reply_to_message_id=msg.message_id,
            reply_markup=active()
        )
    if query.data == 'смайл':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = smile
        )
        query.message.reply_location(
            latitude= 42.85748096767548, 
            longitude= 74.62744978279534,
            reply_to_message_id=msg.message_id,
            reply_markup=active()
        )
    if query.data == 'спорт':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = sport
        )
        query.message.reply_location(
            latitude= 42.873314432026405, 
            longitude= 74.61323225395923,
            reply_to_message_id=msg.message_id,
            reply_markup=active()
        )
    if query.data == 'стрел':
        msg = context.bot.send_message(
            chat_id = update.effective_chat.id,
            text = strel
        )
        query.message.reply_location(
            latitude= 42.857891232066436, 
            longitude= 74.67698571348825,
            reply_to_message_id=msg.message_id,
            reply_markup=active()
        )



    
updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('kitchen1', kitchen1))
updater.dispatcher.add_handler(CommandHandler('kitchen2', kitchen2))
updater.dispatcher.add_handler(CommandHandler('kitchen3', kitchen3))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(CAFE_REGEX),
    kitchen
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KINO_REGEX),
    kino_go
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KULT_REGEX),
    kult_go
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KIDS_REGEX),
    kids_go
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PRIRODA_REGEX),
    active_go
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BRON_REGEX),
    zapis
    ))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
    ))

updater.dispatcher.add_handler(CallbackQueryHandler(kino_finish))
updater.dispatcher.add_handler(CallbackQueryHandler(kino_choose))
updater.dispatcher.add_handler(CallbackQueryHandler(kult_choose))
updater.dispatcher.add_handler(CallbackQueryHandler(kids_choose))

updater.start_polling()
updater.idle()
