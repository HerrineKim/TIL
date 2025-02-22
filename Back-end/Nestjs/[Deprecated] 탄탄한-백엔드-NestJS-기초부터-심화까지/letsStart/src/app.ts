import * as express from 'express'
import catsRouter from './cats/cats.route'

class Server {
  public app: express.Application

  constructor() {
    const app: express.Application = express()
    this.app = app
  }
  // 라우터 부분
  private setRoute(): void {
    this.app.use(catsRouter)
  }
  // 미들웨어 부분
  private setMiddleware(): void {
    // * logging middleware
    this.app.use((req, res, next) => {
      console.log(req.rawHeaders[1])
      console.log("this is logging middleware")
      next()
    })
    // * JSON parsing middleware
    this.app.use(express.json())
    // * routing middleware
    this.setRoute()
    // * 404 error middleware
    this.app.use((req, res, next) => {
      console.log('this is logging middleware')
      res.send({error: "404 not found error"})
      next()
    })
  }

  public listen() {
    this.setMiddleware()
    this.app.listen(8000, () => {
      console.log('server is on...')
    })
  }
}

function init() {
  const server = new Server()
  server.listen()
}

init()