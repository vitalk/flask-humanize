clean:
	@rm -rf build dist *.egg-info
	@find . -name '*.py?' -delete


.PHONY: clean
