import {
  Controller,
  Get,
  Param,
  NotFoundException,
  Post,
  Body,
} from '@nestjs/common';
import { PostsService } from './posts.service';

interface PostModel {
  id: number;
  author: string;
  title: string;
  content: string;
  likeCount: number;
  commentCount: number;
}

const posts: PostModel[] = [
  {
    id: 1,
    author: 'cillian_murphy',
    title: 'Dinner',
    content: 'I had a great dinner at the restaurant last night.',
    likeCount: 100000,
    commentCount: 9999,
  },
  {
    id: 2,
    author: 'cillian_murphy',
    title: 'filming',
    content: 'I am filming a new movie.',
    likeCount: 100000,
    commentCount: 9999,
  },
  {
    id: 3,
    author: 'cillian_murphy',
    title: 'Peaky Blinders',
    content: 'Yay!',
    likeCount: 100000,
    commentCount: 9999,
  },
];
@Controller('posts')
export class PostsController {
  constructor(private readonly postsService: PostsService) {}

  // 1) GET /posts
  //    모든 posts를 가져온다.
  @Get()
  getPosts(): PostModel[] {
    return posts;
  }

  // 2) GET /posts/:id
  //    특정 post를 가져온다.
  @Get(':id')
  getPost(@Param('id') id: string): PostModel {
    const post = posts.find((post) => post.id === parseInt(id));
    if (!post) {
      throw new NotFoundException('Post not found');
    }
    return post;
  }

  // 3) POST /posts
  //    새로운 post를 생성한다.

  @Post()
  postPosts(
    @Body('author') author: string,
    @Body('title') title: string,
    @Body('content') content: string,
  ): PostModel {
    const post: PostModel = {
      id: posts[posts.length - 1].id + 1,
      author,
      title,
      content,
      likeCount: 0,
      commentCount: 0,
    };
    posts.push(post);
    return post;
  }

  // 4) PUT /posts/:id
  //    특정 post를 수정한다.

  // 5) DELETE /posts/:id
  //    특정 post를 삭제한다.
}
