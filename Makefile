up:
	docker compose -f docker-compose-ci.yaml up -d

rebuild:
	docker compose -f docker-compose-ci.yaml up --build -d

down:
	docker compose -f docker-compose-ci.yaml down --remove-orphans
