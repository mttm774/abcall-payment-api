activate:
	if [ -d "venv" ]; then \
        echo "Python 🐍 environment was activated"; \
    else \
        echo "The folder environment doesn't exist"; \
		python -m venv venv; \
        echo "The environment folder was created and the python 🐍 environment was activated"; \
    fi
	. ./venv/bin/activate

install:
	pip3 install -r requirements.txt

run:
	@if [ -z "$(strip $(PORT))" ]; then \
		flask run; \
	else \
		flask run -p $(PORT); \
	fi

run-docker:
ifeq ($(strip $(PORT)),)
	flask run -h 0.0.0.0
else
	flask run -p $(PORT) -h 0.0.0.0
endif

run-worker:
	celery -A flaskr.tasks.task.celery worker --loglevel=info --detach

run-beat:
	celery -A flaskr.tasks.task.celery beat --loglevel=info --detach

docker-gunicorn:
	  gunicorn -w 4 --bind 127.0.0.1:$(PORT) wsgi:app

docker-up:
	docker compose up --build

docker-down:
	docker compose down

docker-dev-up:
	docker compose -f=docker-compose.develop.yml up --build

docker-dev-down:
	docker compose -f=docker-compose.develop.yml down

create-database:
	docker exec payment-local-db psql -U develop -d payment-db -f /docker-entrypoint-initdb.d/init.sql

generate-data:
	docker exec payment-local-db psql -U develop -d payment-db -f /docker-entrypoint-initdb.d/invoiceFakeData.sql

generate-customer-data:
	docker exec payment-local-db psql -U develop -d payment-db -f /docker-entrypoint-initdb.d/customerFakeData.sql

kubernetes-up:
	kubectl apply -f kubernetes/k8s-configMap.yaml
	kubectl apply -f kubernetes/k8s-secrets.yaml
	kubectl apply -f kubernetes/k8s-deployment.yaml
	kubectl apply -f kubernetes/k8s-ingress.yaml

kubernetes-dev-up:
	make kubernetes-dev-up
	minikube tunnel

kubernetes-dev-down:
	kubectl delete configMap/payment-configmap
	kubectl delete secrets/payment-secrets
	kubectl delete deploy/abcall-payment-api
	kubectl delete ingress/abcall-payment-ingress


