# 원격 저장소 활용(GitHub)

## 기초 활용

### 조회

```bash
$ git remote -v
origin  https://github.com/edutak/first1.git (fetch)
origin  https://github.com/edutak/first1.git (push)
```

- fetch vs pull?
  - fetch: 받아오기만 한다
  - pull: fetch + merge (병합)

### 추가 

```bash
$ git remote add <원격저장소이름> <url>
$ git remote add origin https://github.com/username/repository.git
```

* `origin` : 일반적으로 많이 활용되는 원격저장소 이름

### 삭제

```bash
$ git remote rm <원격저장소이름>
$ git remote rm origin
```



## 원격 저장소 push

> Update remote refs along with associated objects (commit)

```bash
$ git push <원격저장소이름> <브랜치이름>
$ git push origin master
```



## pull

> Fetch from and integrate with another repository or a local branch

```bash
$ git pull <원격저장소이름> <브랜치이름>
$ git pull origin master

# 예시
김혜린@DESKTOP-HYERIN MINGW64 ~/OneDrive - 한양대학교/바탕 화면/first1 (master)
$ git pull origin master
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 2 (delta 1), reused 2 (delta 1), pack-reused 0
Unpacking objects: 100% (2/2), 223 bytes | 37.00 KiB/s, done.
From https://github.com/edutak/first1
 * branch            master     -> FETCH_HEAD
   ee084e8..d58b853  master     -> origin/master
Updating ee084e8..d58b853
Fast-forward
 README.md | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
```

- pull로 변경사항을 가져오면 된다.



## 원격 저장소 clone

> Clone a repository into a new directory

```bash
$ git clone <원격저장소주소>
$ git clone https://github.com/username/repository.git
```

* 원격저장소 이름의 폴더가 생성됨

  

## Clone 예시

```bash
김혜린@DESKTOP-HYERIN MINGW64 ~/OneDrive - 한양대학교/바탕 화면
$ git clone https://github.com/edutak/first1.git
Cloning into 'first1'...
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 1), reused 6 (delta 0), pack-reused 0
Receiving objects: 100% (7/7), done.
Resolving deltas: 100% (1/1), done.

김혜린@DESKTOP-HYERIN MINGW64 ~/OneDrive - 한양대학교/바탕 화면
$ cd first1

김혜린@DESKTOP-HYERIN MINGW64 ~/OneDrive - 한양대학교/바탕 화면/first1 (master)
$ git log
commit ee084e8680b2cd7147827287ce86ea757615f397 (HEAD -> master, origin/master, origin/HEAD)
Author: edutak <edutak.ssafy@gmail.com>
Date:   Thu Jan 13 13:17:42 2022 +0900

    Add c

commit 8cf13c60cbd2e35cf5737f2d183212702a75539b
Author: edutak <edutak.ssafy@gmail.com>
Date:   Wed Jan 12 16:54:48 2022 +0900

    Add b.txt

commit c61c049aab383ec9b8f93bc8deedce19331ea2b4
Author: edutak <edutak.ssafy@gmail.com>
Date:   Wed Jan 12 16:38:47 2022 +0900

    First commit

```

- 이제 내가 일부/전부를 커밋할 수 있게 되었고, 분산버전관리시스템을 이해하게 된 것이다.
- 버전!!을 관리할 수 있게 된 것이다.
- 여기서 고쳐서 push해도 올라가지는 않는다. 저장소에 초대된 적이 없기 때문이다.
- init 아니면 clone 하라



- 해시값 관련 영상
  - How secure is 256 bit security? (유튜브)

![image-20220113160415189](git_%EC%9B%90%EA%B2%A9%EC%A0%80%EC%9E%A5%EC%86%8C%ED%99%9C%EC%9A%A9.assets/image-20220113160415189.png)

![image-20220113160508823](git_%EC%9B%90%EA%B2%A9%EC%A0%80%EC%9E%A5%EC%86%8C%ED%99%9C%EC%9A%A9.assets/image-20220113160508823.png)



[좋은 git 커밋 메시지를 작성하기 위한 7가지 약속](https://meetup.toast.com/posts/106)

[좋은 git commit 메시지를 위한 영어 사전](https://blog.ull.im/engineering/2019/03/10/logs-on-git.html)
