// 아키텍쳐란: 효율적인 코드를 작성하기 위한 구조
// 컨트롤러는 요청을 받고, 서비스는 요청을 처리하는 역할
// 서비스는 비즈니스 로직을 작성하는 곳
// 데이터베이스와 연결되는 로직은 서비스에 작성

// Nest.js에서는 컨트롤러를 복잡하게 만들지 않고, 서비스에 비즈니스 로직을 작성하여 컨트롤러에서 호출하는 방식을 사용하라고 권장함.
import { Injectable, NotFoundException } from '@nestjs/common';

export interface PostModel {
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

@Injectable()
export class PostsService {
  getAllPosts() {
    return posts;
  }

  getPostById(id: number) {
    const post = posts.find((post) => post.id === +id);
    if (!post) {
      throw new NotFoundException('Post not found');
    }
    return post;
  }

  createPost(author: string, title: string, content: string) {
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

  updatePost(postId: number, author: string, title: string, content: string) {
    const post = posts.find((post) => post.id === postId);
    if (!post) {
      throw new NotFoundException('Post not found');
    }

    if (author) {
      post.author = author;
    }

    if (title) {
      post.title = title;
    }

    if (content) {
      post.content = content;
    }

    return post;
  }

  deletePost(postId: number) {
    const post = posts.find((post) => post.id === postId);
    if (!post) {
      throw new NotFoundException('Post not found');
    }
    posts.splice(
      posts.findIndex((post) => post.id === postId),
      1,
    );
    return postId;
  }
}
