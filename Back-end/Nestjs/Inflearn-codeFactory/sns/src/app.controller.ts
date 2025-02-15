import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

/**
 * author: string;
 * title: string;
 * content: string;
 * likeCount: number;
 * commentCount: number;
 */

interface Post {
  author: string;
  title: string;
  content: string;
  likeCount: number;
  commentCount: number;
}

// 엔드포인트 생성
@Controller('post')
export class AppController {
  constructor(private readonly appService: AppService) {}

  // 중첩 엔드포인트 생성
  @Get()
  getPost(): Post {
    // json 형식으로 반환
    return {
      author: 'cillian_murphy',
      title: 'Dinner',
      content: 'I had a great dinner at the restaurant last night.',
      likeCount: 100000,
      commentCount: 9999,
    };
  }
}
