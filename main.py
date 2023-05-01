# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# Вариант E: Проверить, является ли формула КНФ
# Выполнена студенткой грруппы 021703 БГУИР Склема Елена Дмитриевна
# 23.03.2023

#((A\/B)/\((!B)\/C\/(!D))/\(D\/(!E)))
#((A\/B\/(!C))(A\/C)(B\/(!C)))
#((!A)/\(B\/C))
#(A/\B)

#(!(B\/C))
#((A/\B)\/C)
#((A/\B)\/C)

def correct_operator(expr):
    new_expr = expr.replace('\/','v').replace('/\\', '^')
    for symbol in new_expr:
        if symbol in '\/':
            return False
    return True

#Проверка на корректность введенных данных
def formula_validation(expr):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if len(expr) == 1:
        if expr not in alphabet:
            return False
        else:
            return True
    else:
        if expr[0] != '(':
            return False
        if '(' not in expr and ')' not in expr:
            return False
        for symbol in expr:
            if symbol not in '\/!()~->' and symbol not in alphabet and symbol not in '01':
                return False

        for index in range(len(expr)):
            if expr[index] == ')' and index + 1 != len(expr):
                if expr[index + 1] == '(':
                    return False
            elif expr[index] in alphabet:
                if expr[index + 1] in '01':
                    return False

        return True


#Проверка, что символ находится в скобках не один
def symbol_is_not_alone_in_brackets(expr: str) -> bool:

    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ01'
    if len(expr) > 1:
        try:
            for symbol_index in range(0, len(expr)):
                if expr[symbol_index] == '(' and expr[symbol_index + 1] in symbols and expr[symbol_index + 2] == ')':
                    return False
                # if formula_validation(formula[symbol_index + 1]):
                #     return False
                elif expr[symbol_index] in symbols and expr[symbol_index + 1] in symbols:
                    return False
                elif expr[symbol_index] == '!' and (expr[symbol_index + 1] == ')' or expr[symbol_index - 1] != '('):
                    return False
                # elif formula[symbol_index] == '~' and (formula[symbol_index + 1] == ')' or formula[symbol_index - 1] != '('):
                #     return False

            return True
        except:
            return False
    else:
        return True


#Проверка на лишние двойные скобки
def double_brackets(expr):
    count = 0
    for index in range(len(expr)):
        if expr[index] == '(':
            if expr[index + 1] == '(':
                for index2 in range(index+2, len(expr)):
                    if expr[index2] in '\/-' and expr[index2+1] in '\/>':
                        count +=1
                    elif expr[index2] in '!':
                        if expr[index2 + 1] == '!':
                            return False
                        else:
                            count +=1
                    elif expr[index2] == ')':
                        if index2 + 1 == len(expr):
                            return True
                        else:
                            if expr[index2 + 1] == ')':
                                break
    # print(count)
    if count == 2:
        return False
    else:
        return True





def is_cnf(expr):
    # Проверяем, что количество открывающих скобок равно количеству закрывающих скобок
    if expr.count('(') != expr.count(')'):
        return False

    # Разбиваем выражение на конъюнкции
    clauses = expr.split('/\\')

    # Проверяем каждую конъюнкцию
    for clause in clauses:
        # Разбиваем конъюнкцию на дизъюнкции
        literals = clause.split('\/')
        new_literal = []

        # Проверяем каждый литерал в дизъюнкции
        for literal in literals:

            # Проверяем, что литерал не содержит логических связок И или ИЛИ
            if '\/' in literal or '/\\' in literal:
                return False

            # Проверяем, что литерал содержит только переменную или ее отрицание
            new_literal = ''
            for s in literal:
                if s != '(' and s != ')':
                    new_literal += s
            if len(new_literal.strip()) > 1 and (new_literal[0] != '!' or not new_literal[1:].isalpha()):
                print(new_literal)
                print('here')
                return False
        # Если все условия выполнены, то выражение является КНФ
        return True


expr = input("Введите логическое выражение: ")
# print(formula_validation(expr))
# print(double_brackets(expr))
# print(symbol_is_not_alone_in_brackets(expr))

if formula_validation(expr):
    if symbol_is_not_alone_in_brackets(expr):
        if double_brackets(expr):
            if correct_operator(expr):
                if is_cnf(expr):
                    print("Выражение является КНФ")
                else:
                    print("Выражение не является КНФ")
            else:
                print('Формула введена некорректно(1)')
        else:
            print('Формула введена некорректно(2)')
    else:
        print('Формула введена некорректно(3)')
else:
    print('Формула введена некорректно(4)')

# (((A\/B)\/C)/\((!A)\/((B\/C)/\(A\/((!B)\/C))))
# ((((A\/B)\/C)/\((A\/(!B))\/C))/\(((!A)\/B)\/C))
#((A/\B/\C))
#((A\/(!B))/\())

#1,0
#(A/\/B)
#A(\/A)
#\/A

