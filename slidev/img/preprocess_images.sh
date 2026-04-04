uv run src/gradient_blur.py \
    --in slidev/img/tahoe-groeger-ioCEgIFVLos-unsplash.jpg \
    --out slidev/img/tahoe-groeger-ioCEgIFVLos-unsplash-blur.jpg \
    --direction left \
    --max-blur 25 \
    --n-strips 100

uv run src/gradient_blur.py \
    --in slidev/img/arturo-castaneyra-oBUUbfmHKwM-unsplash.jpg \
    --out slidev/img/arturo-castaneyra-oBUUbfmHKwM-unsplash-blur.jpg \
    --direction left \
    --max-blur 25 \
    --n-strips 100

uv run src/gradient_blur.py \
    --in slidev/img/arno-senoner-6lOxktnqo04-unsplash-flipped.jpg \
    --out slidev/img/arno-senoner-6lOxktnqo04-unsplash-flipped-blur.jpg \
    --direction left \
    --max-blur 5 \
    --n-strips 100
