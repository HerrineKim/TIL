# express 싱글톤 패턴, 서비스 패턴

# 싱글톤 패턴

>  객체의 인스턴스가 오직 한 개만 생성되게 하는 패턴. 한 Class로 오직 한 개의 인스턴스만 찍어 내게 함.

## 싱글톤 패턴을 쓰는 이유

> https://tecoble.techcourse.co.kr/post/2020-11-07-singleton/

최초의 한 번의 new 연산자를 통해 고정된 메모리 영역 만을 사용하는 객체를 만들 수 있어 추후 객체에 접근할 때 메모리 낭비를 방지한다. 또, 이미 생성된 인스턴스를 활용하니 속도 측면에서도 이점이 있다고 볼 수 있다.

# 싱글톤 패턴으로 app.ts 설정하기

**app.ts**

```typescript
import * as express from 'express'
import catsRouter from './cats/cats.route'

class Server {
  public app: express.Application

  constructor() {
    const app: express.Application = express()
    this.app = app
  }
  // 라우터 부분
  private setRoute(): void {
    this.app.use(catsRouter)
  }
  // 미들웨어 부분
  private setMiddleware(): void {
    // * logging middleware
    this.app.use((req, res, next) => {
      console.log(req.rawHeaders[1])
      console.log("this is logging middleware")
      next()
    })
    // * JSON parsing middleware
    this.app.use(express.json())
    // * routing middleware
    this.setRoute()
    // * 404 error middleware
    this.app.use((req, res, next) => {
      console.log('this is logging middleware')
      res.send({error: "404 not found error"})
      next()
    })
  }

  public listen() {
    this.setMiddleware()
    this.app.listen(8000, () => {
      console.log('server is on...')
    })
  }
}

function init() {
  const server = new Server()
  server.listen()
}

init()

```



# 서비스 패턴

> `cats.service.ts`로 router에 있는 비즈니스 로직을 분리

## 이런 패턴을 사용하는 이유

1. 가독성을 높이고 유지 보수하기 좋도록 만들기 위해
2. Nest.js에서 이와 같은 패턴을 사용하기 때문(온점을 사용하는 파일 명도 Nest.js 식이다.)

## GET 예시

**cats.service.ts**

```typescript
import {Request, Response} from 'express'
import {Cat, CatType} from '../app.model'

// * READ 고양이 전체 데이터 다 조회 -> GET
export const readAllCat = (req: Request, res: Response) => {
  try {
    const cats = Cat;
    // throw new Error('db connect error');
    res.status(200).send({
      success: true,
      data: {
        cats,
      },
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}
...
```

**cats.route.ts**

```typescript
import {Cat, CatType} from '../app.model'
import {Router} from 'express'
import {readAllCat} from './cats.service'

// 이 router 인스턴스에 라우팅을 쭉 추가해나가는 것
const router = Router();

// * READ 고양이 전체 데이터 다 조회 -> GET
router.get('/cats', readAllCat)
...
```

## 전체 수정



이것이 express의 전부는 아니지만 Nest.js를 사용하기 위한 기본 개념들을 배웠다. 공식 문서에서 추가적인 내용을 공부해보면 좋다.
