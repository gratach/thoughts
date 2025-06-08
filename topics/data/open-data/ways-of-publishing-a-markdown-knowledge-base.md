# Ways of publishing a markdown knowledge base

[This-knowledge-base](../knowledge/this-knowledge-base.md) exists as a obsidian vault on a local machine. It is an interesting question what is the best way to make it (or similar knowledge bases) [available to the public](../../code/technologies/how-to-make-data-public.md).

1. **Host it on Github**
	* Like [this](https://github.com/gratach/thoughts) page
	* pros
		* integrated markdown viewer
		* free
		* ...
	* cons
		* Dependent on provider
		* Monopol
		* People only interested in vault contend get distracted by other functionality of github
2. **Build Static web page and host it**
	* **Using [Sphinx](https://www.sphinx-doc.org/en/master/index.html)**
		* Like [this](https://thoughts.debablo.de/) page
		* pros
			* standalone
			* configurable
			* open source (BSD)
		* cons
			* complicated to configure
			* No easy way to display file hirarchy
				* Could not configure table of content tree depth of sidebar in a nice way
				* Verry unintuitive to navigate
			* Not modern
			* Errors while building
	* **Using Quarz**
		* Like [this](https://quartz.jzhao.xyz/) page
		* pros
			* Modern look
			* Backlinks
			* Graph view
			* File explorer
			* open source (MIT)
		* cons
			* Integrates third party web content
				* gstatic.com
				* jsdeliver.net
				* plausible.io
			* No simple way to create static web page using command line
			* Complicated
			* GitHub Needed? Not sure
	* [Jekyll](https://jekyllrb.com/)
	* [Pandoc](https://pandoc.org/)
	
			