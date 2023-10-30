# installization

 1. download type-sound files, which is all in this folder: https://github.com/mrdog233o5/type-sound/archive/refs/heads/main.zip
 2. unzip the zip file and put the folder in where you want to install type-sound
 3. open terminal (a macos application), all the steps after will be done in this app using command line
 4. go to the directory of typing-sound folder using `cd <path of the folder>`
 5. setup all the files of type-sound, you can use the script i made to automatically setup: `bash setup.sh`
 6. now all of the basic files are installed, to be able to use type-sound, you MUST read #config page to be able to use type-sound (this step doesnt have to be done with terminal)
# config
type-sound does not contain any sounds in it, so to use type-sound, you must give type-sound a sound to play. The default setting can also be not suitable for you, so you can customize type-sound by configuring it.

### adding a sound
1. find any sound you want, ANY, even meme sounds.
2. convert the sound you got to .WAV format using any tools, i suggest https://cloudconvert.com/ because it is free, but you can use any tools you want, as long as the output sound is in .WAV format.
3. rename the sound files EXACTLY like this structure:
	<pack_name>									#any name you like for the pack
	 ├── press.wav							#sound played when pressed a key
	 ├── release.wav 						#sound played when released a key
	 ├── mousePress.wav 				#sound played when pressed mouse
	 └── mouseRelease.wav				#sound played when released mouse
4. put the whole folder directly into `~/.config/type-sound/sounds` aka `/Users/<your user name>/.config/type-sound/sound/sounds` 
this is a hidden folder as it starts with a dot, so you have to press `command+shift+period(.)` to enable displaying hidden folders.
5. the sound pack is added correctly if you followed the steps above correctly. To tell type-sound to use that sound pack, open `~/.config/type-sound/type-sound.json` aka `/Users/<your user name>/.config/type-sound/type-sound.json` with a text editor.
6. when you open it, it should look like something like this:
```
{
    "pack":<soundpack that you are using>,
}
```
remember to save and reopen type-sound when you made any changes
# execute

open `<the location of the type-sound folder>/dist/type-sound.app` if u did all the steps above correctly, you should be able to hear sound when ur typing after a few seconds
