from geo import circle_area, circumference, rectangle_area, perimeter

def main():
    # 원 계산
    radius = 5
    print(f"원의 면적: {circle_area(radius):.2f}")
    print(f"원의 둘레: {circumference(radius):.2f}")

    # 직사각형 계산
    length = 10
    width = 4
    print(f"직사각형의 면적: {rectangle_area(length, width):.2f}")
    print(f"직사각형의 둘레: {perimeter(length, width):.2f}")

if __name__ == "__main__":
    main()
