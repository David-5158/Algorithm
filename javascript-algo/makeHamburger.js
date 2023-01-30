function solution(ingredient) {
    let count = 0;

    for (let i = 0; i < ingredient.length; i++) {
        console.log("ingredient :   ", ingredient)
        console.log("i : ", i)
        if (ingredient.slice(i, i + 4).join('') === '1231') {
            count++;
            ingredient.splice(i, 4);
            i -= 3;
        }
    }

    return count;
}
console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
console.log(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))