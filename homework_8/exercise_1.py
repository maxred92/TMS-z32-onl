""" 1. Декодировать в строку байтовое значение b'r\xc3\xa9sum\xc3\xa9'
Затем результат преобразовать в байтовый вид в кодировке «uft-8» и затем результат
снова декодировать в строку с применением кодировки «utf-16». Результаты каждой операции 
с пояснениями выводить на печать
 """

x = b'r\xc3\xa9sum\xc3\xa9'
decode_x = x.decode()
byte_x = decode_x.encode('utf-8')
decode_utf16 = byte_x.decode("utf-16")

print(f'Decoded byte value x: {decode_x}', 
f'Encoded value in utf-8 byte: {byte_x}',f'Decoded byte value to utf-16: {decode_utf16}',sep='\n')