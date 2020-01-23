from django.contrib import admin

from markdownx.models import MarkdownxField
from markdownx.admin import MarkdownxModelAdmin
from markdownx.widgets import AdminMarkdownxWidget

from .models import Project, Tag

admin.site.register(Tag)

class CustomAdminMarkdownxWidget(AdminMarkdownxWidget):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.attrs={'cols': 50, 'rows': 30}
		"""
		forms.TextAreaのattrsを書き換えている。
		"""

class CustomMarkdownxModelAdmin(MarkdownxModelAdmin):
	list_display = ('name', 'slug', 'overview', 'description', 'release_condition',)
	
	formfield_overrides = {
		   MarkdownxField: {'widget': CustomAdminMarkdownxWidget}
	} 
   
admin.site.register(Project, CustomMarkdownxModelAdmin)