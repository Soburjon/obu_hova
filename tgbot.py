"""
 2This is a echo bot.
 3It echoes any incoming text messages.
 4"""
import logging
from aiogram import Bot, Dispatcher, types, executor
from dictfunc import tekshirish, readDB, writeNew
import menu
from pagoda import pogoda, city, tr
from doing import doing
API_TOKEN = '5014204446:AAEiokPR30F_iHymsSNewQ7da-JMtonmlSo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

writeNew({})
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    a=message['chat']['first_name']
    a1=message['chat']['username']
    a2=message['chat']['id']
    if a1 == 0:
        a1=a2
    tekshirish(a1,a2)
    await bot.send_message(message.from_user.id,f"Salom {a}! ✋🏻\nHush kelibsan \nWelcome\nДобро пожаловать", reply_markup=menu.len)
    #await message.reply(f"Salom {a}! ✋🏻\nBotga hush kelibsan 😂\nWikipediani ishlatib kor")


@dp.message_handler()
async def javob(message: types.Message):
    user=message['chat']['username']
    if user=='null':
        user = message['chat']['id']
    boza = readDB()
    if message.text == "UZ 🇺🇿":
        boza[user]['lang'] = "uz"
        if boza[user]["poz"] == 0:
            boza[user]["poz"] = 1
            writeNew(boza)
            await bot.send_message(message.from_user.id, "Hush kelibsan", reply_markup=menu.asmenuuz)
        else:
            writeNew(boza)
            await bot.send_message(message.from_user.id, '⚙️️ Sozlamalar', reply_markup=menu.setmenuuz)
    elif message.text == "ENG 🇺🇸":
        boza[user]['lang'] = "en"
        if boza[user]["poz"] == 0:
            boza[user]["poz"] = 1
            writeNew(boza)
            await bot.send_message(message.from_user.id, "Welcome", reply_markup=menu.asmenuen)
        else:
            writeNew(boza)
            await bot.send_message(message.from_user.id, '⚙️ Settings', reply_markup=menu.setmenuen)
    elif message.text == "RU 🇷🇺":
        boza[user]['lang'] = "ru"
        if boza[user]["poz"] == 0:
            boza[user]["poz"] = 1
            writeNew(boza)
            await bot.send_message(message.from_user.id, "Добро пожаловать", reply_markup=menu.asmenuru)
        else:
            writeNew(boza)
            await bot.send_message(message.from_user.id, '⚙️ Настройки', reply_markup=menu.setmenuru)
    elif message.text=='🌤 Obu-havo':
        boza[user]["poz"] = 2
        writeNew(boza)
        await bot.send_message(message.from_user.id, '🌤 Obu-havo', reply_markup=menu.tpmenuuz)
    elif message.text=='🌤 Weather':
        boza[user]["poz"] = 2
        writeNew(boza)
        await bot.send_message(message.from_user.id, '🌤 Weather', reply_markup=menu.tpmenuen)
    elif message.text=='🌤 Погода':
        boza[user]["poz"] = 2
        writeNew(boza)
        await bot.send_message(message.from_user.id, '🌤 Погода', reply_markup=menu.tpmenuru)
    elif message.text=='⚙️️ Sozlamalar':
        boza[user]["poz"] = 3
        writeNew(boza)
        await bot.send_message(message.from_user.id, '⚙️️ Sozlamalar', reply_markup=menu.setmenuuz)
    elif message.text=='⚙️ Settings':
        boza[user]["poz"] = 3
        writeNew(boza)
        await bot.send_message(message.from_user.id, '⚙️ Settings', reply_markup=menu.setmenuen)
    elif message.text=='⚙️ Настройки':
        boza[user]["poz"] = 3
        writeNew(boza)
        await bot.send_message(message.from_user.id, '⚙️ Настройки', reply_markup=menu.setmenuru)
    elif message.text=='📅 Bugungi obu-havo':
        text=pogoda(user,0)
        await message.answer(text)
    elif message.text=='📆 Bugungi(24 soat) obu-havo':
        text=pogoda(user,1)
        await message.answer(text)
    elif message.text=='🗓 3 kunga malumot':
        text=pogoda(user,2)
        await message.answer(text)
    elif message.text=="📅 Today's weather":
        text=pogoda(user,0)
        await message.answer(text)
    elif message.text=="📆 Today's(24 h) weather":
        text=pogoda(user,1)
        await message.answer(text)
    elif message.text=='🗓 3 day reference':
        text=pogoda(user,2)
        await message.answer(text)
    elif message.text=="📅 Сегодня погода":
        text=pogoda(user,0)
        await message.answer(text)
    elif message.text=="📆 Сегодня(24 ч) погода":
        text=pogoda(user,1)
        await message.answer(text)
    elif message.text=='🗓 Информация за 3 дня':
        text=pogoda(user,2)
        await message.answer(text)
    elif message.text=='⬅️ Orqaga':
        boza[user]['poz']=1
        writeNew(boza)
        await bot.send_message(message.from_user.id, "Asosiy menu", reply_markup=menu.asmenuuz)
    elif message.text=='⬅️ Back':
        boza[user]['poz']=1
        writeNew(boza)
        await bot.send_message(message.from_user.id, "Main menu", reply_markup=menu.asmenuen)
    elif message.text=='⬅️ Назад':
        boza[user]['poz']=1
        writeNew(boza)
        await bot.send_message(message.from_user.id, "Главное меню", reply_markup=menu.asmenuru)
    elif boza[user]['poz']==10:
        text=city(message.text,boza[user]['lang'])
        if len(text)==1:
            await message.answer(f"{text[0]}")
        else:
            if boza[user]['city']!="":
                boza[user]['poz'] = 3
                if boza[user]['lang']=='uz':
                    await bot.send_message(message.from_user.id, '⚙️️ Sozlamalar', reply_markup=menu.setmenuuz)
                elif boza[user]['lang']=='en':
                    await bot.send_message(message.from_user.id, '⚙️ Settings', reply_markup=menu.setmenuen)
                else:
                    await bot.send_message(message.from_user.id, '⚙️ Настройки', reply_markup=menu.setmenuru)
            else:
                boza[user]['poz'] = 2
            boza[user]['tp']=["","","",[0,0]]
            boza[user]['city']=message.text
            writeNew(boza)
            await message.answer(f"{text[0]}\n{text[1]}")
    elif message.text == "🅰️ Til" or message.text == "🅰️ Language" or message.text == "🅰️ Язык":
        await bot.send_message(message.from_user.id, f"{tr('Tilni tanlang',boza[user]['lang'])}",reply_markup=menu.len)
    elif message.text == "🏙 Shahar":
        boza[user]['poz'] =10
        writeNew(boza)
        await bot.send_message(message.from_user.id, "Shahringizni yozing",reply_markup=menu.backmanuuz)
    elif message.text == "🏙 City":
        boza[user]['poz'] = 10
        writeNew(boza)
        await bot.send_message(message.from_user.id, "Write your city",reply_markup=menu.backmanuen)
    elif message.text == "🏙 Город":
        boza[user]['poz'] = 10
        writeNew(boza)
        await bot.send_message(message.from_user.id, "Напиши свой город",reply_markup=menu.backmanuru)


if __name__ == '__main__':
 executor.start_polling(dp, skip_updates=True)