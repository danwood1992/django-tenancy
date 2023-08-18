import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment, Like
from.types import PostType, CommentType, LikeType
from apps.admin.realms.models import RealmAccount
from apps.admin.realms.types import RealmAccountType
from apps.admin.realms.types import RealmType
from apps.admin.realms.models import Realm

# I have commented heavily for an easier time creating a new mutation 

