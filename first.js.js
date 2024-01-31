
function sum(){
    var fir = parseInt(document.getElementById('first').value);
    var sec = parseInt(document.getElementById('second').value);
    var result=(fir/100)*sec;
    document.getElementById('third').value=result;
}
