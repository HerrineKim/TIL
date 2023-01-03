# Multer와 미디어 파일 서비스(mp3, mp4, img 등)

> https://docs.nestjs.com/techniques/file-upload#file-upload
>
> **- 다음 보충 강의에 프런트엔드 코드 없이 postman에서 미디어 파일을 업로드하는 방법도 확인해 주세요. :)**
>
> - nodejs 공식 문서 : https://nodejs.org/api/path.html
>
> 디폴트 이미지 주소는 아래의 주소를 사용하시면 됩니다.
>
> - [https://raw.githubusercontent.com/amamov/teaching-nestjs-a-to-z/main/images/1.jpeg](https://github.com/amamov/teaching-nestjs-a-to-z/blob/main/images/1.jpeg?raw=true)

[TOC]

# 시작하기

## 1. multer 설치

> mutler: multipart/form-data로 안전하게 보낼 수 있도록 해주는 패키지

```bash
$ npm i -D @types/multer
```

## 2. Interceptor를 사용하여 단일 파일 업로드 기본 형태 만들기

### cats.controller.ts

```typescript
  @ApiOperation({ summary: '고양이 이미지 업로드' })
  @UseInterceptors(FileInterceptor('image'))
  @Post('upload/cats')
  uploadCatImg(@UploadedFiles() files: Array<Express.Multer.File>) {
    console.log(files);
    return 'uploadImg';
  }
}
```

## 3. cats.module.ts에 import하기

```typescript
import { MulterModule } from '@nestjs/platform-express';

@Module({
  imports: [
    MulterModule.register({
      dest: './uploads',
    }),
    MongooseModule.forFeature([{ name: Cat.name, schema: CatSchema }]),
    forwardRef(() => AuthModule),
  ],
  controllers: [CatsController],
  providers: [CatsService, CatsRepository],
  exports: [CatsService, CatsRepository],
})
export class CatsModule {}
```

