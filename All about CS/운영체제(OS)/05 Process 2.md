# 05 Process 2

## 05-1 동기식 입출력과 비동기식 입출력

![image-20220628142941198](05%20Process%202.assets/image-20220628142941198.png)



### 비동기식 입출력(Asynchronous I/O)

입출력이 끝나는 것을 기다리지 않고 실행한다.

- I/O가 시작된 후 입출력 작업이 끝나기를 기다리지 않고 제어가 사용자 프로그램에 즉시 넘어감



### 동기식 입출력(Synchronous I/O)

진행되는 입출력이 있다면 끝날 때까지 기다렸다가 실행한다.

- I/O 요청 후 입출력 작업이 완료된 후에야 제어가 사용자 프로그램에 넘어감
- 구현 방법 1
  - I/O가 끝날 때까지 CPU를 낭비시킴
  - 매시점 하나의 I/O만 일어날 수 있음
- 구현 방법 2
  - I/O가 완료될 때까지 해당 프로그램에게서 CPU를 빼앗음
  - I/O 처리를 기다리는 줄에 그 프로그램을 줄 세움
  - 다른 프로그램에게 CPU를 줌



:star:두 경우 모두 I/O의 완료는 인터럽트로 알려줌



## 05-2 프로세스 스케줄링 큐의 모습

![image-20220628212711733](05%20Process%202.assets/image-20220628212711733.png)



## 05-3 Thread

: 프로세스 내부에 CPU 수행 단위가 여러 개 있는 경우, 그것들을 Thread라고 부른다.

![image-20220628213428675](05%20Process%202.assets/image-20220628213428675.png)



- PCB: 프로세스의 상태를 관리하기 위해 하나씩 주어지는 것. 현재 메모리의 어느 부분을 실행하고 있는지를 program counter가 가리키고 있는데, 각 Thread마다 코드의 어느 부분을 실행하고 있는지가 보여지고, 코드를 실행하다 호출하는 함수들은 stack에 있다.
- Thread들은 공유할 것들은 공유하고, 레지스터 등 분리해서 실행할 것들은 분리한다.



#### Thread

- "A thread (or lightweight process) is a basic unit of CPU utilization"
- Thread의 구성
  - program counter
  - register set
  - stack space



- Thread가 동료 thread와 공유하는 부분(=task)
  - code section
  - data section
  - OS resources



- 전통적인 개념의 heavyweight process는 하나의 thread를 가지고 있는 task로 볼 수 있다.



##### Thread의 장점

- 다중 스레드로 구성된 태스크 구조에서는 하나의 서버 스레드가 blocked(waiting) 상태인 동안에도 동일한 태스크 내의 다른 스레드가 실행(running)되어 빠른 처리를 할 수 있다.
- 동일한 일을 수행하는 다중 스레드가 협력하여 높은 처리율(throughput)과 성능 향상을 얻을 수 있다.
- 스레드를 사용하면 병렬성을 높일 수 있다.