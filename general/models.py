from django.db import models

class Project(models.Model):
	"""Model definition for Project."""

	name = models.CharField('プロジェクト名', max_length=255)
	slug = models.SlugField('プロジェクトスラグ', unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	overview = models.CharField('概要', max_length=255, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	RELEASE_CONDITION = (
		('public', '全員に公開'),
		('limited', 'LIMITED')
	)
	release_condition = models.CharField('閲覧制限', max_length=50, choices=RELEASE_CONDITION, default='limited')

	class Meta:
		"""Meta definition for Project."""
		verbose_name = 'Project'
		verbose_name_plural = 'Projects'

	def __str__(self):
		"""Unicode representation of Project."""
		return self.name
