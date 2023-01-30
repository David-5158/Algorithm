function solution(number, limit, power) {
    var divisor = []
    for (let i = 1; i <= number; i++) {
        let check = 0
        for (let j = 1; j <= i / 2; j++) {
            if (i % j === 0) {
                check += 1
            }


        }
        divisor.push(check + 1)
    }
    return divisor.map((n) => {
        return n > limit ? power : n;
    }).reduce((acc, item) => acc + item, 0);
}

console.log(solution(5, 3, 2))