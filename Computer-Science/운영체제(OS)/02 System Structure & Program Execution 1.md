# 02 System Structure & Program Execution 1

## 1. 컴퓨터 시스템 구조

![image-20220621140240754](02%20System%20Structure%20&%20Program%20Execution%201.assets/image-20220621140240754.png)

- Disk: 저장 장치이기도 하지만, output device이기도 하다.



![image-20220621140509819](02%20System%20Structure%20&%20Program%20Execution%201.assets/image-20220621140509819.png)

- register: 메모리보다 더 빠르면서 정보를 저장할 수 있는 공간
- mode bit: CPU에서 실행되는 것이 OS인지 사용자의 프로그램인지 구분
- Interrupt line: CPU는 항상 Memory의 instruction을 순서대로 실행하는 것인데, 키보드에서 입력이 들어왔다든지, Disk에서 정보가 왔다든지 이러한 외부 정보를 이것이 알려준다. 
- timer: 특정 프로그램이 CPU를 독점(무한 루프 등)하는 것을 막는다. 처음에는 OS가 CPU를 가지고 있다가 다른 프로그램이 실행되면 timer에게 시간을 세팅하고 프로그램에게 CPU를 그 시간만큼 넘겨준다.(1초보다도 훨씬 작은 시간이다.)
- local buffer: CPU는 원칙적으로 Memory에만 접근하는데, I/O device들의 작업은 local buffer에서 데이터를 받아서 한다. buffer에 쌓이게 되면 CPU가 그 내용을 읽어서 자신의 Memory에 쌓을 수 있다. 그러다보니 CPU가 너무 interrupt를 많이 당하기도 한다.그래서 DMA controller를 둔다.
- DMA controller: 직접 Memory에 접근할 수 있는 controller. CPU에 직접 interrupt가 걸려서 CPU가 직접 작업을 읽어와 자신의 Memory에 할당하는 것은 overhead가 크기 때문에, CPU는 자신의 일을 하고 DMA controller가 local buffer에서 Memory로 복사해주는 일을 한다. 그 작업이 모두 끝나면 CPU에게 interrupt를 한 번만 걸어 보고를 해주어 CPU를 효율적으로 쓸 수 있게 해준다. 만약 CPU와 controller 둘 다 Memory에 접근하려고 할 때 충돌이 일어날 수 있는데, 이런 상황은 memory controller가 관리한다. 



### Mode bit

- 사용자 프로그램의 잘못된 수행으로 다른 프로그램 및 운영체제에 피해가 가지 않도록 하기 위한 보호 장치 필요

- Mode bit을 통해 하드웨어적으로 두 가지 모드의 operation 지원

  `1` 사용자 모드: 사용자 프로그램 수행

  `0` 모니터 모드*: OS 코드 수행

  - 보안을 해칠 수 있는 중요한 명령어는 모니터 모드에서만 수행 가능한 '특권명령'으로 규정

  - Interrupt나 Exception 발생시 하드웨어가 mode bit을 0으로 바꿈

  - 사용자 프로그램에게 CPU를 넘기기 전에 mode bit을 1로 셋팅

    *`모니터 모드` = 커널 모드, 시스템 모드

![image-20220621153159962](02%20System%20Structure%20&%20Program%20Execution%201.assets/image-20220621153159962.png)



### Device Controller

- I/O device controller

  - 해당 I/O 장치 유형을 관리하는 일종의 작은 CPU
  - 제어 정보를 위해 control register, status register를 가짐
  - local buffer를 가짐(일종의 data register)

- I/O는 실제 device와 local buffer 사이에서 일어남

- Device controller는 I/O가 끝났을 경우 interrupt로 CPU에 그 사실을 알림

  *device driver(장치구동기): OS 코드 중 각 장치별 처리루틴 -> software

  *device controller(장치제어기): 각 장치를 통제하는 일종의 작은 CPU -> hardware



### 입출력(I/O)의 수행

- 모든 입출력 명령은 특권 명령
- 사용자 프로그램은 어떻게 I/O를 하는가?
  - 시스템콜(system call)
    - 사용자 프로그램은 운영체제에게 I/O 요청
  - trap을 사용하여 인터럽트 벡터의 특정 위치로 이동
  - 제어권이 인터럽트 벡터가 가리키는 인터럽트 서비스 루틴으로 이동
  - 올바른 I/O 요청인지 확인 후 I/O 수행
  - I/O 완료 시 제어권을 시스템콜 다음 명령으로 옮김



### 인터럽트(Interrupt)

> 현대의 운영체제는 인터럽트에 의해 구동됨

- 인터럽트
  - 인터럽트 당한 시점의 레지스터와 program counter를 save 한 후 CPU의 제어를 인터럽트 처리 루틴에 넘긴다
- Interrupt(넓은 의미)
  - Interrupt(하드웨어 인터럽트): 하드웨어가 발생시킨 인터럽트
  - Trap(소프트웨어 인터럽트)
    - Exception: 프로그램이 오류를 범한 경우
    - System call: 프로그램이 커널 함수를 호출하는 경우. 사용자 프로그램이 운영체제의 서비스를 받기 위해 커널 함수를 호출하는 것.
- 인터럽트 관련 용어
  - 인터럽트 벡터
    - 인터럽트 발생 시 실행해야 하는 함수들의 일종의 테이블. 해당 인터럽트의 처리 루틴 주소를 가지고 있음
  - 인터럽트 처리 루틴(=Interrupt Service Routine, 인터럽트 핸들러)
    - 해당 인터럽트를 처리하는 커널 함수