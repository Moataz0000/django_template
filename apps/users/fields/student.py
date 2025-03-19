class StudentFields:
    PASSWORD = "password"
    LAST_LOGIN = "last_login"
    IS_SUPERUSER = "is_superuser"
    POLYMORPHIC_CTYPE = "polymorphic_ctype"
    USERNAME = "username"
    IS_ACTIVE = "is_active"
    IS_STAFF = "is_staff"
    DATE_JOINED = "date_joined"
    GROUPS = "groups"
    USER_PERMISSIONS = "user_permissions"
    PHONE_NUMBER = "phone_number"
    IMAGE = "image"
    FULL_NAME = "full_name"
    CLASS_NUMBER = "class_number"

    @classmethod
    def get_field_name(cls, model, field):
        return model._meta.get_field(field).name