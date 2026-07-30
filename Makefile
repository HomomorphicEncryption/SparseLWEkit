all:
	python3 src/estimate_security.py
	awk 1 src/markdown/todo.md > README.md
	awk 1 src/markdown/part1.md >> README.md
	python3 src/gen_attack_table.py >> README.md
	awk 1 src/markdown/part2.md >> README.md
	python3 src/gen_parameter_table.py >> README.md
	awk 1 src/markdown/part3.md >> README.md
	python3 src/gen_security_estimation_table.py >> README.md
	awk 1 src/markdown/part4.md >> README.md

readme:
	awk 1 src/markdown/todo.md > README.md
	awk 1 src/markdown/part1.md >> README.md
	python3 src/gen_attack_table.py >> README.md
	awk 1 src/markdown/part2.md >> README.md
	python3 src/gen_parameter_table.py >> README.md
	awk 1 src/markdown/part3.md >> README.md
	python3 src/gen_security_estimation_table.py >> README.md
	awk 1 src/markdown/part4.md >> README.md
