# Stack Shared Library Example

A minimal example to build an haskell-based shared library
that can be used in C projects.

## Build

```sh
stack build
```

## Test

```sh
$ python3 test.py
Hello Haskell!
```

## Credits

- [Calling Haskell Shared Libraries from C (Linux)](https://www.vex.net/~trebla/haskell/so.xhtml)
- [Cabal foreign libraries](http://qnikst.github.io/posts/2018-05-02-cabal-foreign-library.html)
- [Stack Integration Tests](https://github.com/commercialhaskell/stack/blob/master/test/integration/tests/internal-libraries/files/files.cabal)
