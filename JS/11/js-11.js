const helloWorld = () => 'Hello World!';

const sayHi = (name) => `Hello ${name}`;

const setSquared = (number) => number**2;

const rectangleArea = (length1, length2) => length1 * length2;

const circleValues = (radius) => [(2*Math.PI*radius), (Math.PI*(radius**2))];

const countVowels = (text) => text.match(/[aeiouAEIOU]/gi).length;

const isSameLength = (arr1, arr2) => arr1.length == arr2.length;

const numberToArray = (number) => number.toString().split('');

const getTruthyFalsyArr = (arr) => {
    const booleanArr = [];
    for (let i = 0; i < arr.length; i++){
        if (arr[i]){
            booleanArr.push(true);
        }
        else{
            booleanArr.push(false);
        }
    }
    return booleanArr;
}

const myArr = [1, "hello", true, 0, false, "", " ", null, undefined, NaN, 2, "world", true, {}, [], 3, "foo", 'true', 'false', "bar"]; 
console.log(helloWorld()); 
console.log(sayHi("Ephraim")); 
console.log(setSquared(4)); 
console.log(rectangleArea(5, 6)); 
console.log(circleValues(1)); 
console.log(countVowels('May the Force be with you. Always')); 
console.log(isSameLength([1, 2, 3, 4], ["3", "aaa", "b", "q"])); 
console.log(numberToArray(12345)); 
console.log(getTruthyFalsyArr(myArr));