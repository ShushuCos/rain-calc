# นำเข้าข้อความจากแต่ละภาษา
from Languages.en.en import messages as en_messages
from Languages.th.th import messages as th_messages

# ฟังก์ชันเลือกข้อความตามรหัสภาษา
def get_messages(language_code):
    """
    ส่งคืนข้อความ (message) ที่ตรงกับภาษาที่ผู้ใช้เลือก
    :param language_code: รหัสภาษา เช่น 'en' หรือ 'th'
    :return: ดิกชันนารีของข้อความตามภาษานั้น
    """
    if language_code == "th":
        return th_messages
    elif language_code == "en":
        return en_messages
    else:
        # ถ้าไม่รู้จักภาษา ให้ใช้ภาษาอังกฤษเป็นค่าเริ่มต้น
        print("Invalid language code. Defaulting to English.")
        return en_messages
