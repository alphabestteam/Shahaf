//3
const mainHeading = document.getElementById("main-heading");

//4
console.log(mainHeading.id);

//5
console.log(mainHeading.className);

//6
console.log(mainHeading.classList);

//7
console.log(mainHeading.getAttribute('data-standard'));

//8
const list = mainHeading.classList;
list.add('border', 'bg-lightcyan');

//9
console.log(mainHeading.textContent);

//10
console.log(mainHeading.textContent.trim());

//11
mainHeading.textContent = "Hello there pearl!”";

//12
mainHeading.innerHTML += "<br><span>its me SpongeBob!</span>"

//13
console.log(mainHeading);

//14
const cloned = mainHeading.cloneNode(true);
console.log(cloned);

//15
const subheading = document.createElement('h2');
subheading.textContent = "jellyfish hunting is the best";

//16
document.body.appendChild(subheading);

//17
let string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue tempus erat. Aliquam feugiat congue augue, eu pharetra ligula tincidunt vitae. Sed nec tempor massa. Integer interdum vitae nisi sed malesuada. Maecenas id augue quis urna lobortis sollicitudin. Cras accumsan eros ac dolor suscipit, ac dapibus magna consequat. Quisque tempus justo ac nulla vehicula, et ullamcorper tortor rhoncus. Mauris sit amet efficitur sem, vitae tempor ex. Aliquam porta, metus eu mollis viverra, sem justo tempus ipsum, a posuere nisi nibh a sem. Sed at erat mollis, finibus metus et, auctor tortor. Suspendisse in quam purus."

//18
const wordArr = string.split(' ');

//19
const colors = ["red", "orange", "yellow", "greenyellow", "lightblue", "mediumpurple"];

//20
const randomColor = () => colors[Math.floor(Math.random()*colors.length)];

//21
let randomWords = document.getElementById("random-words")

//22
function loremIpsumWord (word){
    const span = document.createElement("span");
    const style = "background-color: " + randomColor();
    span.setAttribute("style", style);
    span.textContent = word;
    span.className = "random-word";
    //23
    randomWords.appendChild(span);
}

wordArr.forEach(loremIpsumWord);

randomWords.innerHTML += "<br><br><button type='button' id='button'>Change Background color!</button>";
button = document.getElementById('button');

button.addEventListener("click", changeColor);

const arrWords = document.getElementsByClassName("random-word")

function changeColor(){
    for (let i = 0; i < arrWords.length; i++){
        const style = "background-color: " + randomColor();
        arrWords[i].setAttribute("style", style);
    }
}