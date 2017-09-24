PORT = 8000

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

install_local_deps:
	pip install -r requirements/local.txt

install_heroku_deps:
	pip install -r requirements/heroku.txt

install_production_deps:
	pip install -r requirements/production.txt

run_server:
	./manage.py runserver 127.0.0.1:$(PORT)

shell:
	./manage.py shell

migrate:
	./manage.py makemigrations
	./manage.py migrate

new_app:
	mkdir apps/$(NAME)
	django-admin startapp $(NAME) apps/$(NAME)
