mode = input("덧셈 or 곱셈 중 선택하세요 (덧셈/곱셈): ")

inputs = input("a, b중 하나 이상 입력 (공백 구분): "). split(' ')
a = inputs[0] if len(inputs) > 0 else ''
b = inputs[1] if len(inputs) > 1 else ''

def SingleMultiPlication(n):
    n = int(n)
    for i in range(1, 10):
        print(f'{n} * {i} = {n*i}')

def MultiPlication(start, end):
    start = int(start)
    end = int(end)
    for i in range(start, end + 1):
        for x in range(1, 10):
            print(f'{i} * {x} = {i*x}')
        print()

def Addition(a, b):
    a = int(a)
    b = int(b)
    print(f'{a} + {b} = {a+b}')
if mode == '곱셈':
    if a != '' and b == '':
        SingleMultiPlication(a)
    elif a != '' and b != '':
        start = min(int(a), int(b))
        end = max(int(a), int(b))
        MultiPlication(start, end)
    else:
        print("곱셈을 위해 1개 또는 2개의 숫자를 입력하세요.")
    
elif mode == '덧셈':
    if a != '' and b != '':
        Addition(a, b)
    else:
        print("2개의 숫자가 필요합니다.")
elif mode != '곱셈' or '덧셈':
    print("다시 입력해주세요.")