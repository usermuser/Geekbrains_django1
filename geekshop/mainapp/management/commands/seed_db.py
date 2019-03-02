from django.core.management.base import BaseCommand

from mainapp.models import Category, Product
#from django.contrib.auth.models import User
from authapp.models import CustomUser
from django.db.utils import IntegrityError
#from authapp.models import DoesNotExist


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        first_cat = Category()
        first_cat.name = 'Печеньки'
        first_cat.slug = 'Pechenki'
        first_cat.save()
        first_cat_fk = first_cat.id
        print('[+] New Category() with name {} created successfully'.format(first_cat.name))

        second_cat = Category()
        second_cat.name = 'Чай'
        second_cat.slug = 'Chai'
        second_cat.save()
        second_cat_fk = second_cat.id
        print('[+] New Category() with name {} created successfully'.format(second_cat.name))


        # delete all products in db and create new
        Product.objects.all().delete()

        new_prod = Product()
        new_prod.name = 'овсяные'
        new_prod.slug = 'ovsyanye'
        new_prod.image = 'products/2019/01/27/red_tea.jpg'
        new_prod.description = 'Описание овсяного печенья.' \
                               'Lorem ipsum dolor sit amet, consectetur adipisicing elit. ' \
                               'Est in deleniti magnam non debitis perferendis dolor, ' \
                               'doloremque expedita sunt voluptatibus illo eveniet maxime ' \
                               'velit placeat nam aliquam excepturi quod distinctio.'
        new_prod.price = 1000
        new_prod.stock = 49
        new_prod.available = 1
        new_prod.created = '2019-01-2719:34:46.138152'
        new_prod.updated = '2019-01-2719:34:46.138194'
        new_prod.category_id = first_cat_fk
        new_prod.save()
        print('[+] New Product() with name {} created succesfully'.format(new_prod.name))



        second_prod = Product()
        second_prod.name = 'крекер'
        second_prod.slug = 'kreker'
        second_prod.image = 'products/2019/01/27/red_tea_NBB25mC.jpg'
        second_prod.description = 'Описание крекерного печенья.' \
                               'Lorem ipsum dolor sit amet, consectetur adipisicing elit. ' \
                               'Est in deleniti magnam non debitis perferendis dolor, ' \
                               'doloremque expedita sunt voluptatibus illo eveniet maxime ' \
                               'velit placeat nam aliquam excepturi quod distinctio.'
        second_prod.price = 100
        second_prod.stock = 40
        second_prod.available = 1
        second_prod.created = '2019-01-27 19:35:14.143002'
        second_prod.updated = '2019-01-27 19:35:21.173421'
        second_prod.category_id = first_cat_fk
        second_prod.save()
        print('[+] New Product() with name {} created succesfully'.format(second_prod.name))

        third_prod = Product()
        third_prod.name = 'Черный чай'
        third_prod.slug = 'Cherniy-chai'
        third_prod.image = 'products/2019/01/27/red_tea_NBB25mC.jpg'
        third_prod.description = 'Описание черного чая.' \
                                  'Lorem ipsum dolor sit amet, consectetur adipisicing elit. ' \
                                  'Est in deleniti magnam non debitis perferendis dolor, ' \
                                  'doloremque expedita sunt voluptatibus illo eveniet maxime ' \
                                  'velit placeat nam aliquam excepturi quod distinctio.'
        third_prod.price = 555
        third_prod.stock = 3
        third_prod.available = 1
        third_prod.created = '2019-01-27 19:35:14.143002'
        third_prod.updated = '2019-01-27 19:35:21.173421'
        third_prod.category_id = second_cat_fk
        third_prod.save()
        print('[+] New Product() with name {} created succesfully'.format(third_prod.name))


        # check if superuser with name 'admin1234' already in db, if not - create


        new_admin = 'admin1234'
        try:

            old_admin = CustomUser.objects.get(username=new_admin)

        except Exception as e:  # refactor this code later (catch errors properly)

            print(e)

            new_admin = CustomUser.objects.create_superuser(
                'admin1234', 'admin@admin.ru', '1234', age=22
            )

            print('[+] new superuser with name {} created successfully'.format(new_admin))

        else:
            print('[-] {} is already exists, no need to create'.format(new_admin))











