IVLE-Downloader
===============

NUS IVLE Downloader

This project was inspired from Yao Yujian's project http://yjyao.com/2012/08/nus-ivle-downloader.html.
These modules can be used to download all files from IVLE, nicely arranged by their module codes, workbin names (if there are more than one), folders and subfolders.
I build this as an exercise to learn python.

Required Dependencies:
<ul>
  <li> Python 2.7 </li>
  <li> Python requests module, http://docs.python-requests.org/en/latest/ </li>
</ul>

To use:
<ol>
  <li> Download all files in src</li>
  <li> Copy / rename config.template.py to config.py
  <li> Change filepath in config.py to your own output folder (the directory used here will act as a root directory)  </li>
  <li> Run the downloader by: <code> python downloader.py </code> </li>
  <li> The program may ask for authentication for the first time, key in your NUSNET ID and password. </li>
  <li> Enjoy, and see all the files downloaded nicely. </li>
