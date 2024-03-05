from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None, phone_number=None,
        contact_by_phone=False):
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            contact_by_phone=contact_by_phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None, phone_number=None,
        contact_by_phone=False):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone_number=phone_number,
            contact_by_phone=contact_by_phone,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staff(self, first_name, last_name, email, password=None, phone_number=None,
        contact_by_phone=False):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            phone_number=phone_number,
            contact_by_phone=contact_by_phone,
        )
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user
