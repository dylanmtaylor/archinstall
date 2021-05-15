import subprocess
import os

from .exceptions import *
from .general import sys_command

def list_keyboard_languages():
	for line in sys_command("localectl --no-pager list-keymaps", environment_vars={'SYSTEMD_COLORS' : '0'}):
		yield line.decode('UTF-8').strip()

def list_x11_keyboard_languages():
	for line in sys_command("localectl --no-pager list-x11-keymap-layouts", environment_vars={'SYSTEMD_COLORS' : '0'}):
		yield line.decode('UTF-8').strip()

def verify_keyboard_layout(layout):
	for language in list_keyboard_languages():
		if layout.lower() == language.lower():
			return True
	return False

def verify_x11_keyboard_layout(layout):
	for language in list_x11_keyboard_languages():
		if layout.lower() == language.lower():
			return True
	return False

def search_keyboard_layout(filter):
	for language in list_keyboard_languages():
		if filter.lower() in language.lower():
			yield language

def set_keyboard_language(locale):
	if (output := self.arch_chroot(f'localectl set-keymap {locale}')).exit_code != 0:
		raise ServiceException(f"Unable to set locale '{locale}' for console: {output}")

	return True
