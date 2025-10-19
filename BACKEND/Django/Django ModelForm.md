# Django ModelForm

## 1. Form 과 ModelForm

### Form

HTML의 `Form`안에서 사용자의 데이터를 처리하는 `input`을 다루는 것은 매우 복잡하다. Django의 `Form`은 이런 작업의 많은 부분을 간소화하고 자동화 한다. 또한 프로그래머가 작업하는 것보다 보안성이 높다. Django의 `Form`은 다음 세 가지의 작업을 처리한다.

> - 랜더링을 위한 데이터를 준비하고 재구성한다.
> - 데이터를 위한 HTML Form 생성한다.
> - 클라이언트가 `submit`한 데이터를 받아 처리한다.

또한 Form의 가장 큰 역할 중 하나는 **유효성 검사**를 해서 올바른 데이터를 처리할 수있도록 한는 것이다.



### ModelForm

Form과 역할은 비슷하지만, 약간의 차이가 있다. Django form을 정의할 때 Model에 있는 field를 다시 재정의해야 한다. 이러한 반복 작업을 줄일 수 있게 해주는 것이 ModelForm이다.



### Form? ModelForm?

Form은 field와 widget을 재정의해야 하는데 ModelForm은 Model을 기반으로 자동으로 처리한다. 하지만 이런 점이 ModelForm이 Form보다 더 나은 점이라고는 단정 지을 수 없다.

필요에 의해서 다른 방법을 사용할 뿐 어떤 것이 더 우위에 있다고 말할 수는 없다



## 2. Form으로 Create 구현

```python
#forms.py
from django import forms

class RecordForm(forms.Form):
    date = forms.CharField(max_length=8)
    push_up = forms.CharField(max_length=20)
    pull_up = forms.CharField(max_length=20)
```

Model을 정의하는 것과 매우 유사한 방법으로 field를 정의한다. 단, 사용자가 직접 입력하는 데이터를 저장할 field만 정의하고 Django에서 자동으로 만드는 데이터는 정의하지 않는다.

```python
views.py
def new(request):
    form = RecordForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'records/new.html', context)
<form action="{% url 'records:create' %}" method="POST">
{% csrf_token %}
  {{ form.as_p }}
  <button>저장</button>
  <hr>
</form>
<a href="{% url 'records:index' %}">처음으로</a>
```

`{{ form.as_p }}`은 From rendering options라고 하는데 다음과 같은 종류가 있다.

- as_p()
  각 field를 `p`태그로 랜더링
- as_ul()
  각 field를 `li`태그로 랜더링. `ul`은 직접 작성
- as_table()
  각 field를 `tr`태그로 랜더링. `table`은 직접 작성
  ![img](https://velog.velcdn.com/images%2Fmain_string%2Fpost%2F7b688a93-5f22-42c8-9f66-27ae3e9115e1%2Fimage.png)

위와 같이 Form에서 자동으로 랜더링 해주는 것을 확인할 수 있다. 날짜를 입력하고 제출하면 정상적으로 데이터베이스에 반영된다.



### Widget

Django의 HTML input 요소를 표현하는 것으로 HTML 랜더링을 처리한다. Form의 field는 input의 유효성을 처리하는 것이고, Widget은 단순한 랜더링 처리한다는 점을 혼동해서는 안된다.

```python
#forms.py
class RecordForm(forms.Form):
    date = forms.CharField(max_length=8)
    push_up = forms.CharField(max_length=20)
    pull_up = forms.CharField(widget=forms.Textarea)
```

widget을 통해서 `CharField`를 `Textarea`타입으로 랜더링했다.
![img](https://velog.velcdn.com/images%2Fmain_string%2Fpost%2F555976c8-7e70-4f96-87cf-72e17b86a2b4%2Fimage.png)

## ModelForm으로 함수 구조 변경

현재 프로젝트는 `Create`와 `Update`가 두 개의 함수로 나뉘어 있고 `Create`만 Form을 이용하고 있는데, ModelForm으로 불필요한 함수를 줄이고, 유효성 검사를 추가해서 좀 더 깔끔한 코드를 만들 것이다.

```python
#forms.py
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
```

Model의 정보를 기반으로 만들어지기 때문에 model을 import해야 한다. 위 코드를 보면 알 수 있듯이 field를 재정의할 필요없이 Form을 정의하고 그 기능을 사용할 수 있다.

```python
def create(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save()
            return redirect('records:detail', record.pk)
    else:
        form = RecordForm()
    context = {
        'form': form,
    }
    return render(request, 'records/create.html', context)
```

POST요청이 왔을 때, `form`에 POST에 있는 정보를 저장한 `RecordForm` 인스턴스를 저장한다. 해당 인스턴스에 대해서 유효성 검사를 통과하면 데이터베이스에 저장한 뒤, `detail`함수로 `redirect`를 보낸다.

> **유효성 검사**
> Django는 데이터가 유효한지 여부를 True/False 형태로 반환해주는 is_valid()를 제공한다. -> 올바른 데이터가 전송될 수있도록 한다.

POST 외의 요청이 오면 빈 인스턴스를 만들어서 `create.html`를 랜더링 한다. 메인 페이지(`index.html`)에서 `생성`버튼을 누르면 GET 요청이 `create`로 전해지는데, 이 경우가 해당한다. 그 외에 다양한 요청도 마찬가지로 처리한다.

`context`이하 코드를 `else`구문에 포함시키지 않은 이유는 **POST요청이지만 유효성 검사를 통과하지 못한 경우**를 처리하기 위함이다.

### Django Form의 workflow

![img](https://velog.velcdn.com/images%2Fmain_string%2Fpost%2Fe746c80d-6998-4e7d-bac1-40882b110a51%2Fimage.png)위에서 작성한 코드와 사진의 Flowchart를 토대로 Django Form의 동작을 살펴보면 다음과 같다.

> 1. 유저가 요청을 했을 때, 비어있는 Form을 만든 뒤 유저에게 전달한다.
> 2. 유저는 해당 Form에 데이터를 입력해서 다시 요청한다.
> 3. 데이터와 함께 넘어온 요청에 대해 유효성 검사를 진행한다.
> 4. 유효성 검사에 통과하지 못할 경우 **에러 메세지**와 함께 빈 Form을 유저에게 다시 전달한다.
> 5. 유효성 검사에 통과했을 경우 적절한 동작을 수행한 뒤 종료된다.

작성한 코드와 대조해보면 다음과 같다.

```python
def create(request):
    if request.method == 'POST': # (A)
        form = RecordForm(request.POST)
        if form.is_valid(): # (B)
            record = form.save()
            return redirect('records:detail', record.pk) # (C)
    else: # (D)
        form = RecordForm()
    context = {
        'form': form,
    }
    return render(request, 'records/create.html', context) # (E)
```

사용자가 데이터를 생성하려는 요청을 보내면 최초에는 데이터가 없는 GET 요청일 것이다. 이때 빈 Form을 만들어서 유저에게 랜더링해준다.**(D)**

유저는 Form에 데이터를 작성할 것이고 제출하여 POST 요청을 보낸다.**(A)** Django 서버는 유효성 검사를 통해서 적절한 행동을 취한다.**(B)**

유효성 검사에 통과했을 경우 그에 맞는 동작을 한 뒤 종료된다.**(C)**

유효성 검사에 통과 못하면 다시 빈 Form을 만들어서 사용자에게 에러메세지와 함께 다시 전달한다.**(D)**

### Widget

ModelForm 또한 Form처럼 Widget 적용이 가능하다.

```python
class RecordForm(forms.ModelForm):
    # 첫번째 방법
    pull_up = forms.CharField(
        label='턱걸이',
        widget=forms.TextInput(
            attrs={
                'class': 'pull_up',
                'placeholder': '턱걸이 개수'
            }
        )
    )

    class Meta:
        model = Record
        fields = '__all__'
        # 두번째 방법
        widgets = {
            'push_up': forms.TextInput(attrs={
                'class': 'push_up',
                'placeholder': '팔굽혀펴기 개수'
            })
        }
```

![img](https://velog.velcdn.com/images%2Fmain_string%2Fpost%2Fcee6d13c-e01e-435e-b380-88daadb0d76a%2Fimage.png)두번째 방법보다는 첫번째 방법이 권장된다.







##### 참조

> - https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/Forms
> - https://wayhome25.github.io/django/2017/05/06/django-form/
> - https://docs.djangoproject.com/en/3.2/topics/forms/
> - https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#modelform
> - https://www.geeksforgeeks.org/django-forms/