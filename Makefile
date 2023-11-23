IMAGE_NAME="joram87/route66"

build:
	docker build -t $(IMAGE_NAME) .

run: build
	docker run -v /var/run/docker.sock:/var/run/docker.sock:ro -v ./route66:/app -p 80:80 $(IMAGE_NAME)

push: build
	docker push $(IMAGE_NAME)
bash:
	docker run -v /var/run/docker.sock:/var/run/docker.sock:ro -p 80:80 -it $(IMAGE_NAME) bash
