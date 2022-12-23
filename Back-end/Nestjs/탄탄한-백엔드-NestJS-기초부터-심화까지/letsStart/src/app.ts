import * as express from 'express'
import catsRouter from './cats/cats.route'

// app: 서버 역할, express의 인스턴스
const app: express.Express = express()
const port: number = 8000

// * logging middleware
app.use((req, res, next) => {
  console.log(req.rawHeaders[1])
  console.log("this is logging middleware")
  next()
})

// * JSON parsing middleware
app.use(express.json())

// * routing middleware
app.use(catsRouter)

// * 404 error middleware
app.use((req, res, next) => {
  console.log('this is logging middleware')
  res.send({error: "404 not found error"})
  next()
})

// listen(): 서버를 실행하는 메서드
// app.listen(port, () => console.log(`Example app listening on port http://localhost:${port}`))
app.listen(8000, () => {
  console.log('server is on...')
})