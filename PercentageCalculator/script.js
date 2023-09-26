const form= document.querySelector("form");

document.getElementById("sumbit").addEventListener('click',function(){
    const obt= parseInt(document.getElementById('obt').value);
    const total= parseInt(document.getElementById('total').value);
    const result= document.getElementById("result");
    const percentage= (obt/total)*100

    result.innerHTML= "That's a whopping " + percentage.toFixed(2) + '%';
})
