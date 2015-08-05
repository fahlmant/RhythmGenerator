all: output

output:
	python3 generator.py
	lilypond something.ly
	firefox something.pdf

server:
	python3 generator.py
	lilypond something.ly
	sudo cp something.pdf /var/www/music
clean:
	rm something.*
