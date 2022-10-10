function uebung03(){
    var e=document.querySelector("#eingabe")
    var t=document.querySelector("#text")
    var random=Math.floor(Math.random()*16777215).toString(16);
    var farbe="#"+random;
    t.innerHTML=e.value
    t.style["color"]=farbe;
    t.style["font-size"]="50px";

}