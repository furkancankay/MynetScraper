VENV := .venv
PYTHON3 := ${VENV}/bin/python3
PIP3 := ${VENV}/bin/pip3

.PHONY: env venv run clean

make_env:
	python3 -m pip install --upgrade pip
	python3 -m venv ${VENV}

install_requirements:
	PIP3 install --upgrade pip
	PIP3 install -r requirements.txt

run:
	${PYTHON3} ScrapMynet.py

clean:
	rm -rf /MynetHisseBilgileri/__pycache__
	rm -rf $(VENV)

make_requirements:
	PIP3 freeze > requirements.txt

venv:
	source ${VENV}/bin/activate

deneme: venv
	@which python3
