gsed -i 's/:width: 64%/:width: 100% /' 2_the_supply_and_demand_of_electricity.md
jupyter book build --pdf
gsed -i 's/:width: 100% /:width: 64%/' 2_the_supply_and_demand_of_electricity.md

pdftoppm -f 1 -l 1 -png how_electricity_markets_work.pdf > img/pdf_page_1.png
pdftoppm -f 8 -l 8 -png how_electricity_markets_work.pdf > img/pdf_page_8.png
pdftoppm -f 9 -l 9 -png how_electricity_markets_work.pdf > img/pdf_page_9.png
