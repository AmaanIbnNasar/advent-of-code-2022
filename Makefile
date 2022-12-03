SHELL:=/bin/bash

day-%:
	mkdir aoc/day_$*
	pushd aoc/day_$* && touch __init__.py && touch day_$*.py && touch test_day_$*.py && touch test.txt && touch input.txt && popd