function userconfirm() {
    var username = document.getElementById("username").value
    var usercity = document.getElementById("usercity").value
    var user_gender = document.getElementById("usergender").value
    var userdob = document.getElementById("userdob").value
    var useremail = document.getElementById("useremail").value
    var useremailpass = document.getElementById("useremailpass").value
    setTimeout(window.open("loaded.html","_self"), 5000);
    eel.usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass) 
    
}