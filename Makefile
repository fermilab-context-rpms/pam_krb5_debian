_default:
	@echo "make"
sources:
	@echo "make sources"
srpm: sources
	rpmbuild -bs --define '_sourcedir .' --define '_srcrpmdir .' pam_krb5_debian.spec
