import json
def readDB():
    F=open("malumot.json","r")
    Boza=F.read()
    Boza=json.loads(Boza)
    F.close()
    return Boza
def writeNew(new):
    F=open("malumot.json","w")
    new=json.dumps(new)
    F.write(new)
    F.close()
def writeD(user,id):
    Boza=readDB()
    if user=='null':
        user=id
    Boza[user]={'id':id, 'poz':0, 'lang':"", 'city':"", 'tp':["","","",[0,0]]}
    writeNew(Boza)
def tekshirish(user,id):
    boza=readDB()
    if boza.get(user)==None:
        writeD(user,id)
    else:
        boza[user]["poz"]=0
        writeNew(boza)
