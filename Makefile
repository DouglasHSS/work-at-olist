PORT=8000
SETTINGS=config.settings.local

install_local_deps:
	pip install -r requirements/local.txt

run_server:
	./manage.py runserver 127.0.0.1:$(PORT) --settings=$(SETTINGS)

shell:
	./manage.py shell --settings=$(SETTINGS)

migrate:
	./manage.py makemigrations --settings=$(SETTINGS)
	./manage.py migrate --settings=$(SETTINGS)

import_categories:
	./manage.py import_categories $(CHANNEL_NAME) $(CSV_PATH) --settings=$(SETTINGS)

new_app:
	mkdir apps/$(NAME)
	django-admin startapp $(NAME) apps/$(NAME)

coverage:
	coverage run manage.py test --settings=$(SETTINGS)
	coverage html
