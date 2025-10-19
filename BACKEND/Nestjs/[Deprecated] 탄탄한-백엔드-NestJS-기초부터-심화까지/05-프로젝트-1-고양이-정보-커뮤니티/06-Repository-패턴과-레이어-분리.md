# Repository 패턴과 레이어 분리

> 레포지토리 패턴은 필수는 아니다. 상황에 따라 적용하는 걸 추천 

[TOC]

# Repository 패턴

클라이언트 - 서비스 - 데이터베이스로 이어지던 패턴에서 서비스와 데이터베이스 사이에 중개자가 있는 패턴

## 장점

만약 A 서비스와 B 서비스가 서로를 참조하는 상황이 있다면, 순환 참조가 일어나게 된다. 순환 참조를 해결할 수는 있지만, 가독성이 떨어지게 된다.

레포지토리가 있다면 다른 서비스에서 레포지토리만 참조하면 되기 때문에 각 모듈(서비스)에서 각자의 비즈니스 로직에만 집중할 수 있게 되고, 모듈 간의 책임 분리가 확실해진다.

## Repository 패턴의 핵심

서비스 레이어에서 데이터의 출처와 관계 없이 동일한 방식으로 데이터를 접근할 수 있도록 하는 것이다. 만약 우리 서비스에 데이터베이스가 MongoDB 외에도 여러 개가 있다고 하자. 그러면 각 데이터베이스에 접근할 때 사용해야 하는 쿼리가 각각 다를 것이다. 그런데 레포지토리가 중간에서 쿼리를 다듬어주어 서비스 단에서 어떤 데이터베이스에 접근하든지 동일한 방식으로 진행할 수 있게 된다. 

데이터베이스를 추가하는 경우 뿐만 아니라, 다른 데이터베이스로 교체하는 경우에도 레포지토리만 바꿔 주고 서비스에서는 함수로 불러 오면 된다.

## 실습

### cats.repository.ts 파일 생성

> 레포지토리 역시 의존성 주입이 가능한 클래스다. 서비스가 레포지토리로부터 DI를 받아 사용하게 된다.

```typescript
import { HttpException, Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { Cat } from './cats.schema';
import { CatRequestDto } from './dto/cats.request.dto';

@Injectable()
export class CatsRepository {
  constructor(@InjectModel(Cat.name) private readonly catModel: Model<Cat>) {}
  // Service에서 구현했던 isCatExist 함수와 같은 함수를 만들기
  async existsByEmail(email: string): Promise<boolean> {
    try {
      const result = await this.catModel.exists({ email });
      return result;
    } catch (error) {
      throw new HttpException('db error', 400);
    }
  }
  // create도 만들기
  async create(cat: CatRequestDto): Promise<Cat> {
    return await this.catModel.create(cat);
  }
}

```

### cats.module.ts에 등록하기

```typescript
import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';
import { Cat, CatSchema } from './cats.schema';
import { CatsRepository } from './cats.repository';

@Module({
  imports: [MongooseModule.forFeature([{ name: Cat.name, schema: CatSchema }])],
  controllers: [CatsController],
  providers: [CatsService, CatsRepository],
  exports: [CatsService],
})
export class CatsModule {}
```

### cats.service.ts에 DI하기

```typescript
import { Injectable, UnauthorizedException } from '@nestjs/common';
// import { HttpException } from '@nestjs/common/exceptions';
// import { InjectModel } from '@nestjs/mongoose';
// import { Model } from 'mongoose';
// import { Cat } from './cats.schema';
import { CatRequestDto } from './dto/cats.request.dto';
import * as bcrypt from 'bcrypt';
import { CatsRepository } from './cats.repository';

@Injectable()
export class CatsService {
  // DB에 저장하기 위해 schema를 사용하고자 DI처리
  constructor(private readonly catsRepository: CatsRepository) {}
  // DTO 객체를 받는다.
  async signUp(body: CatRequestDto) {
    const { email, name, password } = body;
    // email이 DB에 존재하는지 확인 한 후,
    // const isCatExist = await this.catModel.exists({ email });
    const isCatExist = await this.catsRepository.existsByEmail(email);
    // exception 처리를 한다.
    if (isCatExist) {
      // == throw new HttpException('이미 존재하는 고양이입니다.', 403);
      throw new UnauthorizedException('이미 존재하는 고양이입니다.');
    }
    // 비밀번호 암호화
    const hashedPassword = await bcrypt.hash(password, 10);
    // DB에 저장
    const cat = await this.catsRepository.create({
      email,
      name,
      password: hashedPassword,
    });
    // 저장된 cat 객체를 리턴
    return cat.readOnlyData;
  }
}
```

