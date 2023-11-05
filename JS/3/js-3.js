//findSeashellsIndicies(target, values)

const findSeashellsIndicies = (target, values) => {
    let sum_indexes = 0;
    const arr_indexes = [];

    while (true){
        for (first_index in values) {
            sum_indexes += values[first_index]
            arr_indexes.push(first_index);

            for (second_index in values) {
                if ((sum_indexes + values[second_index]) == target){
                    arr_indexes.push(second_index);
                    return (arr_indexes)
                }
            }

            sum_indexes = 0;
            arr_indexes = [];
        }
    }
}

let target = 30;
let values = [5, 10, 15, 21, 25];

let answer = findSeashellsIndicies(target, values);

console.log(answer)