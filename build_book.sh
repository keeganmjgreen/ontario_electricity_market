gsed -i 's/:width: 64%/:width: 100% /' 2_the_supply_and_demand_of_electricity.md
uv run jupyter book build --pdf
gsed -i 's/:width: 100% /:width: 64%/' 2_the_supply_and_demand_of_electricity.md

pdftoppm -f 1 -l 1 -png how_electricity_markets_work.pdf > img/pdf_page_1.png
pdftoppm -f 7 -l 7 -png how_electricity_markets_work.pdf > img/pdf_page_7.png
pdftoppm -f 10 -l 10 -png how_electricity_markets_work.pdf > img/pdf_page_10.png
