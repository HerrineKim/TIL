import { ApiProperty } from '@nestjs/swagger';

export class ReadOnlyCatDto {
  @ApiProperty({
    example: '12',
    description: 'id',
    required: true,
  })
  id: string;

  @ApiProperty({
    example: 'hyerin@naver.com',
    description: 'email',
    required: true,
  })
  email: string;

  @ApiProperty({
    example: 'hyerin',
    description: 'name',
    required: true,
  })
  name: string;
}
