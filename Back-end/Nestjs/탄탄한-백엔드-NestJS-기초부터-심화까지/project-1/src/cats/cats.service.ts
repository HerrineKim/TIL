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
