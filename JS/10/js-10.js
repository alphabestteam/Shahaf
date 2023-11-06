const myMap = new Map ([
['Main character', 'spongebob'],
['Best friend', 'patrick'],
['pet', 'gary'],
['word buddy', 'squidward'],
['manager', 'Mr. Krabs'],
['teacher', 'Mrs. Puff'],
['location', 'bikini bottom']
]);

//1
console.log(myMap);

//2
let array = Array.from(myMap.keys());
console.log(array)

//3
console.log(myMap.get('location'));

//4
console.log(myMap.size);

//5
console.log(myMap.delete('location'));

//6
console.log(myMap.size);

//7
console.log(myMap);

//8
console.log(myMap.has('location'))