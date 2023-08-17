import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment, Like
from.types import PostType, CommentType, LikeType
from apps.core.seats.models import StaffSeat
from apps.core.seats.types import StaffType
from apps.admin.tenancy.models.tenant import Tenant

# I have commented heavily for an easier time creating a new mutation 

