function userconfirm() {
    var username = document.getElementById("username").value
    var usercity = document.getElementById("usercity").value
    var user_gender = document.getElementById("usergender").value
    var userdob = document.getElementById("userdob").value
    var useremail = document.getElementById("useremail").value
    var useremailpass = document.getElementById("useremailpass").value
    eel.usersettingwrite(username, usercity, user_gender, userdob, useremail, useremailpass) 
    setTimeout(function(){ window.open('','_self').close(); }, 5000);
}