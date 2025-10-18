# What characters to use in a dunin id

What are the characters that should be used in a [dunin-id](../../../topics/data/adresses/dunin-id.md) in order to make it a valid url and keep it nice to understand and to read?

## Brainstorming

Dunin ID should be a valid url [that allows this characters](https://stackoverflow.com/questions/4669692/valid-characters-for-directory-part-of-a-url-for-short-links).
`?`, `&`and `=`can be reserved for queries
What character to use to separate the [dunin-agent-locator](../../../topics/data/adresses/dunin-agent-locator.md) from the rest of the dunin ID?
	Originally Idea: Three slashes `///` but:
		Dunin ID becomes long because three characters
		Hard to read when [stacked-dunin-agent-locator](../../../topics/data/adresses/stacked-dunin-agent-locator.md) 
	An other Idea: `~` but:
		Special meaning in some file systems
		Some user agents encode it
	Best solution: `_`
		For separating words is still `-`left
