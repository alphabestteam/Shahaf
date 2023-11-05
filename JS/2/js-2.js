//isSufficientFuel(distance, literPerKm, fuelLeft)

const isSufficientFuel = (distance, literPerKm, fuelLeft) => ((literPerKm * fuelLeft) >= distance)

let distance = 10
let literPerKm = 3
let fuelLeft = 40

let answer = isSufficientFuel(distance, literPerKm, fuelLeft)

console.log(answer)