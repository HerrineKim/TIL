import { Injectable } from '@nestjs/common';
import { UnauthorizedException } from '@nestjs/common/exceptions';
import { CatsRepository } from 'src/cats/cats.repository';
import { LoginRequestDto } from './dto/login.request.dto';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';

@Injectable()
export class AuthService {
  // Repository: 다른 service에서 DB에 접근 가능. module에 등록하여야 service에 DI 가능
  constructor(
    private readonly catsRepository: CatsRepository,
    // auth.module.ts의 JwtModule이 생성한 jwtService를 DI
    // 이것을 사용해 JWT를 만들고, return해 줌
    private jwtService: JwtService,
  ) {}

  // service 함수 구현
  async jwtLogIn(data: LoginRequestDto) {
    const { email, password } = data;

    // * 해당하는 email이 있는지
    const cat = await this.catsRepository.findCatByEmail(email);
    if (!cat) {
      throw new UnauthorizedException('이메일과 비밀번호를 확인해주세요.');
    }

    // * 비밀번호가 일치하는지
    // bcrypt.compare(입력받은 비밀번호, DB에 저장된 비밀번호): promise 반환
    const isPasswordValidated: boolean = await bcrypt.compare(
      password,
      cat.password,
    );

    if (!isPasswordValidated) {
      throw new UnauthorizedException('이메일과 비밀번호를 확인해주세요.');
    }

    // JWT 요소 중 payload에 들어갈 내용
    const payload = { email: cat.email, sub: cat._id };

    return {
      token: this.jwtService.sign(payload),
    };
  }
}
