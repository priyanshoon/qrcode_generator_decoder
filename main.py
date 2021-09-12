import cv2
import random
import qrcode


def qrcode_generator(data):
    img = qrcode.make(data)
    random_file_name = str(random.randint(1000, 9999)) + '.jpg'
    print(random_file_name + ' has been saved.')
    img.save(random_file_name)


def qrcode_decoder(file_name):
    d = cv2.QRCodeDetector()
    val, _, _ = d.detectAndDecode(cv2.imread(file_name))
    print("Decoded text is: ", val)


if __name__ == "__main__":
    user_input = int(input('Press 1 to make qrcode '
                           'Press 2 to decode qrcode: '))
    if user_input == 1:
        user_data_to_qrcode = input('Enter your data which you want to save in your qrcode: ')
        qrcode_generator(user_data_to_qrcode)
    else:
        user_file_input = input('Enter your file name which you want to decode: ')
        qrcode_decoder(user_file_input)
