# นำเข้าฟังก์ชันต่าง ๆ จาก modules ที่เราเขียนไว้
from operations import add, subtract, multiply, divide, get_number, set_language
from Languages.language import get_messages

# ฟังก์ชันหลักที่ใช้ในการทำงานของเครื่องคิดเลข
def calculate():
    # เลือกภาษา (en หรือ th)
    while True:
        lang = input("เลือกภาษา (en/th): ").strip().lower()
        if lang in ['en', 'th']:
            break
        print("กรุณาเลือกภาษาให้ถูกต้อง (en หรือ th)")

    # ดึงข้อความตามภาษาที่เลือก
    msg = get_messages(lang)
    set_language(lang)

    # แสดงข้อความต้อนรับและเมนู
    print(msg["welcome"])
    for line in msg["menu"]:
        print(line)

    # ลูปหลักของเครื่องคิดเลข
    while True:
        choice = input(msg["prompt_choice"])  # รับเมนูที่ผู้ใช้เลือก

        # ถ้าผู้ใช้เลือกเมนู 5 ให้ออกจากโปรแกรม
        if choice == '5':
            print(msg["exit"])
            break

        # ถ้าเลือกเมนูไม่ถูกต้อง
        if choice not in ['1', '2', '3', '4']:
            print(msg["invalid_choice"])
            continue

        # รับค่าตัวเลขจากผู้ใช้
        num1 = get_number(msg["prompt_num1"])
        num2 = get_number(msg["prompt_num2"])

        # เรียกฟังก์ชันคำนวณตามเมนู
        if choice == '1':
            print(f"{msg['result']}: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{msg['result']}: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{msg['result']}: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            try:
                print(f"{msg['result']}: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(f"{msg['error']}: {e}")

# ถ้าเปิดไฟล์นี้โดยตรง (ไม่ใช่ถูก import)
if __name__ == "__main__":
    calculate()
