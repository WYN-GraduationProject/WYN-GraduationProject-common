BASE_DIR = ./proto
LAUNCH_PYTHON_DIR = video_service

PY_TARGET_DIR = ./proto_build/python
PY_PACKAGE_DIR = ./python_common

PYTHON_SRC = $(shell find $(foreach dir, $(LAUNCH_PYTHON_DIR), $(BASE_DIR)/$(dir) ) -name "*.proto")

.PHONY:clean

%/.:
	@mkdir -p "$@"

all: python3

python3: | $(PY_TARGET_DIR)/.
	python3 -m grpc_tools.protoc -I. --python_out=$(PY_TARGET_DIR) --pyi_out=$(PY_TARGET_DIR) --grpc_python_out=$(PY_TARGET_DIR) \
	$(PYTHON_SRC)
	find $(PY_TARGET_DIR) -type d -exec touch {}/__init__.py \;
	rm -f $(PY_TARGET_DIR)/__init__.py;
	cp -r $(PY_TARGET_DIR)/* $(PY_PACKAGE_DIR)/
