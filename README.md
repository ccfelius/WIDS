# Women in Data Science
Wids Datathon github for team ???

### Install & fetch data from Kaggle for WIDS 2022

Create a kaggle account, in your terminal, type:

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


#### Some tips & tricks

You can create a new folder in your terminal by the make directory (mkdir) command. So e.g.:

```
mkdir wids
```

This will create a directory called 'wids'. Moreover, if you want to know what the path is of the current folder you're in you can use the print working directory (pwd) command. You use it by just typing:

```
pwd
```
