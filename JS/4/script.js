/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/


function starSign(date){
    let month = date.getMonth()
    let day = date.getDate()

    switch(month){
        case 0:
            if (day <= 20){
                return "Capricon"
            }
            else{
                return "Aquarius"
            }

        case 1:
            if (day <= 19){
                return "Aquarius"
            }
            else{
                return "Pisces"
            }

        case 2:
            if (day <= 20){
                return "Pisces"
            }
            else{
                return "Aries"
            }

        case 3:
            if (day <= 20){
                return "Aries"
            }
            else{
                return "Taurus"
            }

        case 4:
            if (day <= 21){
                return "Taurus"
            }
            else{
                return "Gemini"
            }

        case 5:
            if (day <= 21){
                return "Gemini"
            }
            else{
                return "Cancer"
            }

        case 6:
            if (day <= 22){
                return "Cancer"
            }
            else{
                return "Leo"
            }

        case 7:
            if (day <= 23){
                return "Leo"
            }
            else{
                return "Virgo"
            }

        case 8:
            if (day <= 23){
                return "Virgo"
            }
            else{
                return "Libra"
            }

        case 9:
            if (day <= 23){
                return "Libra"
            }
            else{
                return "Scorpio"
            }

        case 10:
            if (day <= 22){
                return "Scorpio"
            }
            else{
                return "Sagittarius"
            }

        case 11:
            if (day <= 21){
                return "Sagittarius"
            }
            else{
                return "Capricon"
            }
    }
}

const date = new Date("2022-03-25")

let answer = starSign(date)

console.log(answer)