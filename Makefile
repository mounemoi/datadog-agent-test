PYTHON_PATH=/opt/datadog-agent/embedded/bin/

.PHONY: default test setup

default:
	# do nothing

setup-test:
	${PYTHON_PATH}/pip install -r requirements-test.txt

test:
	PYTHONPATH=check.d/:tests/dummy/ \
	    ${PYTHON_PATH}/python -m unittest -v tests.test_sample_check

