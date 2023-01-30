function solution(numbers) {
    let strings = numbers.map(num => num + "");
    console.log(strings)

    const answer = strings.sort((a, b) => (b + a) - (a + b))
    console.log(answer)
    return answer[0] === "0" ? "0" : answer;
}

console.log(solution([3, 30, 34, 5, 9]))