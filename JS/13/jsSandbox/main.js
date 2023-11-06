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
