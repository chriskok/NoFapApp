# NoFapApp
The app that will attempt to stop your masturbation habit by being annoyingly intrusive

## Installation
- Download and extract models folder in the current directory: https://drive.google.com/open?id=1CZuylfYvVpIv9CtzqjijuWIkCgSGz0zk
- Install NudeNet:
```
pip install nudenet
or
pip install git+https://github.com/bedapudi6788/NudeNet
```

## Usage
```
python NoFapApp.py
```

## Developer Notes
- Bible verses are taken randomly from t_asv.csv (dataset of bible verses from the American Standard-ASV1901 (ASV) Bible). Currently taken just from the book of Genesis - cause why not? 
- Currently waiting 3 seconds between each time we classify (just to give users some time to close their naughty windows).
- WORKS ON HENTAI! Don't ask how I know. 

## Issues
- Can easily Alt+Tab out of the window. Need to make it come to focus automatically.
- No way to stop distributable exe file currently other than manually through Task Manager.
- Multiple screens.
- Porn too dark or small to categorize -> potentially running the classifier on multiple smaller parts of the screen or using the more complex object localization technique with NudeNet.
- Sound will still be on.
- Mac/Linux users? 
- Testing tempts developers. 
- Surprisingly difficult to find ways to make app more annoying and obstructive.
- Also difficult to find scientific research papers on what turns people off.

## Credits
- Huge thanks to [Bedapudi Praneeth's NSFW Classification Project](https://github.com/bedapudi6788/NudeNet), the app is largely building upon the work he's done to effectively classify nudity with an ensemble of neural networks.
- Bible dataset taken from [Oswin Hartono's Kaggle Dataset Contribution](https://www.kaggle.com/oswinrh/bible), all documentation on how it's structured is on the kaggle entry. 