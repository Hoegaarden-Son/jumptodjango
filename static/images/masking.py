from PIL import Image, ImageDraw

def make_circular_and_transparent(input_path, output_path):
    # 이미지 열기 및 RGBA 모드로 변환
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    # 배경 색상 범위 (노랑, 파랑, 옅은 회색-파랑) 설정하여 투명 처리
    new_data = []
    for item in datas:
        # 노란색 계열
        if ((item[0] > 250 and item[1] > 240 and item[2] < 220) or
            (item[0] < 100 and item[1] < 180 and item[2] > 200) or
            (item[0] > 200 and item[1] > 200 and item[2] > 220)):
            new_data.append((255, 255, 255, 0))  # 투명 처리
    else:
        new_data.append(item)

    img.putdata(new_data)

    # 원형 마스크 생성
    size = img.size
    mask = Image.new("L", size, 0)
    mask_draw = ImageDraw.Draw(mask)
    center_x, center_y = size[0] // 2, size[1] // 2
    radius = min(center_x, center_y)
    mask_draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=255)

    # 원형 마스크를 이미지에 적용
    circular_img = Image.new("RGBA", size)
    circular_img.paste(img, (0, 0), mask=mask)

    # 결과 저장
    circular_img.save(output_path, "PNG")


# 사용 예시
make_circular_and_transparent("nav/3.png", "masked_3.png")
