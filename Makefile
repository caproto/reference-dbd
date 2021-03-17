all: base.py menus.py

CAPROTO ?= $(HOME)/Repos/caproto

base.py: reference.dbd
	python generate.py records reference.dbd base.py
	black -l 80 base.py
	@echo "Done."

menus.py: reference.dbd
	python generate.py menus reference.dbd menus.py
	# black menus.py
	@echo "Done."

copy: base.py menus.py
	cp -f base.py $(CAPROTO)/caproto/server/records/base.py
	cp -f menus.py $(CAPROTO)/caproto/server/menus.py

clean:
	rm -f base.py menus.py

.PHONY: all copy clean
