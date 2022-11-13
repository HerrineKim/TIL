# 04 Process 1

## 04-1 프로세스의 개념

#### "Process is a program in execution"

프로세스(Process)는 쉽게 말해 '실행 중인 프로그램'이다. 더 정확히 말하면, 디스크에 있는 프로그램이 메모리에 로드되면 프로세스가 된다. 하나의 프로그램이 여러 프로세스가 될 수 있다.

#### 프로세스의 문맥(context)

- CPU 수행 상태를 나타내는 하드웨어 문맥
  - Program Counter
  - 각종 register
- 프로세스의 주소 공간
  - code, data, stack
- 프로세스 관련 커널 자료 구조
  - PCB(Process Control Block)
  - Kernel stack



## 04-2 프로세스의 상태

#### 프로세스는 상태(state)가 변경되며 수행된다

- Running

  - CPU를 잡고 instruction을 수행중인 상태

- Ready

  - CPU를 기다리는 상태(메모리 등 다른 조건을 모두 만족하고)

- Blocked(wait, sleep)

  - CPU를 기다리는 상태(메모리 등 다른 조건을 모두 만족하고)

  - Process 자신이 요청한 event(예: I/O)가 즉시 만족되지 않아 이를 기다리는 상태

    (예) 디스크에서 file을 읽어와야 하는 경우



- New: 프로세스가 생성중인 상태
- Terminated: 수행(execution)이 끝난 상태



## 04-3 프로세스 상태도

![image-20220625181512635](04%20Process%201.assets/image-20220625181512635.png)



## 04-4 프로세스 상태

![image-20220625203533351](04%20Process%201.assets/image-20220625203533351.png)



## 04-5 Process Control Block(PCB)

![image-20220625204414816](04%20Process%201.assets/image-20220625204414816.png)



## 04-5 문맥교환(Context Switch)

![image-20220625205807751](04%20Process%201.assets/image-20220625205807751.png)

![image-20220625211229042](04%20Process%201.assets/image-20220625211229042.png)



## 04-6 프로세스를 스케줄링하기 위한 큐

![image-20220625211626972](04%20Process%201.assets/image-20220625211626972.png)



## 04-7 Ready Queue와 다양한 Device Queue

![image-20220625212026079](04%20Process%201.assets/image-20220625212026079.png)



## 04-8 프로세스 스케줄링 큐의 모습

![image-20220625212052894](04%20Process%201.assets/image-20220625212052894.png)



## 04-9 스케줄러(Scheduler)

![image-20220625212119368](04%20Process%201.assets/image-20220625212119368.png)



- degree of Multiprogramming: 메모리에 몇 개의 프로그램을 올려 놓을 지를 결정
- 우리는 time sharing system을 사용하기 때문에 Medium Term Scheduler를 사용한다. 일단 모든 프로그램을 메모리에 올려 놓고, 너무 많이 올라가 있으면 수를 조절하는 것이다. 



## 04-10 프로세스의 상태

![image-20220625212727093](04%20Process%201.assets/image-20220625212727093.png)

- Suspended: Medium Term scheduler로 인해 쫓겨난 상태를 표현하기 위해 추가됨



## 04-11 프로세스 상태도

![image-20220625220622828](04%20Process%201.assets/image-20220625220622828.png)

- New : 프로세스가 만들어진 상태이다. 프로세스가 생성되면 바로 Ready 단계로 가면 되는거 아닌가? 라고 생각할 수 있다. 하지만 프로세스가 만들어지면 메모리도 할당해야하고 프로세스의 정보를 담고 있는 PCB와 프로세스가 실행되면서 사용할 스택 메모리도 할당하고 초기화해줘야 한다. 그렇기 때문에 프로세스 생성에는 시간이 걸리고 New 상태에 어느 정도 머물러야 한다.
- Ready : 실행을 하기 위해 기다리는 상태이다. 언제든지 실행할 준비가 되어있고, CPU를 할당해주면 바로 실행할 수 있는 단계이다.
- Running : 프로세스가 CPU를 차지하고 실행하고 있는 상태이다.
- Blocked : CPU를 할당해주어도 실행할 수 없는 상태이다.(I/O request, 다른 프로세스가 끝날 때까지 대기 등등)
- Exit : 프로세스가 끝나게 되면 프로세스가 할당 받았던 자원들을 반납해야한다. 따라서 Exit 상태에서도 처리 시간이 걸린다.