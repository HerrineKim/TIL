# 마크다운 문법



## 제목 (heading)

제목은 # 기호를 통해서 작성 가능하다. 제목은 h1 ~ h6까지 표현 가능하다.

### 제목 3

#### 제목4

##### 제목5 

###### 제목6



## 목록

### 순서가 없는 목록 (unorderd list)

`*` , `-` , `+`  를 통해서 목록을 구성한다. 목록 레벨 전환은 `tab` 혹은 `shift + tab` 으로 한다.

- 딸기
- 바나나
- 사과
  - (tab) 아오리 사과
  - 세척 사과



### 순서가 있는 목록 (orderd list)

`1.` 으로 목록을 구성한다.

1. 세수
2. 아침
3. 출근



## 코드 블록

` ```python `

```python
print('Hello, world')
for i in range(5):
    print(i)
# 주석
```

```html
<h1>
    제목
</h1>
<!-- 주석 -->
```



## 링크 

```
[구글 링크](https://google.com)
```

[구글 링크](https://google.com)



## 인용문 (quote)

`>`

> Life is short, you need python!

```markdown
다중 인용문

> This is a first blockqute.
>	> This is a second blockqute.
>	>	> This is a third blockqute.
```

> This is a first blockqute.
>
> > This is a second blockqute.
> >
> > > This is a third blockqute.



## 표

`ctrl+T`

| 강아지 | 나이 | 비고 |
| ------ | ---- | ---- |
| 포터   |      |      |
| 봄달래 |      |      |
| 삐롱   |      |      |
| 밍키   |      |      |



## 이미지

`설정에서 상대경로로 지정하여 .assets 파일과 함께 업로드한다`

![1](C:\Users\takhe\Desktop\1.png)

![1](markdown.assets/1.png)

사이즈 조절 방법: `<img width="" height=""></img>`

```
<img src="C:\Users\takhe\Desktop\1.png" width="450px" height="300px" title="px(픽셀) 크기 설정" alt="RubberDuck"></img><br/>
```



## 기타

`*`

*기울임(이탤릭체)*

`**`

**굵게(볼드체)**

`**_`

**_ 이탤릭체와 볼드체를 함께_**

`~~`

~~취소선~~

`-----` , `***`

수평선

---









