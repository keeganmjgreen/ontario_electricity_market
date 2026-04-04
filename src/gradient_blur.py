# /// script
# dependencies = [
#   "pillow"
# ]
# ///

import argparse
from enum import StrEnum

from PIL import Image, ImageFilter


class Direction(StrEnum):
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


def blur_gradient(
    input_image: Image.Image,
    max_blur: float,
    n_strips: int,
    direction: Direction,
) -> Image.Image:
    width, height = input_image.size
    output_image = input_image.copy()

    is_horizontal = direction in (Direction.LEFT, Direction.RIGHT)
    is_reversed = direction in (Direction.LEFT, Direction.DOWN)

    if is_horizontal:
        # Horizontal gradient
        for i in range(n_strips):
            progress = i / n_strips
            if is_reversed:
                progress = 1 - progress

            blur_amount = int(progress * max_blur)
            blurred = input_image.filter(ImageFilter.GaussianBlur(radius=blur_amount))

            x_start = int((i / n_strips) * width)
            x_end = int(((i + 1) / n_strips) * width)

            strip = blurred.crop((x_start, 0, x_end, height))
            output_image.paste(strip, (x_start, 0))
    else:
        # Vertical gradient
        for i in range(n_strips):
            progress = i / n_strips
            if is_reversed:
                progress = 1 - progress

            blur_amount = int(progress * max_blur)
            blurred = input_image.filter(ImageFilter.GaussianBlur(radius=blur_amount))

            y_start = int((i / n_strips) * height)
            y_end = int(((i + 1) / n_strips) * height)

            strip = blurred.crop((0, y_start, width, y_end))
            output_image.paste(strip, (0, y_start))

    return output_image


def main():
    parser = argparse.ArgumentParser(
        description="Create a directional blur gradient on an image",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example:
  python gradient_blur.py --in input.png --out output.png --direction up
  python gradient_blur.py --in input.png --out output.png --direction up --max-blur 30 --n-strips 100
        """,
    )

    parser.add_argument(
        "--in",
        dest="input_file",
        required=True,
        help="Input image path",
    )
    parser.add_argument(
        "--out",
        dest="output_file",
        required=True,
        help="Output image path",
    )
    parser.add_argument(
        "--max-blur",
        type=float,
        default=25,
        help="Maximum blur radius (default: 25)",
    )
    parser.add_argument(
        "--n-strips",
        type=int,
        default=50,
        help="Number of strips for smooth gradient (default: 50)",
    )
    parser.add_argument(
        "--direction",
        choices=Direction,
        default=Direction.RIGHT,
        help="Blur gradient direction (default: right)",
    )

    args = parser.parse_args()

    try:
        image = Image.open(args.input_file)
        output = blur_gradient(
            image,
            max_blur=args.max_blur,
            n_strips=args.n_strips,
            direction=args.direction,
        )
        output.save(args.output_file)
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found")
        exit(1)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == "__main__":
    main()
