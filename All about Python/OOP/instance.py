# 클래스 정의 (Person)
class Person:
    # 인스턴스 메서드
    # Python 내부적으로 Person.test(p1)
    def test(self):
        return self

# 인스턴스 생성 (p1)
p1 = Person()

# p1.test()
# TypeError: test() takes 0 positional arguments but 1 was given

# <__main__.Person object at 0x00000228B53D4F70>
# Python 내부적으로 Person.test(p1)
s = p1.test()
print(s, p1)

