import {Request, Response} from 'express'
import {Cat, CatType} from './cats.model'

// * READ 고양이 전체 데이터 다 조회 -> GET
export const readAllCat = (req: Request, res: Response) => {
  try {
    const cats = Cat;
    // throw new Error('db connect error');
    res.status(200).send({
      success: true,
      data: {
        cats,
      },
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}

// * READ 특정 고양이 데이터 조회 -> GET
export const readCat = (req: Request, res: Response) => {
  try {
    const params = req.params
    const cats = Cat.find((cat) => {
      return cat.id === params.id
    });
    // throw new Error('db connect error');
    res.status(200).send({
      success: true,
      data: {
        cats,
      },
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}

// * CREATE 새로운 고양이 추가 -> PUT
export const createCat = (req: Request, res: Response) => {
  try {
    const data = req.body
    Cat.push(data)
    res.status(200).send({
      success: true,
      data: {data},
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}

// * UPDATE 고양이 데이터 업데이트 -> PUT
export const updateCat = (req: Request, res: Response) => {
  try {
    const params = req.params
    const body = req.body
    let result
    // forEach(): 배열의 각 요소에 대해 한 번씩 제공된 함수를 실행
    Cat.forEach((cat) => {
      if (cat.id === params.id) {
        // 한 번에 바꿔줌
        cat = body
        // 바뀐 결과를 반환해 줄 result에 넣어줌
        result = cat
      }
    })
    res.status(200).send({
      success: true,
      data: {
        cat: result,
      },
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}

// * UPDATE 고양이 데이터 부분적으로 업데이트 -> PATCH
export const updatePartialCat = (req: Request, res: Response) => {
  try {
    const params = req.params
    const body = req.body
    let result
    // forEach(): 배열의 각 요소에 대해 한 번씩 제공된 함수를 실행
    Cat.forEach((cat) => {
      if (cat.id === params.id) {
        // 구조분해할당
        cat = {...cat, ...body}
        // 바뀐 결과를 반환해 줄 result에 넣어줌
        result = cat;
      }
    })
    res.status(200).send({
      success: true,
      data: {
        cat: result,
      },
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}

// * DELETE 고양이 데이터 삭제 -> DELETE
export const deleteCat = (req: Request, res: Response) => {
  try {
    const params = req.params
    // 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환
    const newCat = Cat.filter((cat) => {
      return cat.id !== params.id
    })
    res.status(200).send({
      success: true,
      data: newCat
    });
  } catch (error: any) {
    res.status(400).send({
      success: false,
      error: error.message,
    })
  }
}
