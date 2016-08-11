mkdir -p ./tmp/git/ ./tmp/json/
git clone git@github.com:wikimedia-france/wikiconvention-schedule-app.git ./tmp/git
git -C ./tmp/git config --local user.email $1
git -C ./tmp/git config --local user.name $2
git -C ./tmp/git config --local push.default simple