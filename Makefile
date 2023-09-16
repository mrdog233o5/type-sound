#PROGRAM NAME
PROG1 = sound_making.py
SPEC = .spec
DIR = $(shell pwd)
FILES = build *.spec

#COMPILER variable
CC = pyinstaller
CFLAGS = --clean --noconfirm --noconsole --uac-admin --hidden-import simpleaudio -F

#rules and recipes
all: clean build cleanspec

cleanspec:
	@rm -rf $(FILES)

build:
	$(CC) $(CFLAGS) $(PROG1)
	@mkdir dist/sound_making.app/Contents/Resources/sounds
	@mkdir dist/sounds
	@cp -r sounds/ dist/sound_making.app/Contents/Resources/sounds
	@cp -r sounds/ dist/sounds
	

run: build*
	@open ./dist/*

clean: 
	@rm -rf dist
	
