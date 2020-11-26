#!bin/bash
python3 -m pip install --user --upgrade pip
if command -v apt-get &> /dev/null; then
	sudo apt-get install python3-venv
	sudo apt install python3-tk
fi
python3 -m venv virtual_env
source virtual_env/bin/activate
if [[ "$VIRTUAL_ENV" != "" ]]; then
	echo "env created !"
	pip install -r libs_required.txt
else
	echo "env is not working!"
fi
