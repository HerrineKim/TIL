import { Cat } from '../cats.schema';
import { ApiProperty } from '@nestjs/swagger';

export class ReadOnlyCatDto {
  @ApiProperty({
    example: 'hyerin@naver.com',
    description: 'email',
    required: true,
  })
  @IsEmail()
  @IsNotEmpty()
  email: string;

  @ApiProperty({
    example: 'hyerin@naver.com',
    description: 'email',
    required: true,
  })
  @IsString()
  @IsNotEmpty()
  password: string;

  @ApiProperty({
    example: 'hyerin@naver.com',
    description: 'email',
    required: true,
  })
  @IsString()
  @IsNotEmpty()
  name: string;
}
