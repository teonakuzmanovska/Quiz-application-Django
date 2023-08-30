# Quiz-application-Django


This is a miniature Django quiz application. It contains step by step commits which will guide you in the process of quiz creation and deploying the application on Heroku.
As of 2022, Heroku is no longer free, which is why the application is now deployed on Azure. The application is light, which is why there is no need for postgres database server.

## Steps for deploying apps on Azure:
1. Open the project in VS Code
2. Add Azure Tools in the extensions
3. Open the new Azure button on the left side
   3.1. Log in to Azure through VS Code (sign up first if you don't have an account)
   3.2. Right click on App Services
     3.2.1. Create new web app
     3.2.2. Enter desired unique app name
     3.2.3. Select runtime stack (your project's python version)
     3.2.4. Select Free tier
  4. Skip deploying in this step, we will deploy later
  5. In your newly created app > Application Settings, add SCM_DO_BUILD_DURING_DEPLOYMENT setting with value 1 (if it isn't added already)
4. In settings.py file in your project:
   4.1. Set DEBUG = False
   4.2. Add your newly created app's link to ALLOWED_HOSTS
5. Go back to Azure section
   5.1. Right click on newly created app > Deploy Web app
   5.2. Click "Yes" to always deploy pop up


Note: If you are deploying the application for the first time (unlike me who had it deployed to Heroku first), open the commits and follow the steps for installing waitress or simply:
- Add whitenoise to requirements.txt
- Add `'whitenoise.middleware.WhiteNoiseMiddleware'` to MIDDLEWARE in settings.py
- Add `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` and `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'` at the end of settings.py

Here is a [link](https://youtu.be/D6Wyk9q2JM0?si=7VeIHCSgv3oIRETk) to youtube video with steps for deploying Django application to Azure.
