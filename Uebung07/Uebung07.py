import uvicorn
from fastapi import FastAPI

app = FastAPI()

d={}
file=open("PLZO_CSV_LV95.csv", encoding="utf-8")
next(file)
for line in file:
    daten =line.strip().split(";")
    ort=daten[0]
    zip=str(daten[1])
    gemeinden=daten[3]
    kanton=daten[5]
    zusatzziffer=str(daten[2])
    bfsnr=daten[4]
    e=daten[6]
    n=daten[7]
    sprache=daten[8]
    d[zip+zusatzziffer]={"Gemeinde":gemeinden,"PLZ": zip, "ORT": ort, "Kanton":kanton, "Zusatzziffer":zusatzziffer, "BfsNR":bfsnr,"E":e,"N":n,"Sprache":sprache}


file.close()

@app.get("/")
async def root():
    a=5
    b=10
    return {"test": "Hello World", "1":a+b}
@app.get("/data/{pfad}")
async def demo(pfad):
    return {"path":pfad}

@app.get("/summe")
async def calc(a:int=0,b:int=0):
    return {"summe": a+b}

@app.get("/plz")
async def plz(plz: str):
    if plz in d:
        return d[plz]
    # file=open("PLZO_CSV_LV95.csv", encoding="utf-8")
    # next(file)
    # for line in file:
    #     daten =line.strip().split(";")
    #     ort=daten[0]
    #     zip=daten[1]
    #     gemeinde=daten[3]
    #     kanton=daten[5]
    #     d[zip]={"PLZ": zip, "ORT": ort, "Gemeinde":gemeinde,"Kanton":kanton}

    #     if zip==plz:
    #         return {"PLZ": zip, "ORT": ort, "Gemeinde":gemeinde,"Kanton":kanton}

    
    # file.close()
    return {"ERROR": "PLZ NOT FOUND"}

@app.get("/gemeinde")
async def gemeinde(gemeinde: str):
    
    L={"test":"test"}
    L={}
    for i in d:
        if gemeinde in d[i]["Gemeinde"]:
            L[i]=d[i]
        

        
    # file=open("PLZO_CSV_LV95.csv", encoding="utf-8")
    # next(file)
    # for line in file:
    #     daten =line.strip().split(";")
    #     ort=daten[0]
    #     zip=daten[1]
    #     gemeinde=daten[3]
    #     kanton=daten[5]
    #     d[zip]={"PLZ": zip, "ORT": ort, "Gemeinde":gemeinde,"Kanton":kanton}

    #     if zip==plz:
    #         return {"PLZ": zip, "ORT": ort, "Gemeinde":gemeinde,"Kanton":kanton}
    if L=={}:
        return {"ERROR": "GEMEINDE NOT FOUND"}
    
    # file.close()
    return L
    



uvicorn.run(app, host="127.0.0.1",port=8000)