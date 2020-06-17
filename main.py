from flask import Flask, redirect, url_for, request, render_template
from validatorex import Register_validator , Login_validator


app = Flask(__name__)

posts = [
	{'author':'Corey Schafer',
	 'title':'Blog post 1',
	 'content':'First post content',
	 'date_posted':'April 20,2018'

	 },
	 {
	 'author':'Jane Doe',
	 'title':'Blog post 2',
	 'content':'Second post content',
	 'date_posted':'April 21,2018'

	 },
	 {
	 'author':'Aanet Doly',
	 'title':'Blog post 3',
	 'content':'Third post content',
	 'date_posted':'April 27,2018'

	 }
 
]


@app.route('/')
@app.route('/home')
def index():
   return render_template("index.html",post_variable=posts)


@app.route('/about')
def about():

#	return ("<h1>Hello World</h1>
	return render_template("about.html",title=about)

# this shows the main route url name i choose is independent of the function 
# just thst it helps in the future to make your work less complicated and helps you understand the linkage
#   url_for function helps you generate  the right url for the function logincheck 
# irrespective of the name change i made to 
#         make it logincheck

@app.route('/regcheckZ/<alertdiv>')
def regcheck(alertdiv):
   if alertdiv :
      
      return render_template("register.html",alertmssgs=alertdiv)

   else:
      return render_template("register.html")



@app.route('/register')
def register():

   return render_template("register.html")

@app.route('/login')
def login():

   return render_template("login.html")



@app.route('/success/<name>')
def success(name):
    
    return render_template("index.html")


# this will load future validator functions when the validator class 
# on seperate python script has been imported here

@app.route('/regfunc',methods = ['POST', 'GET'])
def regload():
   if request.method == 'POST':

      firstname = request.form.get('fname')
      lastname = request.form.get('lname')
      username = request.form.get('username')
      email = str(request.form.get('email')).lower()
      passwd = request.form.get('password')
      confirm_passwd = request.form.get('confirm_password')

      # we create a temporal  instance that can store the results from the validorex script  
      validated=Register_validator(firstname,lastname,username,email,passwd,confirm_passwd)
      
     # now we can access the function since the instance has been set 
      if validated.validator():

         return render_template("index.html",post_variable=posts, reg_username=username)

      else:
         return False



@app.route('/loginfunc',methods = ['POST'])
def loginload():
   if request.method == 'POST':

      username = request.form.get('username')
      email = str(request.form.get('email')).lower()
      passwd = request.form.get('password')

      print("WORKS",username, email, passwd)

      # we create a temporal  instance that can store the results from the validorex script  
      validated = Login_validator(username,email,passwd) 
      
     # now we can access the function since the instance has been set 
      if validated.validator():

         return render_template("index.html",post_variable=posts, login_username=username)

      else:
         return "invalid login"

   return "works"



     

if __name__ == '__main__':
   app.run(debug = True)