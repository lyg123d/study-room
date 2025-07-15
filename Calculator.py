expression = input('수식을 입력해주세요: ')

Calculator = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '/': lambda x, y: x / y,
              '*': lambda x, y: x * y
              }
