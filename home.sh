#!/bin/bash
for letter in {a..z} ; do
	echo $letter : $(ls /home/$letter | wc -l)
done
