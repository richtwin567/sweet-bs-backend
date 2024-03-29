from flask_admin import Admin
from api.db.models import (
    IngredientModel,
    MenuItemCategoryModel,
    MenuItemModel,
    OrderItemModel,
    OrderModel,
    UserModel)

from flask_admin.contrib.sqla import ModelView
from flask_admin.model.form import InlineFormAdmin

from app import FlaskApp


class Views:
    """Wrapper View class for adding all Model Views to the admin portal"""

    def __init__(self, app: FlaskApp) -> None:
        self.admin = Admin(app, name='Sweet B\'s', template_mode='bootstrap3')

        self.admin.add_view(self.UserView(UserModel, app.db.session))
        self.admin.add_view(self.IngredientView(
            IngredientModel, app.db.session))
        self.admin.add_view(self.MenuItemView(MenuItemModel, app.db.session))
        self.admin.add_view(self.OrderView(OrderModel, app.db.session))
        self.admin.add_view(self.OrderItemView(OrderItemModel, app.db.session))
        self.admin.add_view(self.MenuItemCategoryView(
            MenuItemCategoryModel, app.db.session))

    class IngredientView(ModelView):
        column_display_all_relations = True
        column_display_pk = True
        column_default_sort = 'id'
        form_excluded_columns = ['related_menuitems']

    class MenuItemView(ModelView):
        column_display_all_relations = True
        column_default_sort = 'id'
        column_exclude_list = ['orderitems', ]
        column_display_pk = True
        form_excluded_columns = ['orderitems', ]
        column_list = ('id', 'flavour', 'category', 'price',
                       'description', 'image_url', 'ingredients')

    class OrderItemView(ModelView):
        column_default_sort = 'id'
        column_display_all_relations = True
        column_display_pk = True
        can_create = False
        can_delete = False
        can_edit = False

    class OrderView(ModelView):

        class OrderItemInline(InlineFormAdmin):
            form_columns = ('id', 'qty', 'menuitem')

        column_default_sort = 'id'
        column_display_all_relations = True
        column_display_pk = True
        inline_models = (OrderItemInline(OrderItemModel),)

    class UserView(ModelView):

        column_default_sort = 'id'
        column_display_all_relations = True
        column_display_pk = True
        form_columns = ('firstname', 'lastname', 'email', 'username',
                        'password', 'address', 'is_admin', 'created_on',
                        "public_id")

        form_excluded_columns = ['orders_placed', ]

        form_widget_args = {
            'created_on': {
                "disabled": True
            },
        }

        can_view_details = True

        column_formatters = {
            '_password': lambda v, c, m, p: m.password[:4] + "..." + m.password[-3:]
        }

    class MenuItemCategoryView(ModelView):
        column_default_sort = 'id'
        column_display_all_relations = True
        column_display_pk = True
        form_excluded_columns = ['menuitems']
