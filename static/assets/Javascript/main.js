//adding Number plate to sale Form
function PlateOutput() {
    let Nump = document.getElementById('numberPlate').value
    document.getElementById('numbplate').value = Nump
}
document.getElementById('submit-btn').addEventListener('click', () =>{
    let Nump = document.getElementsByClassName('numberPlate').value = " "
});

//Adding Body type to sale form *body-btn
let bodybtns = document.getElementsByClassName('body-btn1')

for(i = 0; i < bodybtns.length; i++){
    bodybtns[i].addEventListener('click', function() {

       var categoryId= this.dataset.category
       var action = this.dataset.action
       console.log('categoryId:',categoryId, 'Action:',action)
        //document.getElementById('bodyType').value = bodydata
    })
}
//Adding Service type to sale form
var servicebtns = document.getElementsByClassName('service-type')

for(var i = 0; i < servicebtns.length; i++){
    servicebtns[i].addEventListener('click', function() {

        var servicebtns = document.getElementById('servce-btn').innerText
        document.getElementById('serviceType').value = servicebtns
        //servicebtns.style.backgroundColor = "Green"  service-type

        console.log(servicebtns)


    })
}
//Adding staff  to sale form 'operator-btn' 'washer'
var staffbtns = document.getElementsByClassName('washer')

for(var i = 0; i < staffbtns.length; i++){
    staffbtns[i].addEventListener('click', function() {
      var staffbtns = document.getElementById('operator-btn').innerText
        document.getElementById('staff-washing').value = staffbtns
    })
    console.log(staffbtns)
}

