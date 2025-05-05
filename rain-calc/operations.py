# นำเข้าข้อความจากระบบภาษาที่เราเขียนไว้
from Languages.language import get_messages

msg = None  # ตัวแปรเก็บข้อความตามภาษาที่เลือก

# ฟังก์ชันสำหรับกำหนดภาษา เพื่อให้ระบบแสดงข้อความถูกต้อง
def set_language(language_code):
    global msg
    msg = get_messages(language_code)

# ฟังก์ชันบวกเลข
def add(a, b):
    return a + b

# ฟังก์ชันลบเลข
def subtract(a, b):
    return a - b

# ฟังก์ชันคูณเลข
def multiply(a, b):
    return a * b

# ฟังก์ชันหารเลข พร้อมเช็คว่าหารด้วยศูนย์หรือไม่
def divide(a, b):
    if b == 0:
        raise ValueError(msg["error"] + ": " + msg["divide_by_zero"])
    return a / b

# ฟังก์ชันรับตัวเลขจากผู้ใช้ พร้อมตรวจสอบว่าเป็นตัวเลขจริงหรือไม่
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(msg["invalid_number"])
