def add_numbers(a: int, b: int) -> int:

    return a + b



i: int = "string"  # Lỗi 1: Kiểu chuỗi gán cho biến kiểu int

x: str = 123  # Lỗi 2: Kiểu số nguyên gán cho biến kiểu chuỗi



def divide_numbers(a: int, b: int) -> float:

    return a / b



result: float = divide_numbers(10, "5")  # Lỗi 3: Kiểu chuỗi gán cho tham số kiểu int

y: float = add_numbers(3, 2.5)  # Lỗi 4: add_numbers yêu cầu tham số kiểu int, nhưng 2.5 là float
