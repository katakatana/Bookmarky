from django.db import models
from django.contrib.auth.models import User, AnonymousUser


class Profile(models.Model):
    """ This model is reserved for [Bookmark]s' [User <-> Profile] only.
     Anonymous user profile should be created for the Profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        user_username = f"[user]/username = {self.user.username}" if self.user.username else ''
        bio = f"bio = {self.bio}" if self.bio else ''
        location = f"location = {self.location}" if self.location else ''
        birth_date = f"birth_date = {self.birth_date}" if self.birth_date else ''

        props = "; ".join(filter(None, [user_username, bio, location, birth_date]))
        return f"[{props}]"


class Tag(models.Model):
    """ Tags are selected by [User] [Profile]s when creating [Bookmark]s
        but are selected from a dictionary of [Allowed Tags] """
    keyword = models.CharField(max_length=256, unique=True, blank=False)

    def __str__(self):
        return f"[keyword = #{self.keyword}]"


class Bookmark(models.Model):
    """ User [Profiles] Create Shared [Bookmark]s with associated [Tag]s """
    text = models.TextField()
    # :: ^ In the next [phase] I shall ManyToMany this into a [Resource] model, where a
    # resources = model.ManyToManyField('Resource')
    # ::~

    tags = models.ManyToManyField(Tag)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()

    #
    # Todo: Add optional [Category] where:: [Category] is a model of a [Tree]
    #

    def __str__(self):
        text = f"text = {self.text}" if self.text else ''

        tags_keyword = ['#' + str(tag.keyword) for tag in self.tags.all()]
        tags_keyword = '[tags]/keyword = [' + '; '.join(tags_keyword) + ']' if tags_keyword else ''

        if self.owner and self.owner.user and self.owner.user.username:
            owner_user_username = f"[owner/user]/username = {self.owner.user.username}"
        else:
            owner_user_username = ''

        created_on = f"created_on = {self.created_on}" if self.created_on else ''
        updated_on = f"updated_on = {self.updated_on}" if self.updated_on else ''

        props = "; ".join(filter(None, [text, tags_keyword, owner_user_username, created_on, updated_on]))
        return f"[{props}]"



