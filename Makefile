PORT=8000
SETTINGS=config.settings.local

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

install_local_deps:
	pip install -r requirements/local.txt

install_heroku_deps:
	pip install -r requirements/heroku.txt

install_production_deps:
	pip install -r requirements/production.txt

run_server:
	./manage.py runserver 127.0.0.1:$(PORT) --settings=$(SETTINGS)

shell:
	./manage.py shell --settings=$(SETTINGS)

migrate:
	./manage.py makemigrations --settings=$(SETTINGS)
	./manage.py migrate --settings=$(SETTINGS)

new_app:
	mkdir apps/$(NAME)
	django-admin startapp $(NAME) apps/$(NAME)

coverage:
	coverage run manage.py test --settings=$(SETTINGS)
	coverage html
