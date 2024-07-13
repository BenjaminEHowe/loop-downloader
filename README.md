West Midlands Railway's WiFi service no longer includes magazines or other entertainment. It is now powered by Icomera.

# loop-downloader
A tool which downloads magazines from "The Loop" (an infotainment portal available on train services operated by London Northwestern Railway and West Midlands Railway) for offline reading later. Just connect to the WiFi, "sign in" using your email address, and run the script. As the content is hosted locally on the train, your downloads should complete in a matter of minutes. Downloaded magazines will be placed in individual folders within the folder the script is run from, with each page saved as a JPG image.

Sample terminal output:

```
ben@ben-x240:~$ python3 loop-downloader.py 
Downloading BBC Good Food magazine: page 155 of 155
Downloading Cosmopolitan magazine: page 140 of 140
Downloading FourFourTwo magazine: page 116 of 116
Downloading Imagination - English magazine: page 85 of 85
Downloading Shortlist magazine: page 45 of 45
Downloading Stylist magazine: page 56 of 56
Downloading Time Out London magazine: page 72 of 72
Downloading Top Gear magazine: page 164 of 164
```

The use of a tool such as this in order to copy content is expressly permitted by the [terms of use](https://www.londonnorthwesternrailway.co.uk/travel-information/onboard-facilities/loop-wifi-entertainment), provided that the copy is for personal use and is not modified.

## Potential future improvements

- [ ] Detection of network state (not connected, connected but sign-in requred, connected).
- [ ] Download of other content (e.g. films).
- [ ] Compatability with other infotainment portals operated by [GoMedia](http://www.gomedia.io/) (e.g. [BEAM on Virgin Trains](https://www.virgintrains.co.uk/experience/beam), [VUER on National Express coaches](http://www.nationalexpress.com/vuer.aspx), [VISTA on c2c](https://www.c2c-online.co.uk/travelling-with-us/onboard/free-onboard-wifi-and-entertainment/), [Extream on Transpennine Express](https://www.tpexpress.co.uk/travelling-with-us/train-wifi-and-entertainment), [Connect on Greater Anglia (coming soon)](https://www.greateranglia.co.uk/travel-information/your-journey/wifi), etc.).
