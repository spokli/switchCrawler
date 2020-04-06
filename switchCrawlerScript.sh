ps -A | grep Xvfb | awk '{print $1}' | xargs kill -9 $1 > /dev/null
ps -A | grep chromium | awk '{print $1}' | xargs kill -9 $1 > /dev/null

python3 ./main.py > /var/www/mk/html/switchCrawler.html
