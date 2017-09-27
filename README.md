# wikiconvention-schedule-parser

## Pré-requis

```
apt install python3 python3-pip git
pip3 install pyquery
```

## Installation

```
cd /var/www/html
git clone https://github.com/wikimedia-france/wikiconvention-schedule-app.git
git clone https://github.com/wikimedia-france/wikiconvention-schedule-parser.git
```

```
cd wikiconvention-schedule-app
git checkout YYYY
git config --local user.email tech@wikimedia.fr
git config --local user.name wikimedia-france
git config --local push.default simple
```

## Configuration

```
cd ../wikiconvention-schedule-parser
cat ./sync.sh
```

**Remplacer dans le fichier `sync.sh` les variables avec les valeurs qui vont bien**

* Lieu de l'application :

```
APP="/var/www/html/wikiconvention-schedule-app"
```

* Page META a executer (Remplacer YYYY)

```
META="https://meta.wikimedia.org/w/api.php?action=parse&format=json&text=%7B%7B%3AWikiConvention+francophone%2FYYYY%2FProgramme%7Cshow%3DSimple%7D%7D&prop=text"
```

*Example : [Bac à sable API](https://meta.wikimedia.org/wiki/Special:ApiSandbox#action=parse&format=json&text=%7B%7B%3AWikiConvention%20francophone%2F2017%2FProgramme%7Cshow%3DSimple%7D%7D&prop=text)*

## Synchronization

```
crontab -e
```

Ajouter la ligne suivante :

```
* * * * * /var/www/html/wikiconvention-schedule-parser/sync.sh >> /var/log/parser.log
```

