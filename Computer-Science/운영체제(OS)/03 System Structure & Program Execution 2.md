# System Structure & Program Execution 2

![image-20220624161343819](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624161343819.png)

![image-20220624161817312](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624161817312.png)



CPU는 빠른 일꾼이다. 메모리의 instruction을 읽어서 실행한다. 컴퓨터가 켜져 있는 동안.

다음 instruction을 하기 전에 interrupt가 있는지 확인한다. 있다면 지금 하던 작업을 잠시 멈추고 CPU 제제권이 OS에게 넘어간다. interrupt 별로 실행해야 할 일들은 커널 함수로 저장되어 있다. (interrupt vector와 처리 루틴 )

![image-20220624194745314](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624194745314.png)



![image-20220624195006273](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624195006273.png)

![image-20220624195315944](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624195315944.png)

![image-20220624200225238](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624200225238.png)

![image-20220624201932864](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624201932864.png)

![image-20220624202137829](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624202137829.png)

![image-20220624202614936](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624202614936.png)

- code: 실행 코드
- data: 자료구조
- stack: 함수 호출할 때 데이터 쌓고 가져가는 곳

-> 이러한 주소공간들을 메모리에 올려서 사용함. 쓰지 않는 것은 디스크의 Swap area에 놓음. 프로그램이 종료되면 사라짐. 메모리 낭비를 막기 위해.



![image-20220624203411159](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624203411159.png)

- 운영체제가 하는 일: 자원을 효율적으로 관리



![image-20220624203839373](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624203839373.png)

![image-20220624203940504](03%20System%20Structure%20&%20Program%20Execution%202.assets/image-20220624203940504.png)