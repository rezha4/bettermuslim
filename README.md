# BETTER MUSLIM
#### Video Demo:  <>
#### Description:  
What it is: Better Muslim is a web app, where people can learn about Islam, make to do lists, and make donations.

Abstract: By deeply understanding these 5 pillars, a muslim will be encouraged to be consistent in establishing it, and also encouraged to deep dive into the sea of Islamic teaching, about how to become a complete human being. Which contributes positively from their smallest circles (family and friends), to their widest (society, up to the whole-world).

#### This web app includes:
#### Resources: this will teach you the 5 pillars of Islam, as well as how to learn Islam the correct way.
Inside templates/resources.html you will find that this is a card element from bootstrap. Still trying to figure out how to better it, especially visual side of it.

#### To Do Lists: you can make your own list. Also, after completing each lesson, you will have a new item corresponding with what you learned.
This simple to do list app uses sqlite database that links with the users table. It adds items depending whose user id that are currently logged in. It then prints out the rows of todolist table with jinja for loop syntax.
I also added delete button to permanently DELETE the said item from todolist.
I will try to improve this to better use the status column, in which 0 is the 1st state of the item, 1 is when the item is done and 2 is when the item is deleted (Jinja then only rolls out items that are less than 2).

#### Donation Center: donate to the needy, those affected in war/conflict, poverty, disasters
Using users, on column cash, I make a top up button in which users can easily add their desired amount of cash. They can then spend it on several causes that are acted toward donations on countries that are facing disasters or conflicts.
A missing feature is a flashing message, on which this feature also missed in most of my pages, this will be my homework to better make the Better Muslim web app better!