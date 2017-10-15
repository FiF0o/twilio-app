deps-install:
	echo 'placeholder to install pkgs'

deps-upgrade:
	pip freeze --local | \
	grep -v '^\-e' | \
	cut -d = -f 1  | \
	xargs -n1 pip install -U

build: deps-install
	echo 'placeholder build task!'
run:
	python main.py