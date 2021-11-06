.PHONY : all results clean help settings

COUNT=bin/countwords.py
DATA=$(wildcard data/*.txt)
SUMMARY=bin/book_summary.sh
RESULTS=$(patsubst data/%.txt,results/%.csv,$(DATA))
COLLATE=bin/collate.py
PLOT=bin/plotcounts.py

## all : regenerate all results.
all : results/collated.png

## results/collated.png : plot the collated results
results/collated.png : results/collated.csv bin/plotparams.yml
	python $(PLOT) $< --outfile $@ --plotparams $(word 2,$^)
 
## results/collated.csv : collate all results
results/collated.csv : $(RESULTS) $(COLLATE)
	mkdir -p results
	python $(COLLATE) $(RESULTS) > $@ 

## results : regenerate result for all books.
results : $(RESULTS)

## results/%.csv : regenerate result for any book.
results/%.csv : data/%.txt $(COUNT)
	@bash $(SUMMARY) $< Title
	@bash $(SUMMARY) $< Author
	python $(COUNT) $< > $@

## clean : remove all generated files.
clean :
	rm $(RESULTS) results/collated.csv results/collated.png

## settings : show variables' values.
settings :
	@echo COUNT: $(COUNT)
	@echo DATA: $(DATA)
	@echo SUMMARY: $(SUMMARY)
	@echo RESULTS: $(RESULTS)
	@echo COLLATE: $(COLLATE)
	@echo PLOT: $(PLOT)

## help : show this message.
help :
	@grep '^##' ./Makefile
	
