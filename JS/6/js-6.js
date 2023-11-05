function evalNumbers(number_one, number_two, operator){
    if (operator == 'add'){
        console.log(`Sum of ${number_one} and ${number_two} is ${number_one + number_two}`)
    }
    else if (operator == 'Subtract'){
        console.log(`Difference of ${number_one} and ${number_two} is ${number_one - number_two}`)
    }
    else if (operator == 'multiply'){
        console.log(`Product of ${number_one} and ${number_two} is ${number_one * number_two}`)
    }
    else if (operator == 'divide'){
        console.log(`Division of ${number_one} and ${number_two} is ${number_one / number_two}`)
    }
    else if (operator == 'modulus'){
        console.log(`Modulus of ${number_one} and ${number_two} is ${number_one % number_two}`)
    }
    else{
        console.log("Invalid value")
    }
}

let number_one = 8;

let number_two = 2;

let operator = 'add'

console.log(evalNumbers(number_one, number_two, operator))