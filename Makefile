DATADOG_INSTALL_PATH=/opt/datadog-agent/

.PHONY: default test setup

default:
	# do nothing

setup:
	${DATADOG_INSTALL_PATH}/embedded/bin/pip install mock

test:
	PYTHONPATH=${DATADOG_INSTALL_PATH}/agent/:check.d/ \
	    ${DATADOG_INSTALL_PATH}/embedded/bin/python -m unittest -v tests.test_sample_check

