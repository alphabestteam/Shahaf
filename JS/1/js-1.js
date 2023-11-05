alert("Patrick went missing, go find him!")

if (confirm("Are you going to find him now?") == true){
    alert("Spongebob is going to find Patrik!")
}

let answer = prompt("Did you find Patrik?")

while (answer != null){
    if (answer == 'yes'){
        alert("Spongebob found Patrik!")
        break
    }
    else{
        answer = prompt("Did you find Patrik?")
    }
}