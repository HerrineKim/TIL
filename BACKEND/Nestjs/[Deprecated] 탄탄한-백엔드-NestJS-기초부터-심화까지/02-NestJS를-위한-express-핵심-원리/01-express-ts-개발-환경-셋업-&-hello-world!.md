# express-ts-개발-환경-셋업-&-hello-world!

[TOC]

# 실습(`/letsStart`)

## 준비

1. `npm i`
2. 서버 실행: `npm run start:dev`
   1. 앞으로 express를 사용하면서 이런 방식으로 열게 된다.
   2. `tsx watch` 옵션에 따라 코드가 변화하면 실시간으로 컴파일 해준다.
3. `npm run start`
   1. prestart 명령어가 먼저 실행되어 tsconfig.json에 설정된 옵션에 따라 `dist` 폴더에 컴파일된 결과물이 나온다.
   2. node가 결과물 중 app.js 파일을 실행한다.
4. express 설치
   1. `npm i express --save`
   2. `npm i express @types/express -D` ('-D' 플래그를 포함하면 devDependencies 라이브러리로 포함되어 배포 버전에는 포함되지 않아 빌드 시간을 줄여 준다.)

## 서버 실행

`npm run start:dev`

**app.ts**

```typescript
import * as express from 'express';

// app: 서버 역할, express의 인스턴스
const app: express.Express = express()
const port: number = 8000

// get(): 서버에 요청이 들어왔을 때 어떤 동작을 할지 정의하는 라우터
app.get('/', (req, res) => {
  console.log(req)
  res.send('Hello World!')})

// listen(): 서버를 실행하는 메서드
app.listen(port, () => console.log(`Example app listening on port http://localhost:${port}`))
```

**port**

- Port(포트)**란 IP 내에서 **애플리케이션 상호 구분(프로세스 구분)을 위해 사용하는 번호**이다.
- **포트 숫자**는 IP 주소가 가리키는 PC에 접속할 수 있는 통로(채널)을 의미한다.
- **터미널에서 React를 실행**하면 나타나는 화면에는, **로컬 PC의 IP 주소**인 127.0.0.1 뒤에 :3000과 같은 **숫자가 표현**된다.
- **React를 실행했을 때**에는 **로컬 PC의 IP 주소**로 접근하여, **3000번의 통로**를 통해 실행 중인 **React를 확인**할 수 있다.
- **이미 사용 중인 포트**는 **중복해서 사용할 수 없다.**
- 만약 다른 프로그램에서 **3000번 포트를 사용 중**이라면, **3001번 포트 번호로 React가 실행**된다.
- **포트 번호**는 **0~ 65,535 까지 사용할 수 있다.**
- 그 중에서 **0 ~ 1024번까지의 포트 번호**는 주요 통신을 위한 규약에 따라 **이미 정해져 있다.**



