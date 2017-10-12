diranalysis.pdf : diranalysis.tex liste.txt
	pdflatex $^
liste.txt :
	ls *.py > liste.txt
clean :
	rm diranalysis.aux diranalysis.log liste.txt liste.txt.aux
