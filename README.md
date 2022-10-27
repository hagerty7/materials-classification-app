# Materials Classification Demo
## Getting Started
1. Go-to Google Colab and sign-in to a gmail account (for more about google colab please see: https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c)
2. Create a new notebook
3. Run the following command in cell 1, and allow the notebook to have access to your google drive:
```
from google.colab import drive
drive.mount('/content/drive')
```
4. in cell 2 of your notebook run the following command:
```
! mkdir -p /content/drive/MyDrive/GitHub
%cd 
```
5. Obtain a Person Access Token (PAT) from your GitHub account to use as you password in the next step (for more about PATs in GitHub please see: https://emilyriederer.github.io/projmgr/articles/github-pat.html#:~:text=Getting%20a%20PAT%201%20Go%20to%20GitHub%202,very%20much.%208%20Choose%20Generate%20token%20More%20items). Don't forget to copy/paste and save this somewhere you won't forget (i.e. stick note on your desktop if you're a windows user).
6. in cell 3 of your notebook run the following command:
```
import os
from getpass import getpass
user = getpass('GitHub User')
password = getpass('GitHub Password')
os.environ['GITHUB_AUTH'] = user + ':' + password
!git clone https://$GITHUB_AUTH@github.com/ResourceRecyclingSystems/datacore-materials-classification-demo.git
```
7. You should now have this repo cloned into your colab environment, please move on to the next heading on how to run the ngrok streamlit demo (if not reach out to Joe Hagerty joe.hagerty12@gmail.com for support). See the following for what you should see in Google Colab:

![GitHub Repo]('./pic/colab-menu-repo.png')

## Running the ngrok streamlit demo
1. Open your Google Drive that you signed into earlier and open the GitHub directory containing your cloned repo from earlier.
2. Open the datacore-materials-calssification-demo repo and right-click materials_classification_demo.ipynb and hover over "Open with" and click "Google Colaboratory" to open the notebook in Google Colab. See the following for what you should see in Google Drive:

![Open materials_classification_demo.ipynb]('./pic/open-notebook-colab-from-drive.png')

3. Before running the notebook, go to https://ngrok.com and signup for the free service. 
![Sign-up for ngrok]('./pic/ngrok-signup.png')

Once signed-up, login to your ngrok account, and got to the "Your Authtoken" menu item under the "Getting Started" menu header. See "Your Authtoken" in the page and copy the authtoken, you will need this when running ngrok in the materials_classification_demo.ipynb. See the following for what you should see at ngrok.com:

![Copy ngrok Authtoken]('./pic/ngrok-authtoken.png')

4. Return to the materials_classification_demo.ipynb and Run All, under the "Runtime" menu. Also allow the notebooks to "Connect to Google Drive". See the following for what you should see when running the notebook:

![Run All in notebook]('./pic/colab-run-all.png')

5. You will be prompted to add your ngrok Authtoken, go ahead paste that into the input prompt and hit enter. See the following for what you should see when adding your Authtoken:

![Enter ngrok Authtoken to notebook]('./pic/colab-ngrok-authtoken.png')

6. Once the streamlit app tunnels you can accesss app provided in print output of cell 9. See the following as an example of that output will look similar to, the link that is highlighted is what you will click to go to the app. Also, you will be prompted by ngrok to launch the app, Accept that prompt.

![Click on the hgrok link]('./pic/colab-ngrok-link.png')

7. You should now have access to the app. If you have any issues please reach out to Joe Hagerty at joe.hagerty12@gmail.com. See the following as a reference to the streamlit app:

![Streamlit app]('./pic/streamlit-app')

## Huggingface Space
Huggingface space is [here](https://huggingface.co/hagerty7/recyclable-materials-classification).

## Huggingface Model Card
Huggingface model card is [here](https://huggingface.co/hagerty7/recyclable-materials-classification/tree/main).

## Resource Links

[vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k)
[An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)