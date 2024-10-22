from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Mediator(ABC):
	@abstractmethod
	def notify(sender: Component, event: str):
		pass


class AuthenticationDialog(Mediator):
	def __init__(self, title, login_or_register_checkbox: Checkbox, username: TextBox, password: TextBox, email: TextBox, ok_button: Button, cancel_button: Button):
		self.title = title

		self.login_or_register_checkbox = login_or_register_checkbox
		self.login_or_register_checkbox.mediator = self
		
		self.ok_button = ok_button
		self.ok_button.mediator = self

		self.cancel_button = cancel_button
		self.cancel_button.mediator = self

	def notify(self, sender: Component, event: str):
		if sender == self.login_or_register_checkbox and event == 'check':
			if self.login_or_register_checkbox.checked:
				print('1. Show login form components.')
				print('2. Hide registration form components.')
			else:				
				print('# 1. Show registration form components.')
				print('# 2. Hide login form components')

		elif sender == self.ok_button and event == 'click':
			if self.login_or_register_checkbox.checked:
				print('Try to find a user using login credentials.')
			else:
				print('1. Create a user account using data from the registration fields.')
				print('Log that user in.')


class Component:

	def __init__(self, dialog: Mediator = None) -> None:
		self.mediator = dialog

	def click(self):
		self.mediator.notify(self, 'click')

	def keypress(self):
		self.mediator.notify(self, 'keypress')


class Button(Component):
	pass


class TextBox(Component):
	pass


class Checkbox(Component):
	checked = True

	def check(self):
		self.mediator.notify(self, 'check')


if __name__ == '__main__':
	login_or_register_checkbox = Checkbox()
	username_textbox = TextBox()
	password_textbox = TextBox()
	email_textbox = TextBox()
	ok_button = Button()
	cancel_button = Button()


	login_dialog = AuthenticationDialog(
	    "Log in", login_or_register_checkbox, username_textbox, password_textbox, email_textbox, ok_button, cancel_button 
	)
	login_or_register_checkbox.check()

	print('#' * 40)

	register_dialog = AuthenticationDialog(
		'Register', login_or_register_checkbox, username_textbox, password_textbox, email_textbox, ok_button, cancel_button,
	)
	ok_button.click()

	print('#' * 40)

	login_or_register_checkbox.checked = False
	ok_button.click()