# Creating React Native project

https://reactnative.dev/

*Android 기기 사용

## Expo CLI or React Native CLI

![image-20220904232216117](01_Creating%20React%20Native%20project.assets/image-20220904232216117.png)

### Expo CLI를 추천

- 이유: 더 쉽다!
- 원한다면 React Native CLI로 전환할 수 있다.

### React Native CLI

- 세팅을 직접해야 하는 부분이 더 많아서 초심자에게 어려울 수 있다.
- Native 소스 코드(SWIFT, Kotlin 등)과 통합하기 좀 더 쉽다.



## Expo CLI로 프로젝트 시작하기(실습 폴더)

https://docs.expo.dev/



1. node.js LTS 버전 설치

2. `npm install -g expo-cli`

3. 프로젝트 생성

   ```bash
   expo init RNCourse
   
   # 'blank' 선택
   
   cd RNCourse
   npm start # you can also use: expo starts
   ```

4. ESLint, Prettier 설정

   


### 프로젝트 기본 구조

![image-20220910001211551](01_Creating%20React%20Native%20project.assets/image-20220910001211551.png)

#### 

#### `babel.config.js`

수정할 필요 X



#### `app.json`

나중에 중요해지는 파일로, 우리의 앱에 대한 구성을 여기서 변경할 수 있다. expo가 앱을 빌드할 때 여기서 정보를 읽어 간다.



#### `App.js`

시작 단계에서의 유일한 실제 코드 파일이다. jsx 컴포넌트들과 스타일이 있다.



## Running

1. 우리는 이걸 실제로 볼 만한 기계가 필요한데, 앱스토어/플레이스토어에서 'Expo'를 검색하고, `Expo go` 앱을 다운로드한다.
2. 터미널에서 `npm run start`를 입력한다.
3. 터미널 상에 표시된 QR코드를 앱으로 스캔한다.
4. Expo Go 앱 상에 내가 만든 앱이 표시되고, 수정 후 저장할 때마다 자동으로 반영된다.



### Android Studio 

만약 별개의 기기에서 실행해보고 싶거나, iPhone만 가지고 있다면 Android Studio의 emulator를 사용하면 된다.

1. emulator 중 play store 아이콘이 있는 것으로 생성한다(expo go 설치 위해)
2. ![image-20220910005028864](01_Creating%20React%20Native%20project.assets/image-20220910005028864.png)
3. emulator를 실행한다.
4. `npm start`를 누르고 `a`키를 누르면 자동으로 emulator를 찾아 앱을 실행해준다.



