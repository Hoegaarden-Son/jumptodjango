from PIL import Image

source = "nav/4.webp"
target_name = "nav/4"

# WEBP 파일 열기
img = Image.open(source)


def to_png():
    # PNG나 JPG로 저장
    img.save(f"{target_name}.png", "PNG")  # PNG 형식으로 저장


def to_jpg():
    img.save(f"{target_name}.jpg", "JPEG") # JPG 형식으로 저장


to_png()
