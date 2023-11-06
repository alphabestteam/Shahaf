let text = " Kung Fu Panda is a beloved animated movie about a clumsy, food-loving panda named Po who dreams of becoming a kung fu master.\nPo's dream becomes a reality when he is unexpectedly chosen to become the Dragon Warrior and train with the Furious Five to protect the Valley of Peace from the evil Tai Lung.\nKung Fu Panda was released on June 6, 2008, and grossed over $631 million worldwide, making it the highest-grossing non-sequel animated film at the time of its release.\nAlong the way, Po learns valuable lessons about inner strength, perseverance, and the importance of family and friendship.\nWith stunning animation, a heartwarming story, and a star-studded cast including Jack Black, Angelina Jolie, and Jackie Chan, Kung Fu Panda has become a timeless classic for all ages. "

//1
function splitParagraph (text){
    return text.split("\n");
}

console.log(splitParagraph(text));

//2 
function movieToFilm (text){
    return text.replace('movie', 'film');
}

console.log(movieToFilm(text));

//3
function pandaToBear (text){
    return text.replace(/Panda/g, 'Bear');
}

console.log(pandaToBear(text));

//4
function upperCaseText (text){
    return text.toUpperCase();
}

console.log(upperCaseText(text));

//5
function lowerCaseText (text){
    return text.toLowerCase();
}

console.log(lowerCaseText(text));

//6
function findIndex (text){
    return text.indexOf("Po");
}

console.log(findIndex(text));

//7
function poToEnd (text){
    return text.slice(findIndex(text));
}

console.log(poToEnd(text));

//8
function trimText (text){
    return text.trim();
}

console.log(trimText(text));

//9
function poParagraph (text){
    po = poToEnd(text);
    return po.slice(0, po.indexOf("\n"));
}

console.log(poParagraph(text));

//10
function wordArr (text){
    trim_text = trimText(text);
    return trim_text.split(' ');
}

console.log(wordArr(text));

//11
function endAges (text){
    trim_text = trimText(text);
    return trim_text.endsWith('ages.');
}

console.log(endAges(text));

//12
function addString(text){
    return text.concat('is one of my favorite movies!');
}

console.log(addString(text));