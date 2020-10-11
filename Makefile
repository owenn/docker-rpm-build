.DEFAULT_GOAL := all

build:

	cd $(CURDIR)/rpm-builder && \
		docker build -t rpm-builder .

	cd $(CURDIR)/make && \
		docker build -t rpm-builder-make:latest . 

# the run actions  are used for testing. 
run-rpm-builder:
	cd $(CURDIR) && \
	docker run -ti -v`pwd`:/mnt rpm-builder:latest /bin/bash

run-make:
	mkdir -p /tmp/data /tmp/output  && \
	chmod 777 /tmp/data /tmp/output && \
	docker run -v /tmp/data:/data -v /tmp/output:/output -ti rpm-builder-make  /bin/bash 

all: build


