import uvicorn 

from fastapi import FastAPI
from pyproj import Transformer

app = FastAPI() 
@app.get("/transform")
async def root(): 
    return {"wgs84 zu lv95":"Geben sie folgenden Link ein:/transform/wgs84lv95?lng=0.0000&lat=0.0000","lv95 zu wgs84":"Geben sie folgenden Link ein:/transform/lv95wgs84?east=0.0000&north=0.0000"}


#vmX.sourcelab.ch/transform/wgs84lv95?lng=0.0000&lat=0.000

@app.get("/transform/wgs84lv95")
async def transform(lng:str,lat:str):
    transformer1=Transformer.from_crs("epsg:4326","epsg:2056")
    r1=transformer1.transform(lng, lat)
    geojson=f"""{{"type": "Feature","geometry":{{"type":"point","cooridnates":{r1[0],r1[1]}}}}}"""
    return geojson

@app.get("/transform/lv95wgs84")
async def transform(east:str,north:str):
    transformer2=Transformer.from_crs("epsg:2056","epsg:4326")
    r2=transformer2.transform(east, north)
    geojson=f"""{{"type": "Feature","geometry":{{"type":"point","cooridnates":{r2[0],r2[1]}}}}}"""
    return geojson

@app.get("/transform/test{x}test")
async def test(x):

    return "test"+str(float(float(x)*2))






if __name__ == "__main__": 
    uvicorn.run(app, host="127.0.0.1", port=8001, root_path="/transform")