# Providers & 의존성 주입(DI)

## 개요

**app.controller.ts 초기 버전**

```typescript
import { Controller, Get, Req, Body } from '@nestjs/common';
import { Param } from '@nestjs/common/decorators';
import { Request } from 'express';
import { AppService } from './app.service';

@Controller('cats')
export class AppController {
  // 이러한 패턴을 의존성 주입 패턴이라고 한다.
  constructor(private readonly appService: AppService) {}

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

AppController를 소비자, AppService를 제품이라고 생각하자. 제품을 생산하는 Provider가 따로 있으며, 우리는 제품을 소비자 입장에서 사용하고 있다.

서비스, 리포지토리, 팩토리, 도우미 등 기본 Nest 클래스의 대부분은 공급자로 취급될 수 있다고 공식 문서에 적혀 있다. 공급자는 이런 종속성이 있는 제품들을 주입시킬 수 있다. 코드를 보자.

**app.module.ts**

```typescript
import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
```

여기서 AppService를 제거하면 'AppController'의 의존성이 resolve되지 않았다는 오류가 나온다.

Nest.js는 Service를 등록하면 그 Service의 Provider(지금은 AppService) 찾아가서 제품을 찾아서 소비자에게 넘겨 준다. 그런데 module에서 공급자를 제거했으므로 controller에서 제품을 사용할 수 없게 된 것이다. module 안에 사업자 등록을 해 준다고 생각하면 된다. 공급자로 취급되는 것들은 `@Injectable()` 데코레이터가 앞에 붙는다.

app.module에서 사업자 등록이 되어 있으면, 소비자인 controller가 공급된 제품을 인스턴스로 받아서 사용하라 수 있게 되는 것이다. 이것이 기본적인 Provider와 DI 패턴이다.

이렇게 하는 이유는 실전 프로젝트를 하면서 많이 느낄 수 있다. 객체 지향 프로그래밍의 목표가 바로 실생활과 유사하게 코드를 짠다는 것이다. 이렇게 함으로써 유지 보수도 쉽고 확장성 있게 프로그램을 관리할 수 있다.