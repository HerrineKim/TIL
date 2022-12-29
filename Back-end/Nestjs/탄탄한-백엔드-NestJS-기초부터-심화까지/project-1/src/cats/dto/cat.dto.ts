import { ApiProperty, PickType } from '@nestjs/swagger';
import { Cat } from '../cats.schema';

export class ReadOnlyCatDto extends PickType(Cat, ['email', 'name'] as const) {
  @ApiProperty({
    example: '12',
    description: 'id',
    required: true,
  })
  id: string;
  // @ApiProperty({
  //   example: 'hyerin@naver.com',
  //   description: 'email',
  //   required: true,
  // })
  // email: string;

  // @ApiProperty({
  //   example: 'hyerin',
  //   description: 'name',
  //   required: true,
  // })
  // name: string;
}
