"""Reference arithmetic model for Mechanical Multiplier X2D.

This software verifies expected results only. It is not part of the physical
machine's arithmetic path.
"""


def add_decimal_digits(accumulator: int, addend: int) -> int:
    """Return accumulator + addend using explicit decimal carry propagation."""
    if accumulator < 0 or addend < 0:
        raise ValueError("This prototype model supports non-negative integers only.")

    a = list(map(int, str(accumulator)))
    b = list(map(int, str(addend)))
    width = max(len(a), len(b))
    a = [0] * (width - len(a)) + a
    b = [0] * (width - len(b)) + b

    result = [0] * width
    carry = 0
    for i in range(width - 1, -1, -1):
        total = a[i] + b[i] + carry
        result[i] = total % 10
        carry = total // 10

    if carry:
        result.insert(0, carry)
    return int("".join(map(str, result)))


def multiply_by_repeated_addition(multiplicand: int, multiplier: int) -> int:
    """Multiply non-negative integers using repeated addition."""
    if multiplicand < 0 or multiplier < 0:
        raise ValueError("This prototype model supports non-negative integers only.")

    accumulator = 0
    for _ in range(multiplier):
        accumulator = add_decimal_digits(accumulator, multiplicand)
    return accumulator


if __name__ == "__main__":
    for a, b in [(7, 8), (12, 13), (99, 1), (99, 99), (0, 123), (123, 0)]:
        print(f"{a} × {b} = {multiply_by_repeated_addition(a, b)}")
