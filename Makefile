MAGENTA=`tput setaf 5`
RESET=`tput sgr0`

setup-environment:
	@echo "Setting up environment..."
	@conda env create -f environment.yaml
	@echo "${MAGENTA}Remember to activate your environment with these instructions ^${RESET}"

format:
	@echo "Running autopep8 and isort to fix any formatting issues in the code"
	@autopep8 --in-place --recursive .
	@isort .
	@echo "Running flake8 to check for any other formatting issues"
	@flake8 .

run:
	@echo "Running pipeline..."
	@python -m run_pipeline
