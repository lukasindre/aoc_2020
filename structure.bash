#!/bin/bash

n=2
MAX=25
while [ "$n" -le "$MAX" ]
do
	mkdir "$n" && touch "$n/input" && touch "$n/puzzle_01.py" && touch "$n/puzzle_02.py"
	n=`expr "$n" + 1`
done
