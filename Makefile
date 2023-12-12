MAGENTA=`tput setaf 5`
RESET=`tput sgr0`

setup-environment:
	@echo "Setting up environment..."
	@conda env create -f environment.yaml
	@echo "${MAGENTA}Remember to activate your environment with these instructions ^${RESET}"