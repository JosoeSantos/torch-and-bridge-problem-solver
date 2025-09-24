# Makefile for building apresentacao1_principal.tex with references

TEX=pdflatex
BIBTEX=bibtex
MAIN=report_main
BUILDDIR=build

all: $(BUILDDIR)/$(MAIN).pdf

$(BUILDDIR)/$(MAIN).pdf: $(MAIN).tex | $(BUILDDIR)
	$(TEX) -output-directory=$(BUILDDIR) $(MAIN).tex
	$(BIBTEX) $(BUILDDIR)/$(MAIN)
	$(TEX) -output-directory=$(BUILDDIR) $(MAIN).tex
	$(TEX) -output-directory=$(BUILDDIR) $(MAIN).tex

$(BUILDDIR):
	mkdir -p $(BUILDDIR)

clean:
	rm -f $(BUILDDIR)/*.aux $(BUILDDIR)/*.bbl $(BUILDDIR)/*.blg $(BUILDDIR)/*.log $(BUILDDIR)/*.nav $(BUILDDIR)/*.out $(BUILDDIR)/*.snm $(BUILDDIR)/*.toc $(BUILDDIR)/*.vrb $(BUILDDIR)/*.brf $(BUILDDIR)/*.lof $(BUILDDIR)/*.lot $(BUILDDIR)/*.fls $(BUILDDIR)/*.fdb_latexmk $(BUILDDIR)/*.pdf

.PHONY: all clean
.PRECIOUS: $(BUILDDIR)/$(MAIN).pdf