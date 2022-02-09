function callback(current_ram){
    document.getElementById("ramoutput").innerHTML=current_ram
};
function checkram(){
eel.checkram()(callback)
}

function callback1(current_cpu){
    document.getElementById("cpuoutput").innerHTML=current_cpu
};
function checkcpu(){
eel.checkcpu()(callback1)
}

function callback2(current_network){
    document.getElementById("networkoutput").innerHTML=current_network
};

function checknetwork(){
eel.checknetwork1()(callback2)
};

function callback3(commandinput){
    document.getElementById("commandinput").innerHTML=commandinput
};

