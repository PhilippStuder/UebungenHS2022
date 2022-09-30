function wuerfeln(){
    var a=Math.floor(6*Math.random())+1
    return a
}

var b=wuerfeln()
console.log(b)
while (b!=2){
    b=wuerfeln()
}
console.log(b)
