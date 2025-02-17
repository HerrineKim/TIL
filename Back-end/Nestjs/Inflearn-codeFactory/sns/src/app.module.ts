// module: 여러 개의 컨트롤러와 서비스를 그룹화하는 기능. 일반적으로 기능 별로 만든다.
// 싱글톤이기에 모듈 내에서 선언된 인스턴스는 앱 전체에서 사용 가능.
// controller: 엔드포인트를 정의하는 기능. 요청을 처리하고 응답을 반환하는 기능.
// service: DB 조회, 수정, 삭제 등의 기능을 정의하는 기능. 선언된 인스턴스는 앱 전체에서 사용 가능.

import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PostsModule } from './posts/posts.module';

@Module({
  imports: [PostsModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
