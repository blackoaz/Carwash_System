Models

: Invoice for the actual invoice, and 
ItemLine, which represents a single row in the invoice. Let’s outline the relationships 
between these models:
• Each Invoice can have one or many ItemLines
• An ItemLine belongs to exactly one Invoice
This is a many-to-one (or one-to-many) relationship, which means that ItemLine
will have a foreign key to Invoice

In addition, each Invoice is associated with 
a User

This means:
• A User can have many Invoices
• Each Invoice belongs to one User



Class Based Views 

views.TodoList is an instance of a class-based generic view
. Django’s generic views help us quickly write views
(without having to write too much repetitive code) to do common tasks like:
- Display a list of objects, e.g. list of todos.
- Display detail pages for a single object. E.g. detail page of a todo.
- Allow users to create, update, and delete objects – with or without authorization.

These classes go under the name of class-based view, or CBV for short. 
Some examples of CBV in Django are CreateView, ListView, DeleteView, UpdateView, 
and DetailView. As you might have noticed, the naming of these classes goes hand 
in hand with the CRUD pattern, so common in REST APIs and in traditional web 
applications. In particular:
• CreateView and UpdateView for POST requests
• ListView and DetailView for GET requests
• DeleteView for DELETE requests

For a complete list of class-based views in Django, see ccbv.co.uk.

The Django REST Framework follows the same convention and offers a wide toolbox 
of class-based views for REST API development:
• CreateAPIView for POST requests
• ListAPIView and RetrieveAPIView for GET requests
• DestroyAPIView for DELETE requests
• UpdateAPIView for PUT and PATCH requests

see cdrf.co.

You will use a lot of these CBVs in your decoupled 
Django projects to speed up development of the most common tasks, although the DRF 
offers a more powerful layer on top of CBVs, called viewsets

In Django and the DRF, we use class-based views to expose common 
CRUD operations in terms of GET, POST, PUT, and so on. Nevertheless, the Django REST 
Framework offers a clever abstraction over class-based views, called viewsets, which 
make the DRF look more “resourceful” than ever.

```py
from rest_framework import viewsets
from .models import Blog, BlogSerializer
class BlogViewSet(viewsets.ModelViewSet):
 queryset = Blog.objects.all()
 serializer_class = BlogSerializer
Such a viewset gives you all the methods for handling common CRUD operations for 
free
```

Relationship Between Viewset Methods, HTTP Methods, and CRUD 
Operations
Viewset Methods HTTP Method CRUD Operation
create() POST Create resource
list() / retrieve() GET Retrieve resource(s)
update() PUT Update resource
destroy() DELETE Delete resource
update() PATCH Partial update resource

Once you have a viewset, it’s only a matter of wiring up the class with an 
urlpatterns

from .views import BlogViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"blog", BlogViewSet, basename="blog")
urlpatterns = router.urls


In our serializer we can expose this relationship as an hyperlink

class QuoteSerializer(serializers.ModelSerializer):
 client = serializers.HyperlinkedRelatedField(
 read_only=True, view_name="users-detail"
 )
 class Meta:
 model = Quote
 fields = ["client", "proposal_text"]

class TodoList(generics.ListAPIView):
# ListAPIView requires two mandatory attributes, serializer_class and
# queryset.
# We specify TodoSerializer which we have earlier implemented
serializer_class = TodoSerializer
def get_queryset(self):
user = self.request.user
return Todo.objects.filter(user=user).order_by('-created')

To
have a read-write endpoint, we use ListCreateAPIView. It is similar to ListAPIView but allows for creation as well.

However, when you attempt to add a todo via the form, you get an error like IntegrityError

This is because we have not specified a user who created this todo. To do so, we have to customize the creation
process using perform_create.
perform_create
What is missing currently is when we create a todo, we should automatically assign the user who created it.

def get_queryset(self):
user = self.request.user
return Todo.objects.filter(user=user).order_by('-created')


def perform_create(self, serializer):
#serializer holds a django model
serializer.save(user=self.request.user)
perform_create acts as a hook which is called before the instance is created in the database. Thus, we can specify
that we set the user of the todo as the request’s user before creation in the database.

A very common occurring pattern is retrieving,
editing and deleting a specific model instance. To achieve this, we implement a get(), put() and delete() endpoint.
Django REST Framework provides the built-in RetrieveUpdateDestroyAPIView to automatically implement the
get(), put() and delete() endpoint.

urlpatterns = [
path('todos/', views.TodoListCreate.as_view()),
path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
serializer_class = TodoSerializer
permission_classes = [permissions.IsAuthenticated]
def get_queryset(self):
user = self.request.user
# user can only update, delete own posts
return Todo.objects.filter(user=user)

how do we implement views for customised logic
path('todos/', views.TodoListCreate.as_view()),
path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),

class TodoToggleComplete(generics.UpdateAPIView):
serializer_class = TodoToggleCompleteSerializer
permission_classes = [permissions.IsAuthenticated]
def get_queryset(self):
user = self.request.user
return Todo.objects.filter(user=user)
def perform_update(self,serializer):
serializer.instance.completed=not(serializer.instance.completed)
serializer.save()

class TodoToggleCompleteSerializer(serializers.ModelSerializer):
class Meta:
model = Todo
fields = ['id'] # why need to show id?
read_only_fields = ['title','memo','created','completed']














# Permissions

Currently, we allow anyone to access the API endpoint and list or create a todo. But this obviously shouldn’t be the
case as we only want registered users to call the API to read/create their own todos

from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo
class TodoListCreate(generics.ListCreateAPIView):
...
serializer_class = TodoSerializer
permission_classes = [permissions.IsAuthenticated]

There are other permissions like:
- IsAdminUser – only admins/superusers have access
- AllowAny – any user, authenticated or not, has full access



















 # Async

 Asynchronous code is all about non-blocking execution.

 Due to the single-threaded nature of the Python 
interpreter, our code runs in sequential steps. In our view, we can’t return the response 
to the user until the API call completes. I

Traditionally, to overcome this problem in Django, we would use a task 
queue, a component that runs in the background, picks up tasks to execute, and returns 
the result later. The most popular task queues for Django are Celery and Django 
Q.

  To recap, things you can do now that asynchronous Django is a thing:
• Efficiently execute multiple HTTP requests in parallel in a view
• Schedule long-running tasks
• Interact safely with external systems
There are still things missing before Django and the DRF become 100% 
asynchronous—the ORM and the Django REST views are not asynchronous—but we will 
use asynchronous Django capabilities here and there in our decoupled project to practice.

Splitting the Requirements File