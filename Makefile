vagrant:
	vagrant up --provision
	vagrant ssh

setupfedora:
	sudo yum install python-pip
	sudo pip install virtualenv
	sudo pip install virtualenvwrapper
	export WORKON_HOME=~/python-virtual-envs
	mkdir -p $WORKON_HOME

setupmac:
	sudo easy_install pip
	sudo pip install virtualenv
	sudo pip install virtualenvwrapper
	export WORKON_HOME=~/python-virtual-envs
	mkdir -p $WORKON_HOME

prep:
	pip install -r requirements.txt
	python setup.py install

test:
	autopep8 -v -i -r -a ./features/steps/*.py *.py ./tests/*.py
	behave features/*.feature
	py.test --cov=fibonacci ./tests/*.py

.PHONY: all
