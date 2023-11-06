//with arr.at(index) we have more features and it is newer, for example we can access the last item with arr.at(-1)

//2
function arrLetters(number, letter){
    arr = []
    for (let i = 0; i < number; i++){
        arr.push(letter);
    }
    return arr;
}

//3
function deleteN (n, arr){
    for (let i = 0; i < n; i++){
        arr.pop();
    }
    return arr;
}

//4
function unshiftNumber (number, arr){
    arr.unshift(number);
    return arr;
}

//5
function concatArrs (arr1, arr2){
    arr1.concat(arr2);
    return arr1;
}

//6
function arrUpperCase (arr){
    const upper_arr = arr.map(toUpperCase());
    return upper_arr;
}

//7
function doubleDigit (arr){
    const new_arr = arr.filter(isDoubledigit);
    return new_arr;
}

function isDoubledigit(number){
    return ((number >= 10) && (number <= 99));
}

//8
function isInArray (arr, value){
    return arr.includes(value);
}

//9
function biggerThan10 (arr){
    return arr.find(isBiggerThan10);
}

function isBiggerThan10 (value){
    return (value > 10);
}

//10
function isBiggerThan10Exists (arr){
    return (biggerThan10(arr) != undefined);
}

//11
// sort() will sort an array correctly only for strings because for numbers it will say that 3 is bigger than 1 even if the numbers are 30 and 100.
// to sort numbers we will have to use a function to sort the array.

//12
//array.sort(function(number_one, number_two){return number_one - number_two});

//13
function arrayToString (arr){
    return arr.join("**");
}

//14
function alphabeticArray (arr){
    return arr.sort()
}

//15
function everyArray (arr, value){
    arr.every(isSmaller, value)
}

function isSmaller (arr_value, value){
    return (value > arr_value);
}

//16
function isExistBigger (arr, number){
    if (arr.every(isSmaller, number)){
        return false;
    }
    else{
        return true;
    }
}