const quotes = [
    "I'm ready, I'm ready, I'm ready! - SpongeBob SquarePants",
    "F is for friends who do stuff together, U is for you and me, N is for anywhere and anytime at all! - SpongeBob SquarePants",
    "I'm not just ready, I'm ready Freddy! - SpongeBob SquarePants",
    "Remember, licking doorknobs is illegal on other planets. - SpongeBob SquarePants",
    "The inner machinations of my mind are an enigma. - Patrick Star",
    "I can't hear you, it's too dark in here! - Patrick Star",
    "I'm ugly and I'm proud! - SpongeBob SquarePants",
    "I'll have you know that I stubbed my toe last week while watering my spice garden and I only cried for 20 minutes. - Squidward Tentacles",
    "Once there was an ugly barnacle. He was so ugly that everyone died. The end. - Patrick Star",
    "Is mayonnaise an instrument? - Patrick Star",
    "Can you give SpongeBob his brain back? - Patrick Star",
    "I guess hibernation is the opposite of beauty sleep. - Squidward Tentacles",
    "I know of a place where you never get harmed. A magical place with magical charms. Indoors! Indoors! Indoors! - SpongeBob SquarePants",
    "I can't believe I'm finally wearing a Krusty Krab hat. Promotion, here I come! - SpongeBob SquarePants",
    "I'll take a double triple bossy deluxe on a raft, 4x4, animal-style, extra shingles with a shimmy and a squeeze, light axle grease, make it cry, burn it, and let it swim. - Bubble Bass",
    "Sandy: What do you usually do when I'm gone? SpongeBob: Wait for you to come back.",
    "SpongeBob: Don't worry, Mr. Krabs, I'll have you out of there faster than a toupee in a hurricane!",
    "SpongeBob: I know of a place where you never get harmed. A magical place with magical charm. Indoors. Indoors. Indoors. - Squidward: What's that? - SpongeBob: Outdoors.",
    "SpongeBob: Can I be excused for the rest of my life?",
    "SpongeBob: I'm not just ready, I'm ready Freddy!",
    "SpongeBob: You don't need a license to drive a sandwich.",
    "SpongeBob: Goodbye everyone, I'll remember you all in therapy.",
    "SpongeBob: Patrick, I don't think Wumbo is a real word. Patrick: Come on, SpongeBob, we're best friends. I would never call you a Wumbologist if I didn't think you were one.",
    "SpongeBob: I'm a Goofy Goober, yeah. You're a Goofy Goober, yeah. We're all Goofy Goobers, yeah. Goofy, goofy, goober, goober, yeah!",
    "SpongeBob: Once there was an ugly barnacle. He was so ugly that everyone died. The end."
];



function getRandomQuote() {
    //implement getting a random quote from the array.
    return (quotes[Math.floor(Math.random() * (quotes.length + 1))]);
}

function startGame() {
    /*
    1 - implement game start/restart logic 
    2 - generate a random quote and display it in the relevant html element
    2* - think carefully how to do it such that you can change the background of each char individually
    */
    result.innerHTML = '';
    input.value = '';
    quote.innerHTML = '';

    button.setAttribute('name', 'on');
    let seconds = 0;
    quoteString = getRandomQuote();

    quoteString.split('').forEach(word => {
        const letterSpan = document.createElement('span');
        letterSpan.classList.remove('correct');
        letterSpan.classList.remove('incorrect');
        letterSpan.innerText = word;
        quote.appendChild(letterSpan);
    });

    function secTimer() {
        seconds += 1;
        timer.innerText = `${seconds} s`;
    }

    clock = setInterval(secTimer, 1000);

    input.addEventListener('input', checkInput);
    button.removeEventListener('click', startGame);
    button.addEventListener('click', endGame);
}

function checkInput() {
    //implement checking input, ending the game by calling the endGame() function when needed. 
    //add the relevant css class to each letter
    const arrQuote = quote.querySelectorAll('span');
    const arrInput = input.value.split('');

    arrQuote.forEach((letterSpan, index) => {
        const character = arrInput[index];
        if (character == null){
            letterSpan.classList.remove('correct');
            letterSpan.classList.remove('incorrect');
        }
        else if (character === letterSpan.innerText){
            letterSpan.classList.add('correct');
            letterSpan.classList.remove('incorrect');
        }
        else{
            letterSpan.classList.add('incorrect');
            letterSpan.classList.remove('correct');
        }
    })

}

function countMatchingChars(strA, strB) {
    //helper function used to calculate hits, used for percentage.
}

function endGame() {
    //stop the timer, calculate elapsed time in seconds
    //in the result element display:
    //  a) how many words were typed
    //  b) in how many seconds it was done
    //  c) the speed (wpm)
    //  d) the accuracy as percentage
    console.log(quote.textContent)
    const wordsCount = input.value.split('').length;
    const quoteCount = quote.textContent.split('').length;
    let seconds = timer.textContent.split('')[0];
    let wpm = (seconds / 60) * wordsCount;
    const correctWords = document.getElementsByClassName("correct");
    let accuracy = (correctWords.length / quoteCount) * 100;

    result.innerHTML = `<br><span>You typed ${wordsCount} words</span><br><span>in ${seconds} seconds</span><br><span>Your speed is ${wpm} wpm</span><br><span>with ${accuracy}% accuracy</span>`;

    button.setAttribute('name', 'off');
    clearInterval(clock);

    button.removeEventListener('click', endGame);
    button.addEventListener('click', startGame);
}

let clock;

const quote = document.getElementById("quote");
const timer = document.getElementById("timer");
const input = document.getElementById("input");
const result = document.getElementById("result")
const button = document.getElementById("start-btn");

button.addEventListener('click', startGame);