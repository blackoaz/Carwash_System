let serviceCreate = document.querySelector('create');

document.querySelector('#create-btn').onclick = () =>{
    serviceCreate.classList.toggle('active');
    bodyUpdate.classList.remove('active'); 
    loginForm.classList.remove('active');
    // navbar.classList.remove('active'); 
}

let serviceUpdate = document.querySelector('update');

document.querySelector('#update-btn').onclick = () =>{
    serviceUpdate.classList.toggle('active');
    bodyUpdate.classList.remove('active');
    loginForm.classList.remove('active');
    /* navbar.classList.remove('active'); */
}