# project11_pur_beurre_better

Program developed and deployed by Jean-François Subrini, July 2018.



## What the project is for ?

* **Pur Beurre** website allows you to find a substitute healthy food to your junk food !
* Food quality is based on the nutriscore, with all the data from the [Open Food Facts](https://fr.openfoodfacts.org) open source database.
* The user enters the name and the brand of the food to substitute. The website find a list of substitute foods from the same category and with a better [nutriscore](https://fr.openfoodfacts.org/score-nutritionnel-france).
* Cliking on each substitute food the user can have more information about it.
* If registered and signed in, the user can save the healthy products found in the substitute list and then consult his selection. Each selected food can also be deleted.
* In this version of the website, the user can also select one food *category* and get as a response substitute healthy foods with a *A or B nutriscore*.
* In this version of the website, the user can also *change his/her password*.


## How to use it or get it running ?

* Pur Beurre is a **Python website**, developed with the **Django** framework 2.0, Python 3.6 and PostgreSQL for the backend (see *requirements.txt*), and with a Creative Bootstrap Theme for the frontend.

* You can access the program from your Terminal executing *./manage.py runserver* and watching it from your *localhost:8000* in your favorite browser.

* You can also and more easily go directly online at the **IP address of the DigitalOcean server : to be completed...**. On this site, **the database is updated every week**. A cron job is running at midnight on Sunday morning.


## How to update the category list and food data if running this app with localhost ?

* Pur Beurre has been developped with 20 different categories of food. See the name of these categories in the **CATEGORIES_LIST** (*pur_beurre/food/constants.py*). If you want to change it - add some more or drop ones - just modify that list before running an update. 

* If you change the CATEGORIES_LIST or just want to **update your database** with the latest food data, you need to run this command from your command line : ***./manage.py off_api***.


***Enjoy it !***