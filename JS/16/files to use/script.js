function eventLoop() {
    let count = 0;
    function updateCount (){
        count += 1;
        const countElement = document.getElementById("counter-display");
        countElement.innerText = count;
    }
    return updateCount;
}

const button = document.getElementById("my-button");
button.addEventListener("click", eventLoop());