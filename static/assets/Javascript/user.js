var modalBtn = document.querySelector('.modal-btn');
var modalBg = document.querySelector('.update-user');
var modalClose = document.querySelector('.close-button');

modalBtn.addEventListener('click', function () {
  modalBg.classList.add('bg-active');
});
modalClose.addEventListener('click', function(){
   modalBg.classList.remove('bg-active');
});
