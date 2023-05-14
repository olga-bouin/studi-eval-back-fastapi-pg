# studi-eval-back-fastapi-pg
## Installation
sudo apt install python3.8-venv
python3 -m venv env
source ./env/bin/activate
python -m pip install --upgrade pip
pip install -e ."[dev,doc,test]"
pip install uvicorn
pip install fastapi
pip install python-dotenv

