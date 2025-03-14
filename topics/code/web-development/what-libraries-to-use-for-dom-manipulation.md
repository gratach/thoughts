# What libraries to use for DOM manipulation

#### Plain Javascript

This is a quite verbose method to create dom elements with `document.createElement' and 'elem.appendChild'
#### React

[React](https://react.dev/) is a library that allows one to use the [jsx](https://de.wikipedia.org/wiki/JSX_(JavaScript)) syntax to create HTML elements within JavaScript. However it forces one to store the data in react-hooks that can only be accessed by the render function and have some strange and complicated behavior especially when HTML elements change their position within the DOM.

[Example Project](https://github.com/gratach/test-webpack/tree/2f4fdb0ee03d812b66a514c4d7aa4c35ae9b1c49/simple_react_project)

#### Lighterhtml

In [lighterhtml](https://github.com/WebReflection/lighterhtml) the syntax `d = html.node"<p>Some text ${innerElement} </p>` can be used

[Example Project](https://github.com/gratach/test-webpack/tree/4174eb1a7e3f7882b467c244467318377524d15c/generate_html_with_javascript/lighterhtml_test)