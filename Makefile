deps-install:
	source .venv/bin/activate && pip install -r requirements.txt

deps-upgrade:
	pip freeze --local | \
	grep -v '^\-e' | \
	cut -d = -f 1  | \
	xargs -n1 pip install -U

requirements:
	pip freeze -r requirements.txt > requirements.txt

serve:
	# FLASK_APP=server.py flask run
	flask run

run: deps-install
	source .env && make serve