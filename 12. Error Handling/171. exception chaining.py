try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("A math error caused a value issue") from e