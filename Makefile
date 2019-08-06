.PHONY: test release clean version

export APP_VERSION ?= $(shell git rev-parse --short HEAD)

version:
	@ echo '{"Version": "$(APP_VERSION)"}'

test:
	docker-compose build --pull release
	docker-compose build
	docker-compose run test

release:
	docker-compose up --abort-on-container-exit migrate
	docker-compose run app python3 manage.py collectstatic --no-input
	docker-compose up --abort-on-container-exit acceptance
	@ echo APP running at http://$$(docker-compose port app 9001 | sed s/0.0.0.0/localhost/g)
	@ echo API running at http://$$(docker-compose port api 8080 | sed s/0.0.0.0/localhost/g)

clean:
	docker-compose down -v
	docker images -q -f dangling=true -f label=application=todotask1 | xargs -I ARGS docker rmi -f --no-prune ARGS