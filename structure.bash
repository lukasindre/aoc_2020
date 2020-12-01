#!/bin/bash

n=1
MAX=25
while [ "$n" -le "$MAX" ]
do
	if [[ $n -lt 10 ]]
	then
		mkdir "0${n}" && touch "0${n}/input" && touch "0${n}/puzzle_01.py" && touch "0${n}/puzzle_02.py"
	else
		mkdir "$n" && touch "$n/input" && touch "$n/puzzle_01.py" && touch "$n/puzzle_02.py"
	fi

	n=`expr "$n" + 1`
done
