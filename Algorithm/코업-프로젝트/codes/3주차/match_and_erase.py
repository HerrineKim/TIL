# 짝지어 제거하기
# 예전에 풀었던 스택 문제와 비슷하다
# swea 4873번 문제와 거의 같다
def solution(s):
    stack = []
    # 스택을 만들어 연속으로 같은 값이 나오면 터뜨리고, 아니면 그냥 남기기(테트리스처럼)
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    # 전부 쌍을 이뤄서 최종적으로 스택이 비었으면 성공!
    if len(stack) == 0:
        return 1
    # 스택에 외로운 글자들이 남아 있으면 실패!
    else:
        return 0