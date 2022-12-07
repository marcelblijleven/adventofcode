.PHONY: all install clean_project

all: clean_project install

install:
	pip install -r requirements_dev.txt
	cp pre-commit.template .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

clean_project:
	find . \( -type f -name '*.pyc' -or -type d -name '__pycache__' \) -delete
	find . \( -type d -name '.eggs' -or -type d -name '*.egg-info' -or -type d -name '.pytest_cache' \) | xargs rm -rf
