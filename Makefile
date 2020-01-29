CURRENT_DIR = $(PWD)

VENV_DIR = $(CURRENT_DIR)/venv
OPS_DIR = $(CURRENT_DIR)/ops
LOG_DIR = $(CURRENT_DIR)/log

PIP_VENV = $(VENV_DIR)/bin/pip

CHROME_DRIVER_LAST_VERSION = `curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`

setup:

	# Setup virtual environment
	if [ ! -d $(VENV_DIR) ] ; then\
		virtualenv --python=python3 $(VENV_DIR) ;\
	fi

	# Install project requirements
	$(PIP_VENV) install -r requirements.txt

 	# Get last stable version of chromedirver
	wget -P $(OPS_DIR) https://chromedriver.storage.googleapis.com/$(CHROME_DRIVER_LAST_VERSION)/chromedriver_linux64.zip

	# Remove older chromedriver if it exists
	if [ -d $(OPS_DIR)/chromedriver ] ; then\
		rm $(OPS_DIR)/chromedriver ;\
	fi

	# Unzip chromedriver
	unzip -o $(OPS_DIR)/chromedriver_linux64.zip  -d $(OPS_DIR)
	# Remove downloaded zip
	rm $(OPS_DIR)/chromedriver_linux64.zip

run:
	$(VENV_DIR)/bin/pytest