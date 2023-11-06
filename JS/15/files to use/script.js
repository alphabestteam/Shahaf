const button = document.getElementById('the-button');
const main = document.querySelector("main");
const bobGif = document.getElementById("bob");

const toggleBob = function(){
    if (button.name == "notClicked"){
        bobGif.setAttribute("src", "./assets/sbdance.gif")
        button.innerText = "Hide Bob ;)"
        button.name = "clicked"
    }

    else if (button.name == "clicked"){
        bobGif.setAttribute("src", "")
        button.innerText = "Show Me Bob ;)"
        button.name = "notClicked"
    }
};

button.addEventListener("click", toggleBob)