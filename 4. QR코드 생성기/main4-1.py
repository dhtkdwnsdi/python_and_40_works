#QR코드 생성기
import qrcode
from PIL import Image

qr_data = 'www.naver.com'
qr_img = qrcode.make(qr_data)

#save_path = '4. QR코드 생성기\\' + qr_data + '.png'
save_path = qr_data + '.png'
qr_img.save(save_path)
