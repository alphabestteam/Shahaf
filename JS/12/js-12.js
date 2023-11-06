const student1 = {
    name: 'Shahaf',
    age: 19,
    grades: [100, 95, 92, 90, 98],
    avgGrades: function() {
        vowelCount = this.name.match(/[aeiouAEIOU]/gi).length;
        let sum = 0;
        for (let i = 0; i < this.grades.length; i++){
            sum += this.grades[i];
        }

        avg = sum / this.grades.length;
        return (avg + vowelCount);
    }
}

const student2 = {
    name: 'Matan',
    age: 19,
    grades: [100, 85, 100, 98, 97],
    avgGrades: function() {
        vowelCount = this.name.match(/[aeiouAEIOU]/gi).length;
        let sum = 0;
        for (let i = 0; i < this.grades.length; i++){
            sum += this.grades[i];
        }

        avg = sum / this.grades.length;
        return (avg + vowelCount);
    }
}

const student3 = {
    name: 'Koral',
    age: 18,
    grades: [92, 81, 96, 90, 89],
    avgGrades: function() {
        vowelCount = this.name.match(/[aeiouAEIOU]/gi).length;
        let sum = 0;
        for (let i = 0; i < this.grades.length; i++){
            sum += this.grades[i];
        }

        avg = sum / this.grades.length;
        return (avg + vowelCount);
    }
}

const student4 = {
    name: 'Gilad',
    age: 17,
    grades: [83, 95, 98, 79, 100],
    avgGrades: function() {
        vowelCount = this.name.match(/[aeiouAEIOU]/gi).length;
        let sum = 0;
        for (let i = 0; i < this.grades.length; i++){
            sum += this.grades[i];
        }

        avg = sum / this.grades.length;
        return (avg + vowelCount);
    }
}

const student5 = {
    name: 'Maya',
    age: 19,
    grades: [98, 91, 100, 86, 88],
    avgGrades: function() {
        vowelCount = this.name.match(/[aeiouAEIOU]/gi).length;
        let sum = 0;
        for (let i = 0; i < this.grades.length; i++){
            sum += this.grades[i];
        }

        avg = sum / this.grades.length;
        return (avg + vowelCount);
    }
}

const students = [student1, student2, student3, student4, student5];

for (let i = 0; i < students.length; i++){
    console.log(`index ${i}`);
    console.log(`name: ${students[i].name}`);
    console.log(`age: ${students[i].age}`);
    console.log(`grades: ${students[i].grades}`);
    console.log(`avg: ${students[i].avgGrades()}`);
}

const adults = students.filter(student => student.age >= 18);
console.log(adults);

const myCar = {
    manufacturer: 'Hyundai',
    model: 'i10',
    year: 2020,
    age: function(){
        const now = new Date();
        return now.getFullYear() - this.year;
    }
}

console.log(`manufacturer: ${myCar.manufacturer}`);
console.log(`model: ${myCar.model}`);
console.log(`year: ${myCar.year}`);
console.log(`age: ${myCar.age()}`);