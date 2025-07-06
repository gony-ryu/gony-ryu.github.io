from PIL import Image, ImageDraw

# 원본 이미지 경로
input_file = "/Users/mukkbo/Desktop/goni_home/gony-ryu.github.io/images/bogoni-512x512.png"

# 출력 사이즈 & 파일명 리스트
sizes = [
    (180, "bogoni-180x180.png"),
    (32, "bogoni-32x32.png")
]

# 이미지 열기
with Image.open(input_file) as img:
    # 정사각형 crop을 위해 가장 짧은 변 찾기
    min_side = min(img.size)
    left = (img.width - min_side) // 2
    top = (img.height - min_side) // 2
    right = left + min_side
    bottom = top + min_side

    # 중심 정사각형 crop
    img_cropped = img.crop((left, top, right, bottom)).convert("RGBA")

    # 원형 마스크 생성
    mask = Image.new("L", (min_side, min_side), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, min_side, min_side), fill=255)

    # 마스크 적용해서 원형 이미지 만들기
    img_cropped.putalpha(mask)

    # 각각 원하는 크기로 저장
    for size, filename in sizes:
        resized_img = img_cropped.resize(
            (size, size),
            resample=Image.Resampling.LANCZOS
        )
        resized_img.save(filename, format="PNG")
        print(f"✅ Saved {filename} ({size}x{size}px)")