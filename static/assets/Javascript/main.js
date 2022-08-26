//adding Number plate to sale Form
function PlateOutput() {
    let Nump = document.getElementById('numberPlate').value
    document.getElementById('numbplate').value = Nump
}
document.getElementById('submit-btn').addEventListener('click', () =>{
    let Nump = document.getElementById('numberPlate').value = " "
});

//Adding Body type to sale form
var bodybtns = document.getElementsByClassName('body-btn')

for(var i = 0; i < bodybtns.length; i++){
    bodybtns[i].addEventListener('click', function() {
        var bodybtns = document.getElementsByClassName('body-btn').InnerText
        document.getElementById('bodyType').value = bodybtns

        console.log('bodybtns')
        console.log('Hello World')

        
    })
}
//Adding Service type to sale form
var servicebtns = document.getElementsByClassName('service-type')

for(var i = 0; i < servicebtns.length; i++){
    servicebtns[i].addEventListener('click', function() {
        var servicebtns = document.getElementsByClassName('service-type').value
        document.getElementById('serviceType').value = servicebtns

        console.log('servicebtns')

        
    })
}
//Adding staff  to sale form
var staffbtns = document.getElementsByClassName('washer')

for(var i = 0; i < staffbtns.length; i++){
    staffbtns[i].addEventListener('click', function() {
        var staffbtns = document.getElementsByClassName('washer').value
        document.getElementById('staff-washing').value = staffbtns

        console.log('staffbtns')

        
    })
}



