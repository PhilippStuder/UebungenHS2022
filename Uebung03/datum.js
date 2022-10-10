
var t=0

function zeitdatum() {
    var d=new Date();
    var ds = d.toDateString();
    var ts = d.toTimeString();
    var zeit=document.querySelector("#zeit")
    var datum=document.querySelector("#datum")

    zeit.innerHTML=ts
    datum.innerHTML=ds
    

}

function start() {
    console.log("START!");

    if(t==0){
        setInterval(zeitdatum,500);

    }

    
}
