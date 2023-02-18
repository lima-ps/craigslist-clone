1. create a espcific virtual enviroment do our app
    />conda create --name codedaddie_list python=3

    /> conda activate codedaddie_list  //activate the enviroment

2. Intall Django
    /> pip install django

3. Start Project
    /> django-admin startproject dodedaddies_list

4. Create App
    /> cd dodedaddies_list
    /> python manage.py startapp my_app   //"my_app" is the name of the app

5. Create folders in the root: template and static
    //template gonna take all the html files
    //static gonna take the styles and layout managers

6. Register the APP in the 'settings.py'

    insert: import os  //"os" helps us to resources of the system, like find paths.
    insert: "name_Of_The_App" in the INSTALLED_APPS field.  //this add our app to the project
    insert next to BASE_DIR: TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')  #says where templates is stored
    insert insert: in TEMPLATES{DIRS: BASE_DIR,}
    insert: in th end of the file
            STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
            //helps django to find our static folder and files

7. add a file called "url.py" to config our routes.

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),  //routes examples
    ]

8. config the views functions in the views.py file

    def home(request): //function called by the routes in urls.py
        return render(request, 'base.html')

9. Config the urls.py file in the root project

    Add: path('', include('name_of_the_app.urls'))  //import include from django.urls
        //this put our urls index new file from the app to the path of the root project

9. RUN APP
    /> python manage.py runserver

10. Config to use Python admin page

    //this migrate our models to the database

        /> python manage.py makemigrations
        /> python manage.py migrate

    //creating the admin user
        /> python manage.py createsuperuser
        admin
        admin@admin.com
        pass and confirm pass

    //acess the page localhost/admin

11. Config the Models

    //this will be create our DB tables

    class Search(models.Model):
        search = models.CharField(max_length=500)
        created = models.DateField(auto_now=True)

12. Showing in admin page our tables/models

    from .models import Search
    admin.site.register(Search)

13. FRONTEND CONFIG

    a) Created a folder "CSS" and inside a file "style.css"

    b) 
