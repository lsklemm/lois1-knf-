# Лабораторная работа №1 по дисциплине "Логические основы интеллектуальных систем"
# Вариант E: Проверить, является ли формула КНФ
# Выполнена студенткой грруппы 021703 БГУИР Склема Елена Дмитриевна
# 23.03.2023

def formula_validation(expr):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for symbol in expr:
        if symbol not in '\/!()~' and symbol not in alphabet and symbol not in '01':
            return False
    if len(expr) == 1 and expr not in alphabet:
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
                if formula[symbol_index] == '(' and formula_validation(formula[symbol_index + 1]) and formula[symbol_index + 2] == ')':
                    return False
                elif formula[symbol_index] in alphabet.upper() and formula[symbol_index+1] in alphabet.upper():
                    return False

            return True
        except:
            return False


def double_brackets(expr):
    try:
        count = 0
        for index in range(len(expr)):
            if expr[index] == '(' and expr[index + 1] == '(':
                for index2 in range(index+2, len(expr)+1):
                    if expr[index2] in '\/~->' and expr[index2+1] in '\/~->':
                        count +=1
                    elif expr[index2] in '!':
                        count +=1
                    elif expr[index2] == ')' and expr[index2 + 1] == ')':
                        if count == 1:
                            return False
                        else:
                            return True
    except:
        return False

def is_cnf(expr):
    # Разбиваем выражение на конъюнкции
    clauses = expr.split('/\\')

    # Проверяем каждую конъюнкцию
    for clause in clauses:
        # Разбиваем конъюнкцию на дизъюнкции
        literals = clause.split('\/')

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
#((!A)/\(B\/C))
    # Если все условия выполнены, то выражение является КНФ
    return True


expr = input("Введите логическое выражение: ")
print(double_brackets(expr))
print(symbol_is_not_alone_in_brackets(expr))
if formula_validation(expr) and symbol_is_not_alone_in_brackets(expr) and double_brackets(expr):
    if is_cnf(expr):
        print("Выражение является КНФ")
    else:
        print("Выражение не является КНФ")
else:
    print('Формула введена некорректно')
# def correct_formula(formula: str) -> bool:
#     """
#     Проверяет наличие недопустимых символов
#     """
#     latin_alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     if len(formula) == 1:
#         if formula in latin_alphabet.upper() or formula in '01':
#             return True
#         else:
#             return False
#     else:
#         flag = False
#         for symbol in formula:
#             # if symbol in '{}_=<@#$%^&*.,?|+23456789' or symbol in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper():
#             #     return False
#             if symbol not in latin_alphabet or symbol not in '01' or symbol not in '()\/':
#                 return False
#             if symbol in latin_alphabet:
#                 return False
#
#         return True
#
#
#
# def symbol_is_not_alone_in_brackets(formula: str) -> bool:
#     """
#     Проевряет, что атомарная формула указана без скобок
#     """
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for symbol_index in range(0, len(formula)):
#         if formula[symbol_index] == '(' and correct_formula(formula[symbol_index + 1]) and formula[symbol_index + 2] == ')':
#             return False
#         elif formula[symbol_index] in alphabet.upper() and formula[symbol_index+1] in alphabet.upper():
#             return False
#
#     return True
#
#
#
# def correct_operator(formula:str)->bool:
#     """
#     Проверяет, верно ли введены все операторы
#     """
#     new_formula = formula.replace('\/', 'v').replace('/\\', '^')
#     for index in range(len(formula)):
#         if formula[index] == '!':
#             if formula[index - 1] != '(':
#                 return False
#
#     if len(formula) == 1:
#         return True
#     elif '\\' in new_formula or '/' in new_formula:
#         return False
#     else:
#         return True
#
#
#
# def brackets_count(formula:str) -> bool:
#     """
#     Проверяет, что количество открывающихся круглых скобок равно количеству закрывающихся
#     """
#     left_bracket_count = 0
#     right_bracket_count = 0
#     i = 0
#     for i in formula:
#         if i == '(':
#             left_bracket_count += 1
#         elif i == ')':
#             right_bracket_count += 1;
#
#     if left_bracket_count == 0 and right_bracket_count == 0 and len(formula) == 1:
#         return True
#     elif left_bracket_count == 0 and right_bracket_count == 0 and len(formula) != 1:
#         return False
#     elif left_bracket_count == right_bracket_count:
#         return True
#     else:
#         return False
#
#
#
#
# def modify_formula(formula:str)->str:
#     """
#     Преобразует формулу в вид, необходимый для произведения вычислений
#     """
#     new_formula = ''
#     vars = []
#     for symbol in formula:
#         if symbol not in 'v^>~!()':
#             if symbol not in vars:
#                 vars.append(symbol)
#             new_formula += symbol
#         elif symbol == '(' or symbol == ')':
#             new_formula += symbol
#         elif symbol == '!':
#             new_formula += ' not '
#         elif symbol == '^':
#             new_formula += ' and '
#         elif symbol == 'v':
#             new_formula += ' or '
#         elif symbol == '~':
#             new_formula += ' == '
#         elif symbol == '>':
#             new_formula += ' <= '
#
#     return new_formula, vars
#
#
#
#
# def alphabet_symbols_count(formula:str)->int:
#     """
#     Метод считает количество символов, принадлежащих алфавиту
#     :param formula:
#     :return:
#     """
#     alphabet = 'abcdeffghijklmnopqrstuvwxxyz01'
#     count = 0
#     for symbol in formula:
#         if symbol in alphabet.upper():
#             count += 1
#     return count
#
#
#
#
# def build_truth_table(formula:str, vars:list)->list:
#     """
#     Построение таблицы истинности
#     """
#     truth_table = []
#     for index in range(2 ** len(vars)):
#         binary_number = bin(index)[2::]
#         if len(binary_number) != len(vars):
#             truth_table_row = '0'*(len(vars)-len(binary_number)) + binary_number
#             truth_table.append(truth_table_row)
#         else:
#             truth_table.append(binary_number)
#
#     truth_table_result = []
#
#     for truth_table_row in truth_table:
#         buf_formula = formula
#         for symbol in formula:
#             if symbol in vars:
#                 buf_formula = buf_formula.replace(symbol, truth_table_row[vars.index(symbol)])
#         try:
#             truth_table_result.append(eval(buf_formula))
#         except:
#             print('Неверный формат формулы')
#             raise SystemExit
#     return truth_table, truth_table_result
#
#
#
#
# def build_pdnf(formula:str):
#     """
#     Построение СДНФ в соответствии с таблицей истиности
#     :param formula:
#     :return:
#     """
#     formula, vars = modify_formula(formula)
#     truth_table, truth_table_result = build_truth_table(formula, vars)
#     if formula in '01':
#         print('Формула не является СДНФ')
#
#     else:
#         pdnf_formula = ''
#         if alphabet_symbols_count(formula) != 1:
#             pdnf_formula += '('
#         pdnf_formulas_list = []
#         truth_table_pdnf = []
#
#         for index in range(len(truth_table_result)):
#             if truth_table_result[index] == 1:
#                 truth_table_pdnf.append(truth_table[index])
#
#
#         for expression in truth_table_pdnf:
#             pdnf_formula_expression = []
#             for value_index in range(len(expression)):
#                 if expression[value_index] == '0':
#                     pdnf_formula_expression.append(f'(!{vars[value_index]})')
#                 else:
#                     pdnf_formula_expression.append(f'{vars[value_index]}')
#
#             pdnf_formulas_list.append(pdnf_formula_expression)
#
#
#         for expression in pdnf_formulas_list:
#             if pdnf_formulas_list.index(expression) == len(pdnf_formulas_list)-1:
#                 if len(expression) == 1:
#                     pdnf_formula += f'{expression[0]}'
#                 else:
#                     for value in expression:
#                         if expression.index(value) == len(expression)-1:
#                             pdnf_formula += f'{value})'
#                         else:
#                             pdnf_formula += f'({value}/\\'
#             else:
#                 for value in expression:
#                     if expression.index(value) == len(expression)-1:
#                         pdnf_formula += f'{value})\/'
#                     else:
#                         pdnf_formula += f'({value}/\\'
#
#         if not brackets_count(pdnf_formula):
#             pdnf_formula += ')'
#
#     return pdnf_formula
#
#
#
#
# def logical_formula(formula: str)->bool:
#     """
#     Проверяет, правильно ли введена формула
#     """
#     if correct_formula(formula) and brackets_count(formula) and correct_operator(formula) and ' ' not in formula:
#         if len(formula) != 1:
#             if symbol_is_not_alone_in_brackets(formula):
#                 formula = formula.replace('\/', 'v').replace('/\\', '^').replace('->', '>')
#                 pdnf = build_pdnf(formula)
#                 return pdnf
#             else:
#                 print('Ошибка ввода формулы\n')
#         else:
#             formula = formula.replace('\/', 'v').replace('/\\', '^').replace('->', '>')
#             pdnf = build_pdnf(formula)
#             return pdnf
#
#     else:
#         print('Ошибка ввода формулы\n')
#
#
#
#
# def compare(sdnf, formula):
#     """
#     Сравнивает полученную формулу СKНФ и введенную пользователем формулу
#     """
#     sdnf = sdnf.replace('(', '').replace(')', '').replace('/\\', '^').replace('\/', 'v')
#     sdnf_expressions = sdnf.split('v')
#     sdnf_symbols = []
#     for expression in sdnf_expressions:
#         sdnf_symbols.append(expression.split('^'))
#
#
#     formula = formula.replace('(','').replace(')','').replace('/\\','^').replace('\/', 'v')
#     formula_expressions = formula.split('v')
#     formula_symbols = []
#     for expression in formula_expressions:
#         formula_symbols.append(expression.split('^'))
#
#
#     if len(formula_symbols) != len(sdnf_symbols):
#         return 'Формула не является СKНФ'
#     for i in range(len(formula_symbols)):
#         if len(formula_symbols[i]) != len(sdnf_symbols[i]):
#             return 'Формула не является СKНФ'
#
#     compare_list = []
#     for item1 in sdnf_symbols:
#         for item2 in formula_symbols:
#             if set(item1) == set(item2):
#                 compare_list.append(True)
#
#
#     if False in compare_list or len(compare_list) == 0:
#         return 'Формула не является СKНФ'
#     else:
#         return 'Формула является СKНФ'
#
#
# #(((!P)/\Q)\/(P/\(!Q))\/(Q/\P))
# #(((!P)/\Q)\/(P/\(!Q))\/((!Q)/\(!P)))
# #(((!A)\/B)->S)
# #(((!A)/\(!B)/\S)\/((!A)/\B/\S)\/(A/\(!B)/\(!S))\/(A/\(!B)/\S)\/(A/\B/\S))
#
# # (((A/\B)/\C)\/(((A/\B)/\(!C))\/(((A/\(!B))/\C)\/(((A/\(!B))/\(!C))\/((((!A)/\B)/\C)\/((((!A)/\(!B))/\C)\/((((!A)/\B)/\(!C))\/((((!A)/\(!B))/\(!C))))))))))
#
# if __name__ == '__main__':
#     formula = input('Введите СKНФ формулу:    ')
#     # print(logical_formula(formula))
#     try:
#         sdnf = logical_formula(formula)
#         if sdnf:
#             print('Полученная СKНФ формула:', sdnf)
#             print(compare(sdnf, formula))
#     except:
#         raise SystemExit


# (A/\(B/\(C/\(D/\(E/\(F/\(G/\(H/\(I/\(J/\(K/\(L/\(M/\(N/\(O/\(P/\(Q/\(R/\(S/\(T/\(U/\(Y/\(W/\(X/\(V/\Z)))))))))))))))))))))))))