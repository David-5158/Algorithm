function solution(s) {
    let answer = 0;
    let check = []
    for (let i = 0; i < s.length; i++) {
        check.push(s[i]);

        const same = check.filter((item) => item === check[0]);
        const notSame = check.filter((item) => item !== check[0]);

        if (same.length === notSame.length) {
            answer += 1;
            check = [];
        }
    }
    if (check.length !== 0) {
        answer += 1;
    }

    return answer
}
console.log(solution("abracadabra"))