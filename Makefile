# $(shell chmod -x ./install_module.sh)
# $(shell bash ./install_module.sh)
# chmod -x ./install_module.sh

install_module:
	@ echo "install"
	VAR=$$( sudo echo "ls -lah" ) && bash -c "sudo -s $$VAR"

run:
	@ echo "hello"