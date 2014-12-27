## DJANGO BASIC CRUD

This project is meant as an example of simple CRUD built from Django framework and Django REST framework.


### Installation
  * Install python
  * Install pip
  * Using `pip install -r djabacrud/requirements.txt` command to install project's dependencies
  * Vagrant
    + `vagrant box add hashicorp/precise32`
    + `vagrant up`


### Start the Project

#### Database
  * Set up: `python manage.py syncdb`
  * Migration: `python manage.py migrate`

#### Server
  * Run the server: `python manage.py runserver`


### The Blog

#### Basic CRUD:
  * All blog posts, which are published, are on homepage.
  * Create blog button used to create new blog post
  * The links on the blogs' titles will bring to an individual blog posts' detail
  * In a blog post detail there will be an `Edit` button to update the blog post
  * In a blog post detail there will be a `Delete` button to delete the blog post

#### API:
  * The `/api/blog/` is for `get` the list of the blog posts and `create` new blog post
  * The `/api/blog/<post_id>` is for `get` individual blog post by `id`, and `update` and `delete` individual the blog post


### Testing

#### Syntax
  * Syntax checking and follow the `pep8`

### Unitest
  * The project come with the test suite in the file `tests.py`

### License
MIT

### Greeting
Hope this will be a good example for anyone starting on working with Django framework
