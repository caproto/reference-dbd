all: records.py

CAPROTO ?= $(HOME)/Repos/caproto

records.py: reference.dbd
	python generate.py reference.dbd records.py
	yapf -i records.py
	@echo "Done."

copy:
	cp -f records.py $(CAPROTO)/caproto/server/records.py

clean:
	rm -f records.py


.PHONY: all copy clean
