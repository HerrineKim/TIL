# NestJS와 DB 연결하기, 환경 변수 설정

[TOC]

> Mongoose의 도움을 받아 MongoDB 사용++ 20.08.30
>
> **mongoose 버전 6.0 이상부터는 useFindAndModify, useCreateIndex 옵션을 설정 안 해주셔도 됩니다!**
>
> https://mongoosejs.com/docs/migrating_to_6.html#no-more-deprecation-warning-options
>
> ### mongoose 설정 옵션 정리
>
> [공식 문서에서 확인하기 - 1](https://mongoosejs.com/docs/connections.html#options)
>
> [공식 문서에서 확인하기 - 2](https://mongoosejs.com/docs/deprecations.html)
>
> \- useNewUrlParser : true
>
>   \- mongodb url을 읽을 수 있도록 설정합니다. 설정하지 않으면 다음과 같은 경고가 뜹니다. DeprecationWarning: current URL string parser is deprecated, and will be removed in a future version. To use the new parser, pass option { useNewUrlParser: true } to MongoClient.connect.
>
> \- useUnifiedTopology : true
>
>   \- 최신 mongodb 드라이버 엔진을 사용하도록 설정합니다. (안정적인 연결을 유지할 수 없는 경우를 제외하고 이 옵션을 true로 설정해야 합니다.)

# 설정하기

## 1. 이전 프로젝트를 그대로 사용

## 2. Mongoose 설치

```bash
$ npm install --save @nestjs/mongoose mongoose
```

## 3. MongooseModule import하기

**app.module.ts**

```typescript
import { MiddlewareConsumer, NestModule, Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CatsModule } from './cats/cats.module';
import { LoggerMiddleware } from './common/middlewares/logger.middleware';
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [CatsModule, MongooseModule.forRoot('mongodb://localhost/nest')],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*');
  }
}
```

## 4. MongoDB 아틀라스 설정

### 4-1. 원하는 Cluster에 Connect

![image-20221227112323144](02-NestJS와-DB-연결하기-환경-변수-설정.assets/image-20221227112323144.png)

### 4-2. Connect your application

![image-20221227112408558](02-NestJS와-DB-연결하기-환경-변수-설정.assets/image-20221227112408558.png)

### 4-3. Connection String 복사해 `app.module.ts`의  DB Url에 붙여 넣고 password 입력해주기

#### **app.module.ts**

```typescript
import { MiddlewareConsumer, NestModule, Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CatsModule } from './cats/cats.module';
import { LoggerMiddleware } from './common/middlewares/logger.middleware';
import { MongooseModule } from '@nestjs/mongoose';

@Module({
  imports: [
    CatsModule,
    MongooseModule.forRoot(
      'mongodb+srv://hyerin:<password>@cluster0.bj1fzji.mongodb.net/cats?retryWrites=true&w=majority',
    ),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*');
  }
}
```

## 5. dotenv로 환경 변수 설정

> Nest.js에서 제공하고 있어 config를 설치한 후 import하면 된다.

### 설치

```bash
$ npm i --save @nestjs/config
```

### **app.module.ts**

```typescript
import { MiddlewareConsumer, NestModule, Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CatsModule } from './cats/cats.module';
import { LoggerMiddleware } from './common/middlewares/logger.middleware';
import { MongooseModule } from '@nestjs/mongoose';
import { ConfigModule } from '@nestjs/config';

@Module({
  imports: [
    ConfigModule.forRoot(),
    CatsModule,
    MongooseModule.forRoot(
      'mongodb+srv://hyerin:!QAZ2wsx@cluster0.bj1fzji.mongodb.net/cats?retryWrites=true&w=majority',
    ),
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*');
  }
}
```

### 루트에서 `.env` 파일 생성

`MONGODB_URI = 주소`

**app.module.ts** 수정

```typescript
@Module({
  imports: [
    ConfigModule.forRoot(),
    MongooseModule.forRoot(process.env.MONGODB_URI),
    CatsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
```

### `.env` 파일과 `main.ts`파일에 Port 설정

#### **main.ts**

```typescript
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { HttpExceptionFilter } from './common/exceptions/http-exception.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  app.useGlobalFilters(new HttpExceptionFilter());
  const PORT = process.env.PORT || 8000;
  await app.listen(PORT);
}
bootstrap();
```

## 6. Nest.js-MongoDB 연결 관련 설정

### **app.module.ts**

```typescript
...
@Module({
  imports: [
    ConfigModule.forRoot(),
    MongooseModule.forRoot(process.env.MONGODB_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    }),
    CatsModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*');
  }
}
```

