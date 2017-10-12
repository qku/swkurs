# hello.mk
master.pdf : master.tex figure-1.png figure-2.png
	pdflatex $<
figure-%.png : summary-%.dat
	python myplot.py $^ $@
summary-%.dat : data-%-*.dat
	python myanalysis.py $@ $^
