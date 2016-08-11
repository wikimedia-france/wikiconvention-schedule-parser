git -C ./tmp/git/ pull
d=`date`
python3 ./scheduleSync.py > ./tmp/json/sync.json
head -n 1 ./tmp/json/sync.json > ./tmp/git/sessions.json
head -n 2 ./tmp/json/sync.json > ./tmp/git/tags.json
head -n 3 ./tmp/json/sync.json > ./tmp/git/themes.json
CHANGED=$(git -C ./tmp/git/ diff-index --name-only HEAD --)
if [ ! -n "$CHANGED" ]; then
    sed -i "2s/.*/# revision - $d/" ./tmp/git/schedule.appcache
    git -C ./tmp/git/ add sessions.json tags.json themes.json schedule.appcache
    git -C ./tmp/git/ commit -m "Synchronisation $d"
    git -C ./tmp/git/ push
    echo "SYNCHED"
else
    echo "NOCHANGE"
fi
