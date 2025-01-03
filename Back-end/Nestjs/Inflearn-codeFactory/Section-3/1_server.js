// = import http from 'http';
const http = require('http');

// localhost -> 127.0.0.1 -> loop back -> 서버를 실행한 컴퓨터 자신을 가리키는 주소
const host = 'localhost';
const port = 3000;

// req -> request -> 요청
// res -> response -> 응답
const server = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('<h1>Hello World</h1>');
});

// 어디에서 실행하는지 알려주는 것
server.listen(port, host, () => {
  console.log(`Server running at http://${host}:${port}`);
});
