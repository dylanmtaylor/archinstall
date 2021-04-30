import archinstall

# Define the package list in order for lib to source
# which packages will be installed by this profile
__packages__ = ["apparmor"]

installation.add_additional_packages(__packages__)

installation.enable_service('apparmor')
