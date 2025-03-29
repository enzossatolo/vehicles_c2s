.PHONY: all build app

all: build app

build:
	@echo "Building Docker image..."
	docker build -t vehicles-c2s .

app:
	@echo "Running the app container in interactive mode..."
	docker run -it --rm vehicles-c2s bash
