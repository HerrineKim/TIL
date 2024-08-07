import { Injectable } from '@nestjs/common';
import { AuthGuard } from '@nestjs/passport';

@Injectable()
// AuthGuard: strategy를 자동으로 실행
export class JwtAuthGuard extends AuthGuard('jwt') {}
