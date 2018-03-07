sudo apt-get update
sudo apt-get dist-upgrade

sudo apt-get install python3-dev python3-venv git libffi-dev libssl-dev

python3 -m venv venv/
source venv/bin/activate
pip install -U pip
pip install twisted[tls,http2]
pip install django
pip install channels
pip install asgi_redis
pip install websocket-client
pip install pigpio

deactivate
