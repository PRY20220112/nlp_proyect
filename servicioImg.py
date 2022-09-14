from PIL import Image, ImageDraw
import io

new = Image.new('RGB', (200, 300), color=(0, 0, 0))

d = ImageDraw.Draw(new)
d.text((100, 100), "Paciente", fill=(255, 255, 255))
d.text((200, 100), "Paciente", fill=(255, 255, 255))


img_byte_arr = io.BytesIO()

new.save(img_byte_arr, format='PNG')

img_byte_arr = img_byte_arr.getvalue()

print(img_byte_arr)
