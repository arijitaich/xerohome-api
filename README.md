Steps followed & logged:

1. git clone https://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@github.com/arijitaich/xerohome-api.git
2. sudo apt install python3.8
3. sudo apt install python3-pip
4. sudo apt install software-properties-common
5. sudo add-apt-repository ppa:deadsnakes/ppa
6. sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
7. sudo apt install python3-pip
8. sudo apt install python3-flask 
9. export FLASK_APP="app.main:create_app"
10. export FLASK_ENV=development
11. sudo apt install gunicorn
12. gunicorn -w 4 --reload -b :8000 "app.main:create_app(testing=False)"