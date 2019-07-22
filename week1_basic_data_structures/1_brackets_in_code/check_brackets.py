# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = list()
    for i, next in enumerate(text):
        # print(i, next)
        if next in "([{":
            # Process opening bracket, write your code here
            bracket = Bracket(next, i + 1)
            opening_brackets_stack.append(bracket)

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                open_brac = opening_brackets_stack.pop()
                match = are_matching(open_brac.char, next)
                if match:
                    pass
                else:
                    return i + 1
            else:
                return i + 1

    # print(len(text))
    # print(opening_brackets_stack)
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack.pop().position
    else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
