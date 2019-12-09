from pathlib import Path
from typing import Optional
import requests

import click

from AliceSK.validate.src.DialogValidation import DialogValidation
from AliceSK.validate.src.InstallValidation import InstallValidation
from AliceSK.validate.src.TalkValidation import TalkValidation
from AliceSK.validate.src.Validation import Validation


class Validator:

	def __init__(self, skillPaths: list, verbosity: int = 0, username: str = 'ProjectAlice', token: str = None):
		self._dirPath = Path(__file__).resolve().parent.parent
		self._skillPath = self._dirPath.parent.parent
		self._skillPaths = skillPaths
		self._verbosity = verbosity
		self._username = username
		self._token = token


	@staticmethod
	def indentPrint(indent: int, *args):
		click.echo(' ' * (indent - 1) + ' '.join(map(str, args)))


	def validate(self):
		err = 0
		dialog = DialogValidation(self._username, self._token)
		installer = InstallValidation()
		talk = TalkValidation()
		
		for skillPath in self._skillPaths:
			skill = Path(skillPath)
			dialog.reset(skill)
			installer.reset(skill)
			talk.reset(skill)
			
			dialog.validate(self._verbosity)
			installer.validate()
			talk.validate()
			
			if dialog.errorCode or installer.errorCode or talk.errorCode:
				err = 1
				self.indentPrint(0, click.style(f'{skill.name}', fg='red', bold=True), 'invalid')
				self.printErrors('Installer', installer)
				self.printErrors('Dialog files', dialog)
				self.printErrors('Talk files', talk)
				self.indentPrint(0)
			else:
				self.indentPrint(0, click.style(f'{skill.name}', fg='green', bold=True), 'valid')

		return err


	def printErrors(self, name: str, validation: Validation):
		if validation.errorCode:
			self.indentPrint(2, click.style(f'{name}:', bold=True))
			click.echo(validation.errors)
		else:
			self.indentPrint(2, click.style(name, bold=True), 'valid')
