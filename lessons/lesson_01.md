# Django & Django REST Framework

## Why Python
* The elegance, simplicity and robustness
* Write once, run anywhere
* Suitable for a lot of software problems: web applications, IoT, data science etc

## Why Django

* It is a mature Framework based on industry best-practises, that has evolved over the years through countless iterations by the community
* The documentation is really good, which makes it easy to get started
* Upgrading Django to new versions is quite easy (though this hasn’t always been)
* Easy to write tests
* The security level of the project is world class, just like the patches that are written for Django
* First-class support for the most mature open source relational database, PostgreSQL

## Why Django Rest Framework

When Django was first released in 2005, at the time most websites consisted of one large monolithic codebase. The *back-end* consisted of database models, URLs, and views which interacted with the *front-end* templates of HTML, CSS, and JavaScript that controlled the presentational layout of each web page. However in recent years an “API-first” approach has emerged as arguably the dominant paradigm in web development. This approach involves formally separating the back-end from the front-end. This approach of dividing services into different components, by the way, is broadly known as **Service-oriented architecture**.

The advantage of separating the front-end from the back-end is that the app becomes much more *future-proof* because a back-end API can be consumed by multiple front-ends written in different languages and frameworks.
With a traditional monolithic approach, a Django website cannot support these various front-ends. But with an internal API, all three can communicate with the same underlying database back-end!

`Django` and `Django REST Framework` is a powerful and accessible way to build web APIs. And while there are multiple ways to build an API, web APIs–which allow for the transfer of data over the world wide web–are overwhelmingly structured in a RESTful pattern. REST stands for Representational State Transfer and as you might be able to infer by its name, it is a style of creating API’s that allows you to communicate the state of the stateful server to the client in a representational way. what does representational mean in this context? It means that we give the client a window into each resource that we store on the server where the client can properly understand the resource in the same structure as it is being stored.

REST does allow us to do **CRUD** actions to each of our resources. This means that we can `Create`, `Read`, `Update` and `Delete` each resource. Since we are using the HTTP protocol, we will do these actions using different HTTP verbs such as

* `GET`, used to read a resource.
* `POST`, used to create a new resource.
* `PATCH`, used to update an existing resource.
* `PUT`, used to replace an existing resource.
* `DELETE`, used to delete an existing resource.

Structure the REST API URI’s

Let’s imagine that we have the following 2 resources:

* Article
* Category

We will set up separate endpoints for each resource:

* /api/articles/, List a collection of Articles.
* /api/articles/<id>/, Display a single Article.
* /api/categories/, List a collection of Categories.
* /api/categories/<id>/, Display a single Category.

By structuring our API in this manner, it is very easy for the client to know which resources it is fetching, and it is very easy to update or modify a single, specific resource.

On top of that, we can also make sure that each response is stateless. We do not have a `/api/get_current_article/` or `/api/get_liked_categories/` that depend on the logged in user or the state of the client, instead the client is explicit about fetching the exact article it wants. This also makes things very Cacheable, another constraint and requirement for our RESTful Design.

DjangoRestFramework is based on 4 main files:

`Models`(models.py) -> `Serializer`(serializer.py) -> `Viewset`(views.py) -> `Router`(urls.py)

### Models

Define the data model

```py
from django.db import models


class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    price_usd = models.DecimalField(
        max_digits=20, decimal_places=2, null=True)
    price_btc = models.DecimalField(
        max_digits=50, decimal_places=20, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.symbol)
```


### Serializers

```py
from rest_framework import serializers

from .models import Coin


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = ('id', 'name', 'symbol', 'price_usd', 'price_btc')
```

Any field that is not listed there, the API is going to ignore. Private internal fields just leave them out of the serializer and they wont be exposed. 

### Views

What do views do?

* Determine what verb is being used
* Check permisions
* Get relevant data
* Serialize data
* Run any filters you need

```py
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins

from django_filters import rest_framework as filters

from .filters import BitFilter, CoinFilter
from .models import Coin
from .serializers import CoinSerializer


class CoinViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CoinSerializer
    filter_backends = (filters.DjangoFilterBackend, BitFilter)
    queryset = Coin.objects.all()
    filter_class = CoinFilter
```

### Router

They route our url to the correct view.

# Database

By default Django ships with the lightweight SQLite db. PostgreSQL is a powerful, open-source, object-relational database system that uses and extends the SQL language in combination with many other features. PostgreSQL has earned a strong reputation for its proven architecture, reliability, data integrity, robust feature set, extensibility, and the dedication of the open-source community behind the software to consistently deliver performant and innovative solutions. PostgreSQL runs on all operating systems and has been ACID-compliant since 2001. 

Using PostgreSQL and Django together offers many benefits:

* Django provides a number of data types that will only work with PostgreSQL.
* Django has django.contrib.postgres to make database operations on PostgreSQL. 
* If you are building an application with maps or you are storing geographical data, you need to use PostgreSQL, as * GeoDjango is only fully compatible with PostgreSQL.
* PostgreSQL has the richest set of features that are supported by Django.

Download and install Postgres software to your local machine, after that proceed to set it up as the default persistence layer for the API in settings.py. Add configuration to .env file.

## User Model and Authentication

To help with creating users,Django ships with a default User Model. The default user model includes fields such as

* id
* username(Django will use this for login by default)
* email
* first_name
* last_name
* is_active
* is_staff
* is_super_user
* date_joined
* password
* last_login

While it works well there are limitations to the implementation that may require you to extend it. Default user model limitations

1. The username field is case-sensitive

Even though the username field is marked as unique, by default it is not case-sensitive. That means the username `samwel.kanda` and `Samwel.kanda` identifies two different users in your application. If the user does not type the username exactly in the same way when they created their account, they might be unable to log in to your application.

2. The email field is not unique

Multiple users can have the same email address associated with their accounts. By default, the email is used to recover a password. If there is more than one user with the same email address, the password reset will be initiated for all accounts and the user will receive an email for each active account.

3. The email field is not mandatory

By default the email field does not allow null, however, it allows blank values, so it pretty much allows users to not inform an email address.

4. A user without a password cannot initiate a password reset

There is a small catch on the user creation process that if the `set_password` method is called passing `None` as a parameter, it will produce an unusable password. And that also means that the user will be unable to start a password reset to set the first password.

To address the limitations, there are two options: (1) implement workarounds to fix the behavior of the default user model; (2) replace the default user model altogether and fix the issues for good. What is going to dictate what approach you need to use is in what stage your project currently is.(Existing project vs New project)

Changing the user model is something you want to do early on. After your database schema is generated and your database is populated it will be very tricky to swap the user model. Swapping the default user model is very difficult after you created the initial migrations 

![Django User Model](./img/django-user-model.png)

So extending the `AbstractUser` class is only useful when you want to modify its methods, add more fields or swap the objects manager.

If you want to remove a field or change how the field is defined, you have to extend the user model from the `AbstractBaseUser`.

The best strategy to have full control over the user model is to create a new concrete class from the `PermissionsMixin` and the `AbstractBaseUser`. Note that the PermissionsMixin is only necessary if you intend to use the Django admin or the built-in permissions framework.

### Authentication

* **Basic Authentication** - Anytime you need to fetch info from the database you need to send your username and password. The credentials are checked against the database and then you are authenticated. This is highly ineffiecient.
* **Token Authentication** - Creates a token table in the database, generates a token for an authenticated user and sends it back to the user. Next time you need something from the database, you supply the token. Everytime the token will be checked against the database. Also token never expires unless you revoke it
* **JWT Authentication**. Uses cryptographic signing. Username and password is supplied. Token gets generated against a private key and not in the database. Everytime you want to get something you supply the token which is checked against the private key, not the database. 

#### djangorestframework-simplejwt

1. Pip install `djangorestframework-simplejwt`
2. Add add `rest_framework_simplejwt.authentication.JWTAuthentication` to the list of authentication
 classes in `settings.py`
3.  In your root urls.py file (or any other url config), include routes for Simple JWT’s `TokenObtainPairView` and `TokenRefreshView` views:
4 To verify that Simple JWT is working, you can use curl to issue a couple of test requests:

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "davidattenborough", "password": "boatymcboatface"}' \
  http://localhost:8000/api/token/

...
{
  "access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU",
  "refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"
}

You can use the returned access token to prove authentication for a protected view:

curl \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZiI6IuKYgyIsImV4cCI6MTIzNDU2LCJqdGkiOiJmZDJmOWQ1ZTFhN2M0MmU4OTQ5MzVlMzYyYmNhOGJjYSJ9.NHlztMGER7UADHZJlxNG0WSi22a2KaYSfd1S-AuT7lU" \
  http://localhost:8000/api/some-protected-view/

When this short-lived access token expires, you can use the longer-lived refresh token to obtain another access token:

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImNvbGRfc3R1ZmYiOiLimIMiLCJleHAiOjIzNDU2NywianRpIjoiZGUxMmY0ZTY3MDY4NDI3ODg5ZjE1YWMyNzcwZGEwNTEifQ.aEoAYkSJjoWH1boshQAaTkf8G3yn0kapko6HFRt7Rh4"}' \
  http://localhost:8000/api/token/refresh/

...
{"access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3BrIjoxLCJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiY29sZF9zdHVmZ

## Multi-tenacy

Multi-tenancy is an architecture in which a single instance of a software application serves multiple customers. Each customer is called a tenant. 

In a multi-tenant application, resources are shared between tenants but usually each tenant's information is private. This means that we must ensure that their information is secure and only accessible to their members.


### Main architectures

![multi-tenancy-approaches](./img/multi-tenant-approaches.webp)

#### 1. Instance Replication Model 

The system spins a new instance for every tenant. We can use docker to spin up the different tenants. This is maybe the safest option in terms of privacy and security. In this approach, each tenant has a standalone database instance where their data is stored. The application server must be connected to each of these instances and determine which database must be activated for each user(based on the tenant to which the user belongs).

Advantages

* The data is secure and private because it is stored in independent databases. Each tenant only has access to their own database, keeping the other tenant’s information private.
* Other tenants never connect to your database, resulting in better performance. 

Disadvantages

* Having multiple database instances means higher costs. 
* The management of each database is independent. All the management tasks, such as backups and vacuuming, must be done per instance.
* Having shared data between tenants is not trivial. In this approach, all the shared data must be replicated in all the databases.
* Hard to scale. It becomes a nightmare when 100s of tenants signup. Adding new tenants requires new connections to new databases. Implementing this approach requires an independent connection between the abbreviation server and each one of the databases. That means that when a new tenant is added, a new database must be created and connected to the application server. 

#### Data Segregation Model 

There are two types of approach in a data segregation model.

##### Shared database, shared schema

 In this case, all tenants’ information is stored in the same database schema, using the same tables. Each table of this schema has an attribute that identifies the tenant owner of that piece of information. A `ForeignKey` in the tables identifies the tenant. Data segregation is managed explicitly. after the initial migration to add a `tenant_id` everywhere, subsequent migrations were all regular, standard Django migrations. querying without appending `WHERE tenant_id = my_tenant_id` would give you back the whole info.

Advantages:

* All data is stored in a single instance. The configuration of this architecture is exactly the same as a standalone application, making all database management tasks easier (backups, vacuuming the instance, etc).
* A single connection exists between the database and the application server. Adding new tenants doesn’t require any configuration changes, making it a trivial task.
* Sharing data between tenants is easy. You only need to store that data in a table without the tenant_id column.

Disadvantages:

* The application server always needs to filter by `tenant_id` before accessing the data. If for some reason the filter is not applied, a user can access information from a tenant of which he is not a member. This is a privacy vulnerability because a single error that a developer might make in a component can compromise sensitive information.
* The whole performance of the app can be affected by a single tenant. As we have a single database instance and all the tables are shared between tenants. For example, if a tenant tries to execute a bulk operation over a huge table that requires locking it, the table will be locked for all tenants. This means that the usability of the application can be affected because a single tenant is applying a bulk operation.


##### Shared database, multiple schema.

In this case, we have a single database instance to store all the tenants’ information. The difference between this approach and the previous one is that we create a separate schema per tenant(named collections of tables). When the application server needs to access the data, the schema is activated based on the user and the tenant they belong to.

This approach has some of the same advantages as the previous ones:

* The data is secure and private because it is stored in independent schemas.
* All data is stored in a single instance, reducing costs and configurations and management tasks.
* Adding new tenants only involves the creation of new schemas. The connection to the database is shared, so no configuration changes are required.
* Sharing data between tenants is easy. All shared data can be stored in a public schema that all tenants can access.

Disadvantages:

* Changing the structure of the tables requires modifying multiple schemas. This is a management task that can be a little bit tedious and complex. Each time a tenant was created, they needed to have a new `Postgres schema`(named collections of tables) allocated for them and set up with the app’s current data schema. Then, any update to the data schema requires looping over all the tenant schemas.


Django provides currently no simple way to support multiple tenants using the same project instance

`django-tenants` is a django based package that will enable you to perform the creation of client-specific schemas in a single Postgres DB instance, in addition, it’ll also aid in request routing ensuring data isolation is maintained, in other words, every client will only access data associated with their account.

Tenants are identified via their host name (i.e tenant.domain.com). This information is stored on a table on the public schema. Whenever a request is made, the host name is used to match a tenant in the database. If there’s a match, the search path is updated to use this tenant’s schema. So from now on all queries will take place at the tenant’s schema. Tenant-specific apps do not share their data between tenants, but you can also have shared apps where the information is always available and shared between all.

Steps:
1. Pip install `django-tenants`
2. Change database engine to use django-tenants backend
3. Add `django_tenants.routers.TenantSyncRouter` to your `DATABASE_ROUTERS` setting, so that the correct apps can be synced
4. Add the middleware `django_tenants.middleware.main.TenantMainMiddleware` to the top of `MIDDLEWARE`, so that each request can be set to use the correct schema.
5. Add  `django.template.context_processors.request` listed under the `context_processors` option of `TEMPLATES` otherwise the tenant will not be available on `request`.
6. create your tenant model. You must inherit from `TenantMixin`. You also have to have a table for your domain names for this you must inherit from `DomainMixin`.
7. `TenantAdminMixin` is available in order to register the tenant model.create a the related admin class ClientAdmin. The mixin disables save and delete buttons when not in current or public tenant (preventing Exceptions).
8. Configure Tenant and Shared Applications. there are two settings called `SHARED_APPS` and `TENANT_APPS`. `SHARED_APPS` is a tuple of strings just like `INSTALLED_APPS` and should contain all apps that you want to be synced to public. If `SHARED_APPS` is set, then these are the only apps that will be synced to your public schema! The same applies for `TENANT_APPS`, it expects a tuple of strings where each string is an app. If set, only those applications will be synced to all your tenants.
9. You also have to set where your tenant & domain models are located. `TENANT_MODEL = "customers.Client"` `TENANT_DOMAIN_MODEL = "customers.Domain"`
10. Now run `migrate_schemas --shared`, this will create the shared apps on the public schema. Note: your database should be empty if this is the first time you’re running this command.
```py
python manage.py migrate_schemas --shared
```
11. Lastly, you need to create a tenant whose schema is public and it’s address is your domain URL. The command 
`create_tenant` creates a new schema.
```py
./manage.py create_tenant --domain-domain=newtenant.net --schema_name=new_tenant --name=new_tenant --description="New tenant"
```
The arguments are dynamic depending on the fields that are in the `TenantMixin` model. For example if you have a field in the `TenantMixin` model called company you will be able to set this using `–company=MyCompany`. If no argument are specified for a field then you be prompted for the values. There is an additional argument of `-s` which sets up a superuser for that tenant.
The command `create_tenant_superuser` is already automatically wrapped to have a schema flag. Create a new super user with

```py
./manage.py create_tenant_superuser --username=admin --schema=customer1
```

Note: If you want to use `django-tenants` in development you need to use a fake a domain name. All domains under the TLD .localhost will be routed to your local machine, so you can use things like tenant1.localhost and tenant2.localhost.



