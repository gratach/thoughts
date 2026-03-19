# Jest test

Javascript code can be testet with jest.

## Debugging in vscode

In vscode jest orta can be used to run tests.

### TestPathPattern error while debugging in vscode

When debugging jest tests in vscode the following error can appear:

```
testPathPattern:

  Option "testPathPattern" was replaced by "--testPathPatterns". "--testPathPatterns" is only available as a command-line option.
  
  Please update your configuration.

  CLI Options Documentation:
  https://jestjs.io/docs/cli
```

It can be fixed by going to extensions > jest > gear symbol > settings and enable the checkbox at Use Jest30.