# Woma Programming Language Demo/Template

Here is everything that is needed to build a small CPython extension in the Woma Programming Language.
The only requirement is to install the compiler Aspidites.

You can build it with the included Makefile by running:
```shell
make demo
```
Or you can build manually as follows:
```shell
Aspidites src/woma_demo.wom -o src/woma_demo.pyx -c
```
To run the demo use:
```shell
python -m src.demo
```

