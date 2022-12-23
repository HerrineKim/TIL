# 고양이 데이터 Update Delete API 개발

# UPDATE(PUT)

> 아직 DB가 없기 때문에 실제로 반영은 되지 않는다.

```typescript
// * UPDATE 고양이 데이터 업데이트 -> PUT
router.put('/cats/:id', (req, res) => {
  try {
    const params = req.params;
    const body = req.body;
    let result;
    // forEach(): 배열의 각 요소에 대해 한 번씩 제공된 함수를 실행
    Cat.forEach((cat) => {
      if (cat.id === params.id) {
        // 한 번에 바꿔줌
        cat = body;
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
})
```



# UPDATE(PATCH: 부분적으로 업데이트)

```typescript
router.patch('/cats/:id', (req, res) => {
  try {
    const params = req.params;
    const body = req.body;
    let result;
    // forEach(): 배열의 각 요소에 대해 한 번씩 제공된 함수를 실행
    Cat.forEach((cat) => {
      if (cat.id === params.id) {
        // 구조분해할당
        cat = {...cat, ...body};
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
})
```

## 

# DELETE

```typescript
// * DELETE 고양이 데이터 삭제 -> DELETE
router.delete('/cats/:id', (req, res) => {
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
})
```

