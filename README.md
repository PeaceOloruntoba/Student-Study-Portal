Developed by Peace Oloruntoba aka Prof Prince Peace
you can contact me on whatsapp and phone call @+2348166846226
email @ profprincepeace@gmail.com or peascainc@gmail.com
social media @ Peace Oloruntoba or PeaceOloruntoba including LinkedIn, Facebook, Twitter, etc.

copyright 2022.

Django modules required for the projects include:
Django itself,
Youtube search
Wikipedia Search
google apis (for book search)
English dictionary (from django library), etc.

Python VirtualEnv Explained:

    - Install command: pip install virtualenv
    - How to use:

        1. Within your project directory in your local copy of your project's repository,
        run the following command "virtualenv 'env_name'". Your virtual environment folder should now be located in your local repo.

        2. Before installing any packages, you need to activate your virtual environment in order to encapsulate them and keep to them to   be specifically used within your project. Use the following command (whilst located inside your project directory): env\Scripts\activate

        3. Now that the virtual environment has been activated, you can install your packages.

        4. To deactivate the virtual environment at any time. Use the following command: deactivate.

    Note 1: I have included a requirements.txt file within your project so you can easily install all packages from there using the following command: pip install -r requirments.txt

    Note 2: If you're ever going to update said requirments.txt file, you should use the following command: pip freeze > requirements.txt

    Conclusion: I really hopes this helps you out. I know theres a dedicated built in way of handing python virtual environments but this way I found it easier to explain. Also just to finish. The 'env' (virtual environment) has been added to the .gitignore. We never push up the environment files to our repo as they are really only needed locally for reasons stated above (ecapsulation so as to not affect our entire machine). Plus it would just lead to a build up of cruft within your remote repo. Hope this help!! Delete this message from your readme when your comfortable with everything!



