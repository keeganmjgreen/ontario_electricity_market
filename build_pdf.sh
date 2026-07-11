rm -rf _build/temp
uv run jupyter book build --pdf

pdftoppm -f 1 -l 1 -png how_electricity_markets_work.pdf > img/pdf_page_1.png
pdftoppm -f 11 -l 11 -png how_electricity_markets_work.pdf > img/pdf_page_2.png
pdftoppm -f 16 -l 16 -png how_electricity_markets_work.pdf > img/pdf_page_3.png
