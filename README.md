#FindMyParking.space

FindMyParking space is a marketplace portal that allows users to rent and lease parking spots. The app provides a marketplace for individuals and businesses to lease parking spots for visitors to rent, especially during crowded events in urban areas. One can think of the portal as Airbnb for parking spaces -- an interactive market where people with spare parking can sell their spaces for money to people looking for parking spots, particularly helpful for congested events. 

The app came out as a hackathon project and is currently being maintained by me. 

##Project Structure

The project has been split between two branches, where the `master` branch (made up of just static files) is deployed on GitHub pages. 

The `dev` branch contains the Flask source, which can be compiled to run on a server. 

##Running

You can run the Flask backend by installing all dependencies using `pip` and then installing a virtual environment (recommended) and then running

```bash
export FLASK_APP=hello.py
```

This should compile a production build of the app, suitable for deployment. 

If you want to run the development build for testing, you can change the export settings and run

```bash
export FLASK_ENV=development
```

To finally run the Flask app, you should run

```bash
flask run
```

The app should be live on port 5000, unless specified otherwise. 

## Contributing

Feel free to contribute by forking, pulling your own branch and initiating pull/merge requests. Hit me up on email if you have any queries!
