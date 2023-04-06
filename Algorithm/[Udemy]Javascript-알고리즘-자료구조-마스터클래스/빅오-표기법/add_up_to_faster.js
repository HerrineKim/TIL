function addUpTo(n) {
  return n * (n + 1) / 2;
}

// 이 함수를 사용하지 않고도 알고리즘의 성능을 측정할 수 있는 것이 빅오 표기법이다.
let t1 = performance.now();
console.log('addUpTo(100000000) >>>', addUpTo(100000000))
let t2 = performance.now();
console.log(`Time Elapsed: ${(t2 - t1) / 1000} seconds.`)