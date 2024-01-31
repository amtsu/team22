curl -s https://finance.rambler.ru/currencies/ -o cur.html > /dev/null
awk '/<div class="finance-exchange-rate__money">\$<\/div>/,/<\/div>/{getline;getline;printf "usd/rur = %f \n", $0}' cur.html | head -n1
awk '/<div class="finance-exchange-rate__money">€<\/div>/,/<\/div>/{getline;getline;printf "eur/rur = %f \n", $0}' cur.html | head -n1
