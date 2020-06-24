from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _
import re

class SymbolPasswordValidator:
	def __init__(self):
		self.message = "The password must contain at least one special character."

	def validate(self,password,user=None):
		if re.search('[^A-Za-z0-9]', password) is None:
			raise ValidationError(
					_('Password must one special character'),
					code="missing_symbol",
				)
	def get_help_text(self):
		return self.message

class NumberPasswordValidator:
	def __init__(self):
		self.message = "The password must contain at least one number."

	def validate(self,password,user=None):
		if re.search(r'\d',password) is None:
			raise ValidationError(
					_('Password must one Number'),
					code="missing_symbol",
				)

	def get_help_text(self):
		return self.message
