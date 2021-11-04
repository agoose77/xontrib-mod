# xontrib-mod
Xonsh pushes the user towards Pythonic contructs over shell pipelines of general purpose tools (think `xargs` and friends), but these tools are generally less verbose to use. 
Given that the shell rewards ease-of-writing over verbosity, this can make writing shell script in Python a less enjoyable experience for shell programmers.

Enter `mod`. `mod` is a simple xontrib that defines a `mod` builtin that attempts to resolve modules and their attributes:
```pycon
>>> xontrib load mod
>>> mod.json.loads($(echo "[1, 2, 3]"))
[1, 2, 3]
```
