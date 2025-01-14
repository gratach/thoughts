# Dunin agent locator

A dunin agent locator is a string, that is used to identify [dunin agents](../../code/architecture/dunin-agent.md). It is the first part of a [dunin ID](dunin-id.md) up to the first two slashes of the dunin IDs triple slash.

There are two types of dunin agent locators:

* URL dunin agent locators
* Cryptographic dunin agent locators

The dunin agent locator is a uri that must not contain any "?", "=", "&" or "\#" characters and ends with a double backslash. The beginning of the dunin agent locator including the [uri scheme](https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml) is eather `http://`for URL dunin IDs or `crypt://`for cryptographic dunin IDs

Example for a URL dunin ID:

`http://my.domain.com/dunin/agent/locator//`
