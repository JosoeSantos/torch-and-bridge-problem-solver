
all:
	for dir in $(shell cat projects.txt); do \
		make -C $$dir; \
	done

clean:
	for dir in $(shell cat projects.txt); do \
		make -C $$dir clean; \
	done

sol:
	python scripts/solution_runner.py

.PHONY: all
