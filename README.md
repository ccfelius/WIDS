# Women in Data Science
Wids Datathon github for team Queen B (Refers to Blair Waldorf from GG)

### Install & fetch data from Kaggle for WIDS 2022

First thing to do: create an account on [Kaggle](http://www.kaggle.com). Once you've created an account open your terminal (in MacOS/Linux) and install the kaggle package by using pip:

```
pip install kaggle
```

If you get any errors after you installed, read the [webpage](https://www.kaggle.com/docs/api) of Kaggle. Essentially, you need to download a kaggle.json file on Kaggle and put it in the right folder.

The kaggle.json can be download if you go on Kaggle to Account > Create new API token > Download Kaggle.json

Subsequently go in your terminal to downloads

```
cd ~/.downloads
```

and move kaggle.json to the right folder 

```
mv kaggle.json ~/.kaggle
```

After this procedure, you should be good to go. The last thing you need to do is navigate to a folder where you want to put your WIDS 2022 data. You can navigate by the "change directory" (cd) command. So for example like:

```
cd ~/.documents/WIDS2022
```

Once in this folder, run the following command:

```
kaggle competitions download -c widsdatathon2022
```

Then unzip the downloaded .zip folder by using a command, e.g. unzip (works in MacOS)

```
unzip wids2022.zip
```

Now you should have the data locally on your computer, good luck!

### Installing Conda and other packages

Furthermore, try to install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). This is necessary for tensorflow (ML package) and jupyter notebooks. Some other packages that we'll probably use are [sklearn](https://www.bing.com/search?q=sklearn+&qs=n&form=QBRE&msbsrank=6_6__0&sp=-1&pq=sklearn+&sc=6-8&sk=&cvid=60BD5DAD0C6D44BFA710F1CCEF83827D) and [XGboost](https://xgboost.readthedocs.io/en/stable/install.html)

#### Some tips & tricks

You can create a new folder in your terminal by the make directory (mkdir) command. So e.g.:

```
mkdir wids
```

This will create a directory called 'wids'. Moreover, if you want to know what the path is of the current folder you're in you can use the print working directory (pwd) command. You use it by just typing:

```
pwd
```
