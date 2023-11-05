let para = document.createElement(`p`);


function verbalDescription(){
    const grade = parseInt(document.getElementById("grade").value);
    let letter_grade = ' ';

    if (grade != NaN){
        if (grade == 100){
            letter_grade = "A+";
        }

        else if ((grade <= 99) && (grade >=90)){
            letter_grade = "A";
        }

        else if ((grade <= 89) && (grade >=80)){
            letter_grade = "B";
        }

        else if ((grade <= 79) && (grade >=70)){
            letter_grade = "C";
        }

        else if ((grade <= 69) && (grade >=60)){
            letter_grade = "D";
        }

        else if ((grade <= 59) && (grade >=50)){
            letter_grade = "E";
        }

        else if (grade < 50){
            letter_grade = "F";
        }
    }

    else{
        para.innerText = "Invalid value";
        return;

    }

    switch(letter_grade){
        case "A+":
            para.innerText = "Perfect!";
            break;

        case "A":
            para.innerText = "Amazing!";
            break;

        case "B":
            para.innerText = "Nicely done!";
            break;

        case "C":
            para.innerText = "This is fine!";
            break;

        case "D":
            para.innerText = "You can do better!";
            break;

        case "E":
            para.innerText = "Moed B is an option!";
            break;

        case "F":
            para.innerText = "Moed B is a must!";
            break;
    }
    document.getElementById("parent").appendChild(para);
}

let button = document.getElementById("button");
button.addEventListener("click", verbalDescription);