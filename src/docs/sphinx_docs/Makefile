# Initially generated with sphinx-quickstart

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
LINKCHECKDIR  = _build/linkcheck
GENDIR        = $(SOURCEDIR)/generated

# First so that "make" without arguments is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile checklinks

checklinks:
	@$(SPHINXBUILD) -b linkcheck $(SPHINXOPTS) $(LINKCHECKDIR)
	@echo
	@echo "Check finished. Report is in $(LINKCHECKDIR)."

rebuild:
	@$(SPHINXBUILD) -E "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

clear-generated:
	@echo "Clearing generated files"
	@$(RM) -rf $(GENDIR)

clean: clear-generated
# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O) -j auto
