# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# Вариант E: Проверить, является ли формула КНФ
# Выполнена студенткой грруппы 021703 БГУИР Склема Елена Дмитриевна
# 23.03.2023

#((A\/B)/\((!B)\/C\/(!D))/\(D\/(!E)))
#((!A)/\(B\/C))
#(A/\B)

#(!(B\/C))
#((A/\B)\/C)
#((A/\(B\/(D/\E))))

def formula_validation(expr):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for symbol in expr:
        if symbol not in '\/!()~->' and symbol not in alphabet and symbol not in '01':
            return False

    if len(expr) == 1 and expr not in alphabet and expr != '1' and expr != '0':
        return False
    for index in range(len(expr)):
        if expr[index] == ')' and index + 1 != len(expr):
            if expr[index + 1] == '(':
                return False
        elif expr[index] in alphabet:
            if expr[index + 1] in '01':
                return False

    return True


def symbol_is_not_alone_in_brackets(formula: str) -> bool:
    """
    Проевряет, что атомарная формула указана без скобок
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(formula) > 1:
        try:
            for symbol_index in range(0, len(formula)):
                # if formula[symbol_index] == '(' and formula_validation(formula[symbol_index + 1]) and formula[symbol_index + 2] == ')':
                #     return False
                if formula[symbol_index] in alphabet.upper() and formula[symbol_index+1] in alphabet.upper():
                    return False
                elif formula[symbol_index] == '!' and (formula[symbol_index + 1] == ')' or formula[symbol_index - 1] != '('):
                    return False

            return True
        except:
            return False
    else:
        return True


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
                            if  expr[index2 + 1] == ')':
                                break
    # print(count)
    if count == 1:
        return False
    else:
        return True





def is_cnf(expr):
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
            # for s in literal:
            #     if s.isalpha():
            #         print(s)

            if len(literal.strip()) > 1 and (literal[0] != '!' or not literal[1:].isalpha()):
                return False
    # Если все условия выполнены, то выражение является КНФ
    return True


expr = input("Введите логическое выражение: ")
print(formula_validation(expr))
print(double_brackets(expr))
print(symbol_is_not_alone_in_brackets(expr))
if formula_validation(expr) and symbol_is_not_alone_in_brackets(expr) and double_brackets(expr):
    if is_cnf(expr):
        print("Выражение является КНФ")
    else:
        print("Выражение не является КНФ")
else:
    print('Формула введена некорректно')