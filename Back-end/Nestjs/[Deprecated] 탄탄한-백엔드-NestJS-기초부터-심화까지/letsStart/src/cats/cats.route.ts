import {Router} from 'express'
import {
  readAllCat,
  readCat,
  createCat,
  updateCat,
  deleteCat,
} from './cats.service'

// 이 router 인스턴스에 라우팅을 쭉 추가해나가는 것
const router = Router();

// * READ 고양이 전체 데이터 다 조회 -> GET
router.get('/cats', readAllCat)

// * READ 특정 고양이 데이터 조회 -> GET
router.get('/cats/:id', readCat)

// * CREATE 새로운 고양이 추가 -> PUT
router.post('/cats', createCat)

// * UPDATE 고양이 데이터 업데이트 -> PUT
router.put('/cats/:id', updateCat)

// * UPDATE 고양이 데이터 부분적으로 업데이트 -> PATCH
router.patch('/cats/:id', updateCat)

// * DELETE 고양이 데이터 삭제 -> DELETE
router.delete('/cats/:id', deleteCat)

export default router;