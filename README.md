Run with
``` bash
python3 -m venv .venv
source .venv/bin/activate
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata fixtures/Item.json
```