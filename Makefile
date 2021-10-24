
clean:
	-cd src/ && $(MAKE) uninstall

demo: src/woma_demo.so

src/woma_demo.so:
	Aspidites src/woma_demo.wom -o src/woma_demo.pyx -c