from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Project(models.Model):
	"""Model definition for Project."""

	name = models.CharField('プロジェクト名', max_length=255)
	slug = models.SlugField('プロジェクトスラグ', unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	overview = models.CharField('概要', max_length=255, null=True, blank=True)
	# description = models.TextField(null=True, blank=True)
	description = MarkdownxField('本文', help_text='write down in markdown format', null=True, blank=True)
	
	RELEASE_CONDITION = (
		('public', '全員に公開'),
		('limited', 'LIMITED')
	)
	release_condition = models.CharField('閲覧制限', max_length=50, choices=RELEASE_CONDITION, default='limited')

	tags = models.ManyToManyField('Tag')

	class Meta:
		"""Meta definition for Project."""
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'

	def __str__(self):
		"""Unicode representation of Project."""
		return self.name

	def formatted_markdown(self):
		""" md => html文字列 """
		return markdownify(self.description)

class Tag(models.Model):
	"""
	プロジェクトにつくタグモデル 
	"""
	name = models.CharField('タグ名', max_length=255)
	slug = models.SlugField('タグスラグ', unique=True)
	
	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def __str__(self):
		return self.name
