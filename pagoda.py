import json
import time
import requests
from dictfunc import readDB, writeNew
def url(city):
  return f"http://api.weatherapi.com/v1/forecast.json?key=9930c6321be54fd1a61163609223003&q={city}&days=3&aqi=no&alerts=no"
icon={1000:['🌙','☀️'],1003:['🌙☁️','🌤'],1006:['☁️','☁️'],1009:['☁️','☁️'],1030:['🌫','🌫'],1063:['🌙🌧','🌦']
    ,1066:['🌨','🌨'],1069:['💦❄️','💦❄️'],1072:['☁️','☁️'],1087:['🌩','🌩'],1114:['🌨🌫','🌨🌫'],1117:['❄️🌫','❄️🌫']
    ,1135:['🌫','🌫'],1147:['🌫','🌫'],1150:['🌧','🌧'],1153:['🌧','🌧'],1168:['☁️','☁️'],1171:['☁️','☁️'],1180:['🌙🌧','🌦']
    ,1183:['🌧','🌧'],1186:['🌙🌧','🌦'],1189:['🌧','🌧'],1192:['🌙🌧','🌦'],1195:['🌧','🌧'],1198:['☁️','☁️'],1201:['☁️','☁️']
    ,1204:['🌧🌨','🌧🌨'],1207:['🌧🌨','🌧🌨'],1210:['🌧🌨','🌧🌨'],1213:['️🌨','️🌨'],1216:['🌙️🌨','☀️🌨'],1219:['️🌨','️🌨']
    ,1222:['🌙️🌨','☀️🌨'],1225:['️🌨','️🌨'],1237:['️🌨','️🌨'],1240:['🌙🌧','🌦'],1243:['🌙🌧','🌦'],1246:['🌙🌧','🌦']
    ,1249:['🌧🌨','🌧🌨'],1252:['🌧🌨','🌧🌨'],1255:['🌙️🌨','☀️🌨'],1258:['🌙️🌨','☀️🌨'],1261:['🌙️🌨','☀️🌨']
    ,1264:['🌙️🌨','☀️🌨'],1273:['🌙️🌩','☀️🌩'],1276:['🌩','🌩'],1279:['🌩🌨','🌩🌨'],1282:['🌩🌨','🌩🌨']}


from googletrans import Translator
translator=Translator()
def tr(text,til):
  return translator.translate(text, dest=til).text
def tp(boza,lang):
  t1uz=f"📍{boza['location']['name']} {boza['forecast']['forecastday'][0]['date']}"\
    +f"\n\nHozir: {icon[boza['current']['condition']['code']][boza['current']['is_day']]} 🌡{boza['current']['temp_c']}°C   🌬 {boza['current']['wind_kph']} km/soat"\
    +f"\n\nBugun: {tr(boza['forecast']['forecastday'][0]['day']['condition']['text'],'uz')} {icon[boza['forecast']['forecastday'][0]['day']['condition']['code']][1]}"\
    +f"\nYuqori: 🌡{boza['forecast']['forecastday'][0]['day']['maxtemp_c']}°C"\
    +f"\nPast: 🌡{boza['forecast']['forecastday'][0]['day']['mintemp_c']}°C"\
    +f"\n\nNamlik:💧 {boza['forecast']['forecastday'][0]['day']['avghumidity']} %"\
    +f"\nShamol:🌬 {boza['forecast']['forecastday'][0]['day']['maxwind_kph']} km/soat"\
    +f"\nBosim:📊 {boza['current']['pressure_mb']} mbar"\
    +f"\n\nQuyosh chiqishi:🌝 {boza['forecast']['forecastday'][0]['astro']['sunrise'].split()[0]} ertalabgi"\
    +f"\nQuyosh botishi:🌝 {boza['forecast']['forecastday'][0]['astro']['sunset'].split()[0]} kechgi"\
    +f"\nOy holati:🌙 {tr(boza['forecast']['forecastday'][0]['astro']['moon_phase'],'uz')} "

  t1ru=f"📍{tr(boza['location']['name'],'ru')} {boza['forecast']['forecastday'][0]['date']}"\
    +f"\n\nСейчас: {icon[boza['current']['condition']['code']][boza['current']['is_day']]} 🌡{boza['current']['temp_c']}°C   🌬 {boza['current']['wind_kph']} км/ч"\
    +f"\n\nСегодня: {tr(boza['forecast']['forecastday'][0]['day']['condition']['text'],'ru')} {icon[boza['forecast']['forecastday'][0]['day']['condition']['code']][1]}"\
    +f"\nВысокий: 🌡{boza['forecast']['forecastday'][0]['day']['maxtemp_c']}°C"\
    +f"\nНизкий: 🌡{boza['forecast']['forecastday'][0]['day']['mintemp_c']}°C"\
    +f"\n\nВлажность:💧 {boza['forecast']['forecastday'][0]['day']['avghumidity']} %"\
    +f"\nВетер:🌬 {boza['forecast']['forecastday'][0]['day']['maxwind_kph']} км/ч"\
    +f"\nДавление:📊 {boza['current']['pressure_mb']} мбар"\
    +f"\n\nВосход солнца:🌝 {boza['forecast']['forecastday'][0]['astro']['sunrise'].split()[0]} утро"\
    +f"\nЗакат:🌝 {boza['forecast']['forecastday'][0]['astro']['sunset'].split()[0]} вечер"\
    +f"\nПоложение Луны:🌙 {tr(boza['forecast']['forecastday'][0]['astro']['moon_phase'],'ru')} "

  t1en=f"📍{boza['location']['name']} {boza['forecast']['forecastday'][0]['date']}"\
    +f"\n\nNow: {icon[boza['current']['condition']['code']][boza['current']['is_day']]} 🌡{boza['current']['temp_c']}°C   🌬 {boza['current']['wind_kph']} km/h"\
    +f"\n\nToday: {boza['forecast']['forecastday'][0]['day']['condition']['text']} {icon[boza['forecast']['forecastday'][0]['day']['condition']['code']][1]}"\
    +f"\nMax: 🌡{boza['forecast']['forecastday'][0]['day']['maxtemp_c']}°C"\
    +f"\nMin: 🌡{boza['forecast']['forecastday'][0]['day']['mintemp_c']}°C"\
    +f"\n\nHumidity:💧 {boza['forecast']['forecastday'][0]['day']['avghumidity']} %"\
    +f"\nWind:🌬 {boza['forecast']['forecastday'][0]['day']['maxwind_kph']} km/h"\
    +f"\nPressure:📊 {boza['current']['pressure_mb']} mbar"\
    +f"\n\nSunrise:🌝 {boza['forecast']['forecastday'][0]['astro']['sunrise'].split()[0]} AM"\
    +f"\nSunset:🌝 {boza['forecast']['forecastday'][0]['astro']['sunset'].split()[0]} PM"\
    +f"\nMoon phases:🌙 {boza['forecast']['forecastday'][0]['astro']['moon_phase']} "

  t24uz=f"📍{boza['location']['name']} {boza['forecast']['forecastday'][0]['date']}\n"
  for i in range(0,24):
    t24uz+=f"\n{boza['forecast']['forecastday'][0]['hour'][i]['time'].split()[1]}: {icon[boza['forecast']['forecastday'][0]['hour'][i]['condition']['code']][boza['forecast']['forecastday'][0]['hour'][i]['is_day']]}" \
           +f" 🌡{boza['forecast']['forecastday'][0]['hour'][i]['temp_c']}°C   🌬 {boza['forecast']['forecastday'][0]['hour'][i]['wind_kph']} km/soat"

  t24ru = f"📍{tr(boza['location']['name'],'ru')} {boza['forecast']['forecastday'][0]['date']}\n"
  for i in range(0, 24):
    t24ru += f"\n{boza['forecast']['forecastday'][0]['hour'][i]['time'].split()[1]}: {icon[boza['forecast']['forecastday'][0]['hour'][i]['condition']['code']][boza['forecast']['forecastday'][0]['hour'][i]['is_day']]}" \
             + f" 🌡{boza['forecast']['forecastday'][0]['hour'][i]['temp_c']}°C   🌬 {boza['forecast']['forecastday'][0]['hour'][i]['wind_kph']} км/ч"

  t24en = f"📍{boza['location']['name']} {boza['forecast']['forecastday'][0]['date']}\n"
  for i in range(0,24):
    t24en+=f"\n{boza['forecast']['forecastday'][0]['hour'][i]['time'].split()[1]}: {icon[boza['forecast']['forecastday'][0]['hour'][i]['condition']['code']][boza['forecast']['forecastday'][0]['hour'][i]['is_day']]}" \
           +f" 🌡{boza['forecast']['forecastday'][0]['hour'][i]['temp_c']}°C   🌬 {boza['forecast']['forecastday'][0]['hour'][i]['wind_kph']} km/h"

  t3uz = f"📍{boza['location']['name']}\n"
  for i in range(0, 3):
    t3uz+=f"\n{boza['forecast']['forecastday'][i]['date']}: {tr(boza['forecast']['forecastday'][i]['day']['condition']['text'],'uz')} {icon[boza['forecast']['forecastday'][i]['day']['condition']['code']][1]}\n" \
         +f"Harorat: 🌡{boza['forecast']['forecastday'][i]['day']['maxtemp_c']}°C...{boza['forecast']['forecastday'][i]['day']['mintemp_c']}°C  " \
         +f"🌬 {boza['forecast']['forecastday'][i]['day']['maxwind_kph']} km/soat\n"

  t3ru = f"📍{tr(boza['location']['name'],'ru')}\n"
  for i in range(0, 3):
    t3ru += f"\n{boza['forecast']['forecastday'][i]['date']}: {tr(boza['forecast']['forecastday'][i]['day']['condition']['text'], 'ru')} {icon[boza['forecast']['forecastday'][i]['day']['condition']['code']][1]}\n" \
            + f"Температура: 🌡{boza['forecast']['forecastday'][i]['day']['maxtemp_c']}°C...{boza['forecast']['forecastday'][i]['day']['mintemp_c']}°C  " \
            + f"🌬 {boza['forecast']['forecastday'][i]['day']['maxwind_kph']} км/ч\n"

  t3en = f"📍{boza['location']['name']}\n"
  for i in range(0, 3):
    t3en += f"\n{boza['forecast']['forecastday'][i]['date']}: {boza['forecast']['forecastday'][i]['day']['condition']['text']} {icon[boza['forecast']['forecastday'][i]['day']['condition']['code']][1]}\n" \
            + f"Temperature: 🌡{boza['forecast']['forecastday'][i]['day']['maxtemp_c']}°C...{boza['forecast']['forecastday'][i]['day']['mintemp_c']}°C  " \
            + f"🌬 {boza['forecast']['forecastday'][i]['day']['maxwind_kph']} km/h\n"
  day=time.gmtime()[2]
  h=time.gmtime()[3]
  if lang=="uz":
    return [t1uz,t24uz,t3uz,[day,h]]
  elif lang=="ru":
    return [t1ru,t24ru,t3ru,[day,h]]
  else:
    return [t1en,t24en,t3en,[day,h]]
def pogoda(user,n):
  boza=readDB()
  city=boza[user]['city']
  if city=="":
    boza[user]['poz']=10
    writeNew(boza)
    if boza[user]['lang']=='uz':
      return "Birchi marta foydalanayotgan bo'sangiz shahringizni kiriting!"
    elif boza[user]['lang']=='ru':
      return tr("Birchi marta foydalanayotgan bo'sangiz shahringizni kiriting!",'ru')
    else:
      return tr("Birchi marta foydalanayotgan bo'sangiz shahringizni kiriting!", 'en')
  elif time.gmtime()[2]==boza[user]['tp'][3][0] and time.gmtime()[3]==boza[user]['tp'][3][1]:
    return boza[user]['tp'][n]
  else:
    m=requests.get(url(city))
    m=m.json()
    boza[user]['tp']=tp(m,boza[user]['lang'])
    writeNew(boza)
    return boza[user]['tp'][n]
def city(Sh,lan):
  J=requests.get(url(Sh)).json()
  try:
    a=J["error"]
    if lan=='uz':
      return ['Topilmadi']
    elif lan=='ru':
      return [tr('Topilmadi','ru')]
    else:
      return [tr('Topilmadi', 'en')]
  except:
    if lan=='uz':
      return ['Viloyat: '+J['location']['region'],'Mamlakat: '+J['location']['country']]
    elif lan=='ru':
      return ['Область: '+J['location']['region'],'Страна: '+J['location']['country']]
    else:
      return ['Region: '+J['location']['region'],'Country: '+J['location']['country']]
