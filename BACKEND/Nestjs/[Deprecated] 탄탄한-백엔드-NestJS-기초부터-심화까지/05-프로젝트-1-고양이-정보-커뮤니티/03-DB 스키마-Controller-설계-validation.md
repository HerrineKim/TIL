# DB 스키마, Controller 설계 & validation

[TOC]

# Mongoose 로그 & dev 모드 세팅하기

## `app.module.ts`

```typescript
...
import * as mongoose from 'mongoose';
...
export class AppModule implements NestModule {
  private readonly isDev: boolean = process.env.MODE === 'dev' ? true : false;
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*');
    mongoose.set('debug', this.isDev);
  }
}
```



# Schema 만들기

> https://docs.nestjs.com/techniques/mongodb

## 순서

1. mongoose로부터 Document(key와 value로 이루어진 BSON 데이터)를 상속 받아 class 정의
2. class를 schema로 바꾸기
3. schema option 지정 후 인자로 넣어 주기
4. @Prop() 데코레이터를 이용해 컬럼 정의

## `cats.schema.ts`

```typescript
import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document, SchemaOptions } from 'mongoose';

const options: SchemaOptions = {
  // DB에서 하나가 만들어지거나 수정될 때마다 시간을 찍어 줌
  timestamps: true,
};

@Schema(options)
// mongoose의 Document를 상속받음
export class Cat extends Document {
  // 컬럼 정의
  @Prop({
    required: true,
    unique: true,
  })
  email: string;

  @Prop({ required: true })
  catName: string;

  @Prop({ required: true })
  password: string;

  @Prop({ required: true })
  imgUrl: string;
}

// Cat이라는 class를 schema로 만들어 줌
export const CatSchema = SchemaFactory.createForClass(Cat);
```



# Validation

> https://github.com/typestack/class-validator

## 1. Nest.js에서 제공하는 Class validator 라이브러리 설치

```bash
$ npm i --save class-validator class-transformer
```

## 2. 각 컬럼에 validation 적용

```typescript
...
@Schema(options)
// mongoose의 Document를 상속받음
export class Cat extends Document {
  // 컬럼 정의
  @Prop({
    required: true,
    unique: true,
  })
  @IsEmail()
  @IsNotEmpty()
  email: string;

  @Prop({ required: true })
  @IsString()
  @IsNotEmpty()
  name: string;

  @Prop({ required: true })
  @IsString()
  @IsNotEmpty()
  password: string;

  @Prop({ required: true })
  @IsString()
  @IsNotEmpty()
  imgUrl: string;
}
...
```

## 3. main.ts에 Pipe 적용

```typescript
import { ValidationPipe } from '@nestjs/common/pipes';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';
import { HttpExceptionFilter } from './common/exceptions/http-exception.filter';

async function bootstrap() {
  const app = await NestFactory.create(AppModule);
  // ValidationPipe
  app.useGlobalPipes(new ValidationPipe());
  app.useGlobalFilters(new HttpExceptionFilter());
  const PORT = process.env.PORT || 8000;
  await app.listen(PORT);
}
bootstrap();
```

