all:
	cat src/markdown/part1.md > README.md
	python3 src/gen_attack_table.py >> README.md
	cat src/markdown/part2.md >> README.md
	python3 src/gen_parameter_table.py >> README.md
	cat src/markdown/part3.md >> README.md
