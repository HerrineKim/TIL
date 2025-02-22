// 아키텍쳐란: 효율적인 코드를 작성하기 위한 구조
// 컨트롤러는 요청을 받고, 서비스는 요청을 처리하는 역할
// 서비스는 비즈니스 로직을 작성하는 곳
// 데이터베이스와 연결되는 로직은 서비스에 작성

// Nest.js에서는 컨트롤러를 복잡하게 만들지 않고, 서비스에 비즈니스 로직을 작성하여 컨트롤러에서 호출하는 방식을 사용하라고 권장함.
import { Injectable } from '@nestjs/common';

@Injectable()
export class PostsService {}
