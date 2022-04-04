from django_seed import Seed

seeder = Seed.seeder()

from .models import Category, Post
seeder.add_entity(Category, 5)
seeder.add_entity(Post, 10)

inserted_pks = seeder.execute()