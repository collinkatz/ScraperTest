var setInput = function(textBoxName, text) {
    var textbox = document.getElementById(textBoxName);
    textbox.value = text;
}

var click = function(buttonName) {
    document.getElementById(buttonName).click();
}

var u1 = "username";
var p1 = "password";
var submit = "submit";

setInput("username", u1);
setInput("password", p1);
click(submit);