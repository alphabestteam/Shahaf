//with arr.at(index) we have more features and it is newer, for example we can access the last item with arr.at(-1)

//2
function arrLetters(number, letter){
    arr = []
    for (let i = 0; i < number; i++){
        arr.push(letter);
    }
    return arr;
}

let char = 'A'
let number = 3
console.log(arrLetters(number, char))

//3
function deleteN (n, arr){
    if (n < arr.length){
        for (let i = 0; i < n; i++){
            arr.pop();
        }
        return arr;
    }
    else{
        console.log(`cannot delete ${n} values from array`);
    }
}

let n = 4;
const pop_array = [1, 2, 3, 4, 5, 6, 7, 8];
console.log(deleteN(n, pop_array));

//4
function unshiftNumber (number, arr){
    arr.unshift(number);
    return arr;
}

let push_number = 8;
console.log(unshiftNumber(push_number, pop_array));

//5
function concatArrs (arr1, arr2){
    new_arr = arr1.concat(arr2);
    return new_arr;
}

const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
console.log(concatArrs(arr1, arr2));

//6
function arrUpperCase (arr){
    const upper_arr = arr.map(value => value.toUpperCase());
    return upper_arr;
}

const lower_arr = ['love', 'a', 'shahaf'];
console.log(arrUpperCase(lower_arr));

//7
function doubleDigit (arr){
    const new_arr = arr.filter(isDoubledigit);
    return new_arr;
}

const digits_arr = [1, 23, 55, 7];
console.log(doubleDigit(digits_arr));

function isDoubledigit(number){
    return ((number >= 10) && (number <= 99));
}

//8
function isInArray (arr, value){
    return arr.includes(value);
}

let in_arr_value = 'shahaf';
console.log(isInArray(lower_arr, in_arr_value))

//9
function biggerThan10 (arr){
    return arr.find(isBiggerThan10);
}

const bigger_10_arr = [1, 4, 11, 3];
console.log(biggerThan10(bigger_10_arr));

function isBiggerThan10 (value){
    return (value > 10);
}

//10
function isBiggerThan10Exists (arr){
    return (biggerThan10(arr) != undefined);
}

console.log(isBiggerThan10Exists(bigger_10_arr));

//11
// sort() will sort an array correctly only for strings because for numbers it will say that 3 is bigger than 1 even if the numbers are 30 and 100.
// to sort numbers we will have to use a function to sort the array.

//12
//array.sort(function(number_one, number_two){return number_one - number_two});

//13
function arrayToString (arr){
    return arr.join("**");
}

const string_arr = ['a', 3, 'abba', 66];
console.log(arrayToString(string_arr));

//14
function alphabeticArray (arr){
    return arr.sort()
}

const alphabetic_array = ['shahaf', 'maya', 'koral'];
console.log(alphabeticArray(alphabetic_array));

//15
function everyArray (arr, value){
    return arr.every(arr_value => isSmaller(arr_value, value))
}

const is_smaller_array = [1, 2, 3, 4, 5, 6];
value = 10;
console.log(everyArray(is_smaller_array, value));

function isSmaller (arr_value, value){
    return (arr_value < value);
}

//16
function isExistBigger (arr, number){
    if (arr.every(arr_value => isSmaller(arr_value, value))){
        return false;
    }
    else{
        return true;
    }
}

console.log(isExistBigger(is_smaller_array, value))