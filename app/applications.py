from . import data_structures

# 1. Stack application
def balanced_parentheses_checker(symbol_string):
    """Verify that a set of parentheses is balanced."""

    opening_symbols = '{[('
    closing_symbols = '}])'

    opening_symbols_stack = data_structures.Stack()
    symbol_count = len(symbol_string)
    counter = 0

    while counter < symbol_count:
        current_symbol = symbol_string[counter]
        if current_symbol in '{[(':
            opening_symbols_stack.push(current_symbol)
        else:
            if not opening_symbols_stack.is_empty() and \
            opening_symbols.index(opening_symbols_stack.peek()) == \
            closing_symbols.index(current_symbol):
                opening_symbols_stack.pop()
            else:
                counter = symbol_count

        counter += 1

    return opening_symbols_stack.is_empty() and counter == symbol_count


if __name__ == '__main__':
    print(balanced_parentheses_checker('[]{[]{([][])}()}'))
