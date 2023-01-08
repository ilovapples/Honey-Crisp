from PIL import Image
def image(path, TO_png_jpg_webp):
    FROM_png_jpg_webp = path[path.rindex('.')+1:]
    
    newPath = path.replace(FROM_png_jpg_webp, TO_png_jpg_webp)
    
    image = Image.open(path).convert("RGB")
    
    if FROM_png_jpg_webp == "png":
        if TO_png_jpg_webp == "jpg":
            image.save(newPath, TO_png_jpg_webp)
        elif TO_png_jpg_webp == "webp":
            image.save(newPath, TO_png_jpg_webp)
    elif FROM_png_jpg_webp == "jpg":
        if TO_png_jpg_webp == "png":
            image.save(newPath, TO_png_jpg_webp)
        elif TO_png_jpg_webp == "webp":
            image.save(newPath, TO_png_jpg_webp)
    elif FROM_png_jpg_webp == "webp":
        if TO_png_jpg_webp == "png":
            image.save(newPath, TO_png_jpg_webp)
        elif TO_png_jpg_webp == "jpg":
            image.save(newPath, TO_png_jpg_webp)

image(input("Path to image: "), input("File type to convert to: "))