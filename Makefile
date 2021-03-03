all: records.py menus.py

CAPROTO ?= $(HOME)/Repos/caproto

records.py: reference.dbd
	python generate.py records reference.dbd records.py
	yapf -i records.py
	isort records.py
	@echo "Done."

menus.py: reference.dbd
	python generate.py menus reference.dbd menus.py
	# yapf -i menus.py
	isort menus.py
	@echo "Done."

copy: records.py menus.py
	cp -f records.py $(CAPROTO)/caproto/server/records.py
	cp -f menus.py $(CAPROTO)/caproto/server/menus.py

clean:
	rm -f records.py menus.py

.PHONY: all copy clean
