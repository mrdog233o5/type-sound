#PROGRAM NAME
PROG1 = main.py
SPEC = .spec
DIR = $(shell pwd)
FILES = build *.spec

#COMPILER variable
CC = pyinstaller
CFLAGS = --clean --noconfirm --noconsole --uac-admin --hidden-import simpleaudio --name type-sound -F

#rules and recipes
all: clean build cleanspec

cleanspec:
	@rm -rf $(FILES)

build:
	$(CC) $(CFLAGS) $(PROG1)

run: build*
	@open ./dist/*

clean: 
	@rm -rf dist
	
