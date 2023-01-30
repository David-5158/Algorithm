function solution(k, score) {
    var answer = [];
    var stack = [];
    for (let i = 0; i < score.length; i++) {
        console.log("stack.length : ", stack.length)
        console.log("i : ", i)
        if (stack.length < k) {
            stack.push(score[i]);
            console.log("stack : ", stack)
            console.log("log", Math.min(...stack))
            answer.push(Math.min(...stack));
        } else {
            stack.sort((a, b) => b - a);
            console.log("length>k : ", stack)
            console.log("stack[-1] : ", stack[stack.length - 1])
            if (stack[stack.length - 1] < score[i]) {
                stack.pop();
                stack.push(score[i]);
                answer.push(Math.min(...stack));
            } else {
                answer.push(Math.min(...stack));
            }

        }

    }
    return answer;
}

console.log(solution(3, [10, 100, 20, 150, 1, 100, 200]))