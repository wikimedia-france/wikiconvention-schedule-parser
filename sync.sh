git -C ./tmp/git/ pull
d=`date`
python3 ./scheduleSync.py > ./tmp/json/sync.json
sed -n '1p' < ./tmp/json/sync.json > ./tmp/git/sessions.json
sed -n '2p' < ./tmp/json/sync.json > ./tmp/git/tags.json
sed -n '3p' < ./tmp/json/sync.json > ./tmp/git/themes.json
CHANGED=$(git -C ./tmp/git/ diff --name-only HEAD --)
if [ -n "$CHANGED" ]; then
    sed -i "2s/.*/# revision - $d/" ./tmp/git/schedule.appcache
    git -C ./tmp/git/ add sessions.json tags.json themes.json schedule.appcache
    git -C ./tmp/git/ commit -m "Synchronisation $d"
    git -C ./tmp/git/ push
    echo "SYNCHED"
else
    echo "NOCHANGE"
fi
