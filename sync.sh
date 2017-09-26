CURRDIR="$(readlink -f $(pwd))"
ROOTDIR="$(readlink -f $(dirname $0))"


APP="/var/www/html/wikiconvention-schedule-app"
META="https://meta.wikimedia.org/w/api.php?action=parse&format=json&text=%7B%7B%3AWikiConvention+francophone%2F2017%2FProgramme%7Cshow%3DSimple%7D%7D&prop=text"

TMP="${ROOTDIR}/tmp/json"

mkdir -p ${TMP}

git -C ${APP} pull
d=`date`

python3 ${CURRDIR}/scheduleSync.py ${META} > ${TMP}/sync.json
sed -n '1p' < ${TMP}/sync.json > ${APP}/sessions.json
sed -n '2p' < ${TMP}/sync.json > ${APP}/tags.json
sed -n '3p' < ${TMP}/sync.json > ${APP}/themes.json

CHANGED=$(git -C ${APP} diff --name-only HEAD --)
if [ -n "$CHANGED" ]; then
    sed -i "2s/.*/# revision - $d/" ${APP}/schedule.appcache
    git -C ${APP} add sessions.json tags.json themes.json schedule.appcache
    git -C ${APP} commit -m "Synchronisation $d"
    #git -C ${APP} push
    echo "SYNCHED"
else
    echo "NOCHANGE"
fi
