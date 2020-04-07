ps -A | grep Xvfb | awk '{print $1}' | xargs kill -9 $1 > /dev/null
ps -A | grep chromium | awk '{print $1}' | xargs kill -9 $1 > /dev/null

/usr/bin/python3 /home/marco/owncloud/Projekte/switchCrawler/main.py > /var/www/mk/html/switchCrawler.html

scp -i /home/marco/switchCrawler_id_rsa -P 42420 /var/www/mk/html/switchCrawler.html marco@192.168.178.50:/var/www/mk/html/switchCrawler.html

echo `date` finished >> /home/marco/owncloud/Projekte/switchCrawler/cron.log
