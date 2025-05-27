all:
	cat src/part1.md > README.md
	python3 src/gen_attack_table.py >> README.md
	cat src/part2.md >> README.md
	python3 src/gen_parameter_table.py >> README.md
	cat src/part3.md >> README.md
