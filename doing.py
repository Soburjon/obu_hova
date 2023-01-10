from dictfunc import readDB, writeNew
import menu
def lang(user,lan):
    boza=readDB()
    boza[user]['lang']=lan
    if lan=="uz":
        text="Hush kelibsan"
        m=menu.asmenuuz
        menu2 = "setmenuuz"
    elif lan=="en":
        text = "Welcome"
        m= menu.asmenuen
        menu2 = "setmenuen"
    else:
        text = "Добро пожаловать"
        m= menu.asmenuru
        menu2 = "setmenuru"
    if boza[user]["poz"]==0:
        boza[user]["poz"]=1
        writeNew(boza)
        return [text,menu]
    else:
        writeNew(boza)
        return [text,menu2]
def doing(user,text):
    if text=="UZ 🇺🇿":
        return lang(user,"uz")
    elif text=="ENG 🇺🇸":
        return lang(user, "en")
    elif text=="RU 🇷🇺":
        return lang(user, "ru")
