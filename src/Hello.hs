module Hello where

foreign export ccall "hello" c_hello :: IO ()

c_hello = putStrLn "Hello Haskell!"
