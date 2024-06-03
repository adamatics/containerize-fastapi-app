# Containerize and Deploy FastAPI App

This repository contains files that define a FastAPI app (`app.py`, `requirements.txt`, and the `templates` folder) and a containerfile (`containerfile`) that specifies the build steps to build a container image for the FastAPI app.

The app is quite simple and does not have a database attached. It has a landing page, from which there is a link to another page in the app which allows the user to add items to a To-Do list. The list is not saved between launches of the app, and items cannot be removed. You can experiment with the code in `app.py` to see if you can find a way to check or remove items from the list.

The following sections contain descriptions of the steps to build and deploy the containerized FastAPI app on AdaLab.

## Build the container image

First, open a terminal and make sure that the directory you are in, is the folder that the repository was cloned into. Then, from the terminal, build the container image with the below command:

```sh
docker build -t to-dos-list-app:1.0 -f containerfile .
```

The argument `-t to-dos-list-app:1.0` specifies the name and tag to use for the built container image, and you can specify it as you wish. The only requirement is that a container image with this name does not already exist on your local computer, as this will cause an error, and that the name follows the [Open Container Initiative (OCI) naming convention](https://github.com/containers/image/blob/main/docker/reference/regexp.go). 

The argument `-f containerfile` specifies the name of the containerfile if the containerfile is not named "Dockerfile", which is the default that the `docker build` command expects if the `-f` argument is not given.


## Add metadata

Once the container image building process is complete, you will have the container image available in your Lab on the AdaLab platform. One way to view the container image file is with this command in a terminal, which can be executed from any location:

```docker images```

Once the image has finished building, metadata needs to be added. This will make it easier for your colleagues to find your container image, and will also prepare the app defined by the container image to be deployed. After specifying the metadata, the publish button will push the container image, as well as the metadata, to a central storage location, making it available for deployment.

To add metadata, go to the AdaLab menu, then choose "Container Metadata", and click the "Add New" button.

Next, you simply wait a few minutes for the publishing process to complete. Click the **Refresh** button at the top of the Container Metadata page to check whether the publishing process finished. You can also watch the logs to follow along with the build process, or view them after the publishing process finished, by clicking on the triple dot menu on the right-hand side of your container image metadata entry.

## Deploy

Once the Container Metadata publishing process finished successfully, an option to deploy the container image as an app will appear in the triple dot menu for the Container Metadata entry. Click this to open a dialog box in which you can fill in the details about the app, such as the name you want it to have, and the URL the app will be available at. You can also specify other settings such as resource usage, environment variables, and the startup command. 

To make these links work, the **Strip Prefix** checkbox must be unchecked

The startup command can either be defined in the containerfile, or it can defined or overwritten in `Advanced Settings` when the app is deployed. If defining the startup command in the `Advanced Settings` when deploying the app, it needs to be of the following format:

`gunicorn -k uvicorn.workers.UvicornWorker -b 0.0.0.0:5000 app:app`


The app deployment takes less than a minute. To check the status of the deployment, you can click the **Refresh** button. You can also follow along in the deployment process by clicking the triple dot menu on the right-hand side of your app entry, and clicking "View Logs". Once the app has finished deploying, you can click on its entry under the "App Deployment" menu item to go to your new app

