# NestjJS 구조 & Controller 패턴

# `package.json` 설명

1. `reflect-metadata`: 데코레이터를 사용할 때 쓰는 패키지
2. `rimraf`: Linux의 rm -rf 등의 명령어를 Windows에서도 사용할 수 있도록 해줌
3. `rxjs`: 비동기 및 이벤트 기반 프로그래밍을 하기 위한 도구



# 컨트롤러

들어오는 요청을 처리하고 클라이언트에 응답을 반환한다. 

**app.controller.ts**

```typescript
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

// 이 클래스 안에서 서비스를 사용할 수 있게 해주는 decorator
@Controller()
export class AppController {
  // 의존성 주입하는 부분(다음 문서에서 설명)
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    // return 'hello world';
    // 둘은 같다.
    return this.appService.getHello();
  }
}
```



## 라우팅

`@Controller()` 데코레이터 안에 경로를 지정하여 그룹화하고, 경로의 해당 부분을 service가 반복할 필요 없게 해줄 수 있다.

**app.controller.ts**

```typescript
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller('cats')
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
```

또, 메서드 데코레이터 안에도 그 다음에 올 경로를 지정해 줄 수 있다.

```typescript
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller('cats')
export class AppController {
  constructor(private readonly appService: AppService) {}

  // * localhost:8000/cats/hello
  @Get('hello')
  getHello(): string {
    return this.appService.getHello();
  }
}
```



## 요청 개체

> express에서 Request, Response 개체를 인자로 받았었다. Nest.js에서는 Decorator 패턴을 사용해 요청 개체를 처리한다.

```typescript
import { Controller, Get, Req, Body } from '@nestjs/common';
import { Param } from '@nestjs/common/decorators';
import { Request } from 'express';
// import { AppService } from './app.service';

@Controller('cats')
export class AppController {
  // constructor(private readonly appService: AppService) {}

  @Get('hello/:id')
  getHello(
    @Req() req: Request,
    @Body() Body,
    @Param() param: { id: string },
  ): string {
    // console.log(req);
    console.log(param);
    return 'Hello World!';
    // return this.appService.getHello();
  }
}
```

- Nest.js는 Body를 `req.body`와 같은 형태로 받을 수도 있지만, 인자에서 바로 받을 수도 있다. 책임을 완전히 분리하는 의미가 있다.
- Param 객체를 사용해 동적 라우팅이 가능하다.
- params의 type을 지정할 수 있다. 그러나 이보다는 [DTO(Data Transfer Object)](https://resilient-923.tistory.com/356)를 사용해 body를 검증하는 방법이 더 좋다.