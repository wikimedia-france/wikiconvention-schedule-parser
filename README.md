# wikiconvention-schedule-parser

cd /var/www/html
git clone https://github.com/wikimedia-france/wikiconvention-schedule-app.git
git clone https://github.com/wikimedia-france/wikiconvention-schedule-parser.git

cd wikiconvention-schedule-app
git checkout YYYY
git config --local user.email tech@wikimedia.fr
git config --local user.name wikimedia-france
git config --local push.default simple

cd ../wikiconvention-schedule-parser
cat ./sync.sh

Remplacer dans le fichier les variables avec les valeurs qui vont bien
Lieu de l'application :

APP="/var/www/html/wikiconvention-schedule-app"

Page META a executer (Remplacer YYYY)

META="https://meta.wikimedia.org/w/api.php?action=parse&format=json&text=%7B%7B%3AWikiConvention+francophone%2FYYYY%2FProgramme%7Cshow%3DSimple%7D%7D&prop=text"

crontab -e

Ajouter la ligne suivante

* * * * * /var/www/html/wikiconvention-schedule-parser/sync.sh > /var/log/parser.log

