# Django 1:N, M:N 관계

> https://devjaewoo.tistory.com/39

### **1. 1:1 관계**

models 클래스의 OneToOneField를 사용하여 1:1 관계를 표현할 수 있다.

 

**models.py**

```python
from django.db import models


class Engine(models.Model):
    name = models.CharField(max_length=30)


class Car(models.Model):
    name = models.CharField(max_length=30)
    engine = models.OneToOneField(Engine, on_delete=models.CASCADE)
```

 

OneToOneField(Engine)과 ForeignKey(Engine, unique=True)는 구조적으로는 같지만, OneToOneField는 조회 시 객체 하나를 반환하지만, ForeignKey는 객체 Set을 반환한다는 차이가 있다.

------

### **2. 1:N 관계**

models 클래스의 ForeignKey를 사용하여 1:N 관계를 표현할 수 있다.

 

**models.py**

```python
from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=30)


class Car(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
```

Owner 1명이 N개의 차를 소유할 수 있다. 이런 경우 N개에 해당하는 모델에 1개에 해당하는 모델을 Foreign Key로 지정해주면 1:N 관계를 정의할 수 있다.

------

### **3. M:N 관계**

M:N 관계는 관계를 가지는 2개의 모델 외에 둘 사이를 중재해주는 모델이 추가로 필요하다.

**직관적인 형태**

```python
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=70)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20)


class Author(models.Model):
    name = models.CharField(max_length=30)


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

 

작성된 코드를 보면 BookAuthor 클래스에 Foreign Key를 2개 생성했다.

그 결과 Book과 BookAuthor가 1:N 관계를 맺게 되고, Author와 BookAuthor가 1:N 관계를 맺게 된다. 이렇게 둘 사이에 중개 클래스를 생성함으로써 M:N 관계를 정의할 수 있다.



**중개 모델 사용: ManyToManyField 설정**

```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor,
                                    through='Reservation')
    
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```





**중개 모델 사용 및 역참조 사용해야 할 때: related_name 설정**

```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor,
                                    through='Reservation',
                                    related_name='patients')
    
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```



**중개 모델 없이 id값만 필요한 경우**

```python
class Doctor(models.Model):
    name = models.CharField(max_length=10)

class Patient(models.Model):
    name = models.CharField(max_length=10)
    doctors = models.ManyToManyField(doctor,
                                    related_name='patients')
```

