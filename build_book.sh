gsed -i 's/:width: 64%/:width: 100% /' 2_the_supply_and_demand_of_electricity.md
jupyter book build --pdf
gsed -i 's/:width: 100% /:width: 64%/' 2_the_supply_and_demand_of_electricity.md
