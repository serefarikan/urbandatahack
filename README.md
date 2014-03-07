urbandatahack
=============

Work from the urban data hackathon 

Important points:

1) This is  a single html page that is meant to run from your computer. Sorry, did not have time to build a web site for this. 

2) You need to get this repo to your disk and open testBing.html Then click LOAD on the right, and use show/clear buttons for any type of crime data you'd like to view

3) The html page uses  Bing Maps API and you'll see a warning in the middle of the map. To remove it, you need to get a Bing Maps API key (you can get it for free) from https://www.bingmapsportal.com/ It is really a nice api, so I suggest you check it out (Thanks Microsoft) Once you get the key, place it into testBing.html Look at the html file with notepad, the location you need to insert it is marked as "YOUR-BING-MAPS-API-KEY-GOES-HERE"

4) The crime location data comes from http://data.police.uk/ which is data released under open government licence. Many thanks to people who make data available to public. See http://www.nationalarchives.gov.uk/doc/open-government-licence/version/2/ for licencing terms of this data

The data from the data.police.uk web site is transformed into java script code which ends up in getlocs.js This transformation is done via some python code The python code is in ipython_REPL.py Simply go to data.police.uk download crime data and put all csv files into a directory. Then using the python code (in iPython for example) you can generate javascript code (written to test.txt by the python code) put that javascript code into getlocs.js and you're done. I've use only a limited amount of data, you can get a lot more and use the python code to turn it into jscript

5) Finaly, many, many thanks to Data Science London for organising such great events. See http://datasciencelondon.org/ and come join the next meeting. 



