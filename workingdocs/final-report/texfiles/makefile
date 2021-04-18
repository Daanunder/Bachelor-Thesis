all: 
	abstract introduction research-question background method results discussion-conclusion appendix-dflow appendix-numerics

abstract:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl' --top-level-division='chapter' $(PWD)/abstract.md -o $(PWD)/abstract.tex

introduction:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/introduction.md -o $(PWD)/introduction.tex

research-question:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/research-question.md -o $(PWD)/research-question.tex

background:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/background.md -o $(PWD)/background.tex

method:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/method.md -o $(PWD)/method.tex

results:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/results.md -o $(PWD)/results.tex

discussion-conclusion:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/discussion-conclusion.md -o $(PWD)/discussion-conclusion.tex

appendix-dflow:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/appendix-dflow.md -o $(PWD)/appendix-dflow.tex

appendix-numerics:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/appendix-numerics.md -o $(PWD)/appendix-numerics.tex

appendix-modelling-results:
	pandoc --latex-engine='xelatex' --natbib --csl='apa-6th-edition.csl'  --top-level-division='chapter' $(PWD)/appendix-modelling-results.md -o $(PWD)/appendix-modelling-results.tex

move_to_latex:
	mv abstract.tex introduction.tex research-question.tex background.tex method.tex results.tex discussion-conclusion.tex appendix-dflow.tex appendix-numerics.tex appendix-modelling-results.tex appendix-python.tex -t ~/daank/civiel/BEP/workingdocs/latex/report_style/





