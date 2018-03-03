# make figures
.PHONY: all
all: figs PDF
.PHONY: figs
figs : SimpleHarmonicOscillator.py
	python SimpleHarmonicOscillator.py 200 0 5 .5 .1 
.PHONY: PDF
PDF: HarmonicOscillator.pdf
HarmonicOscillator.pdf: HarmonicOscillator.tex
	pdflatex HarmonicOscillator.tex
.PHONY: clean
clean: 
	rm -f HarmonicOscilalltor.pdf