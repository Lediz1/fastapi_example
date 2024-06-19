integration-tests:
	docker-compose -f docker-compose-tests.yml stop
	docker-compose -f docker-compose-tests.yml build
	docker-compose -f docker-compose-tests.yml up 

run:
	uvicorn user-api.main:app --reload

run_docker_user_app:
	docker-compose -f docker-compose.yml stop
	docker-compose -f docker-compose.yml build
	docker-compose -f docker-compose.yml up	

services:
	docker-compose -f docker-compose-services.yml stop
	docker-compose -f docker-compose-services.yml build
	docker-compose -f docker-compose-services.yml up

