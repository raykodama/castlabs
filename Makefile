# Build the Docker image
build:
	docker build -t jwt_utility .

# Run the JWT utility inside a Docker container
run:
	docker run --rm -v "$(PWD)/secret.txt:/app/secret.txt" jwt_utility

