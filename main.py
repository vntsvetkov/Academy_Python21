from data_structure.stack import Stack
from data_structure.queue import Queue

"""
Task 1. Дана скобочная последовательность. Нужно определить, правильная она или нет. 

Каждой открывающей скобке в последовательности соответствует закрывающая, образуя пары.

Будем считать строку «правильной» если все скобки закрываются в нужном порядке, т.е:

1. для каждой открывающей есть закрывающая из той же пары;
2. скобки закрываются в правильном порядке.
3. Пустая строка считается правильной.

Программе на вход подаётся последовательность из скобок трёх видов: [], (), {}.

Напишите функцию is_correct_brackets, которая принимает на вход скобочную последовательность и возвращает True, 
если последовательность правильная, а иначе возвращает False.
"""


def is_correct_brackets(sequence: str) -> bool:
    brackets = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    s = Stack()
    for symbol in sequence:
        if symbol in brackets.keys():
            s.push(symbol)
        elif not s.is_empty() and symbol == brackets[s.peek()]:
            s.pop()
        else:
            return False

    if s.is_empty():
        return True
    return False


"""
Task 2. Реализовать алгоритм вычисления выражения по обратной польской записи.

Обратная польская нотация или постфиксная нотация — форма записи математических и логических выражений, 
в которой операнды расположены перед знаками операций. Выражение читается слева направо. 
Когда в выражении встречается знак операции, выполняется соответствующая операция над двумя ближайшими операндами, 
находящимися слева от знака операции. Результат операции заменяет в выражении последовательность её операндов и знак, 
после чего выражение вычисляется дальше по тому же правилу. Таким образом, результатом вычисления всего выражения 
становится результат последней вычисленной операции.

Например, выражение (1 + 2) * 4 + 3 в постфиксной нотации будет выглядеть так: 1 2 + 4 * 3 +, а результат: 15.

Реализуйте метод get_expression_value() класса Expression в файле expression.py, 
который принимает список, каждый элемент которого содержит число или знак операции (+, -, *, /). 
Функция должна вернуть результат вычисления по обратной польской записи.

Для вычисления значения выражения, записанного в постфиксной форме, можно использовать описанный далее алгоритм. 
На вход подается последовательность лексем (числа или знаки операций), представляющая некоторое арифметическое выражение, 
записанное в постфиксной форме. Результатом работы алгоритма является значение этого выражения.

1. Если не достигнут конец входной последовательности, прочитать очередную лексему.
2. Если прочитан операнд (число), положить его в стек.
3. Если прочитан знак операции, вытолкнуть из стека два операнда и положить в стек результат применения прочитанной операции к этим операндам, взятым в обратном порядке.
4. Если достигнут конец входной последовательности, завершить работу. В стеке останется единственное число — значение выражения.

"""

"""
Task 3. Перевести выражение из инфиксной формы в постфиксную форму записи.

Говорят, что выражение записано в инфиксной форме, если знак операции (сложения, умножения, вычитания либо деления) 
стоит между своими аргументами, например, 5 + 7. Каждая операция имеет приоритет выполнения (сначала выполняются умножение и деление, затем сложение и вычитание). 
Для изменения приоритета выполнения операций используются круглые скобки. Вычислять значение выражения, записанного в инфиксной форме, неудобно. Проще сначала перевести его в постфиксную.

Для перевода выражения из инфиксной формы в постфиксную с учетом приоритетов операций и скобок существует простой алгоритм.
Алгоритм работает со стеком, в котором хранятся знаки операций. Сначала стек пуст. На вход алгоритму подается последовательность лексем (числа, скобки или знаки операций), 
представляющая некоторое арифметическое выражение, записанное в инфиксной форме. Результатом работы алгоритма является эквивалентное выражение в постфиксной форме. 
Вводятся приоритеты операций: открывающая скобка имеет приоритет 0, знаки + и – — приоритет 1 и знаки * и / — приоритет 2.

Алгоритм:
1. Если не достигнут конец входной последовательности, прочитать очередную лексему.
    1.1. Если прочитан операнд (число), записать его в выходную последовательность.
    1.2. Если прочитана открывающая скобка, положить ее в стек.
    1.3. Если прочитана закрывающая скобка, вытолкнуть из стека в выходную последовательность все до открывающей скобки. Сами скобки уничтожаются.
    1.4. Если прочитан знак операции, вытолкнуть из стека в выходную последовательность все операции с большим либо равным приоритетом, а прочитанную операцию положить в стек.
2. Если достигнут конец входной последовательности, вытолкнуть все из стека в выходную последовательность и завершить работу.

Реализуйте метод to_postfix класса ExpressionConverter в файле expression.py и протестируйте класс Expression. 
"""


def execute_application():
    s = "([{}])"
    print(is_correct_brackets(s))


if __name__ == "__main__":
    execute_application()