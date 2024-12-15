from typing import List

def process_numbers(numbers: List, divisor: int) -> List[float]:  # List thiếu kiểu
    return [num / divisor for num in numbers]

result = process_numbers(["1", "2", "3"], 0)  # Lỗi: danh sách chuỗi và chia cho số không
print(result)
