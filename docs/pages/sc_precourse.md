# Pre-course Activities

While it is possible to simply listen to the lecturers in the short 
course, we think that this is a far better learning experience if 
you are able to follow along with the examples. And for this we recommend the following:

## Software Installation

[**Please sign up for an Earthscope account**](https://data-idm.unavco.org/user/profile/login)


**Check out the slack channel**

This will be the main avenue used for asking questions.

**Please install the gnssrefl software.**

We have [installation instructions](https://gnssrefl.readthedocs.io/en/latest/pages/README_install.html) 
for three different ways to access our code. 

- The github or pypi install requires you are running linux and 
have python 3.8+ on your system and feel comfortable
installing python packages.  

- Dockers. PC users should use this path, but it is also a good way 
for mac and linux users that don't want to install python and/or 
manage dependencies or environment variables.

- Jupyter notebooks. This is another great way for people that are unfamiliar 
with python to access the code. The examples are given as tutorials.

**Check your environment variables**

Direct installers (github/pypi) need to set environment variables. In a terminal window, you should
check that they are active by typing these commands:

<code>printenv REFL_CODE</code>

<code>printenv EXE</code>

If nothing comes back, you haven't set them. **They have to be set every time you run the code.**
That is why we recommend you put them in your .bashrc file.


[More on environment variables and file formats](https://gnssrefl.readthedocs.io/en/latest/pages/README_install.html#environment-variables)

## Running the Code 

**Getting Started: Translate a Single GNSS File**

For github, pypi, and docker users, type in a terminal window:

<code>rinex2snr p038 2022 90 -orb rapid</code>

On my machine this returns:

<pre>
SUCCESS: SNR file was created 
/Users/kristine/Documents/Research/2023/snr/p038/p0380900.23.snr66
</pre>

This file was created using:

- a rapid GNSS orbit at GFZ
- GNSS data from EarthScope

If we knew we only wanted to look at GPS signals, we could have typed:

<code>rinex2snr p038 2022 90</code>

If you have any trouble with this command or do not have an Earthscope account, please try:

<code>rinex2snr p038 2022 90 -orb rapid -archive sopac</code>

**Next Step: Look at the reflection data for a single GNSS station**

<code>quickLook</code> is a valuable tool for assesing a GNSS-IR site. We will start by using the 
simplest request, which evaluates L1 GPS data using a standard azimuth/elevation angle mask:

<code>quickLook p038 2022 90</code>

This creates two png files. If you are using a direct github/pypi install, they will come to the screen.

<img src="../_static/p038-2.png">
<img src="../_static/p038-1.png">

If you are using a docker, the png files will **not** come to the screen but 
will be stored. 

For example, on my machine the docker said the file was saved here:

<pre>
/etc/gnssrefl/refl_code/Files/p038/quickLook_lsp.png
</pre>

But as I was running the docker from /Users/kristine/docker_friday, I should view 
it from 

<pre>
/Users/kristine/docker_friday/refl_code/Files/p038/quickLook_lsp.png
</pre>

If you are able to download and translate a GNSS file and 
run <code>quickLook</code>, you are doing great.
While we mostly used the defaults, we want to emphasize that there are options 
to both of these codes.


- [rinex2snr](https://gnssrefl.readthedocs.io/en/latest/api/gnssrefl.rinex2snr_cl.html)

- [quickLook](https://gnssrefl.readthedocs.io/en/latest/api/gnssrefl.quickLook_cl.html)

If you have the docker running or you have your virtual environment up, you can type <code>-h</code>
for some help, i.e.

<code>rinex2nsr -h</code>


## Understanding what the GNSS-IR Output is telling you.

You should read [the overview documentation](https://gnssrefl.readthedocs.io/en/latest/pages/understand.html)

And then the [quickLook documentation](https://gnssrefl.readthedocs.io/en/latest/pages/quickLook.html).

What do we mean when we say "reflector height"? You need to know that before the next section.
What happens when you change the inputs to quickLook? (h1, h2, e1, e2). Try using different 
frequencies. Since we used the rapid multi-GNSS orbit from GFZ, we have access to GPS, Glonass,
and Galileo signals. [You can check here to remind yourself how the frequencies are named in this software](https://gnssrefl.readthedocs.io/en/latest/pages/file_structure.html)

**What is a Reflection Zone**

[Watch this video](https://www.youtube.com/watch?v=sygZMeCHHDg&t=23s)

Use the [refl_zones web site](https://gnss-reflections.org/rzones) to try and pick 
reflection zones for station [ross](http://gnss-reflections.org/geoid?station=ross) 
that was used in the examples. Should you use the default
sea level reflector height (RH) or should you pick one? And if so, what value should you use?
From the picture, what value do you think is reasonable?


Try to pick reflection zones for station [sc02](http://gnss-reflections.org/geoid?station=sc02). 
Is it reasonable to use the mean sea level RH option in https://gnss-reflections.org/rzones ?

## Additional Assignments

We have some students who are taking this virtual course for university credit. And others 
might be interested to get an early start with the software. If you are in either of these 
categories, please work on one or more use cases:

The main module for estimating reflector height is 
called [gnssir](https://gnssrefl.readthedocs.io/en/latest/pages/gnssir.html).
Try out one of [our examples](https://gnssrefl.readthedocs.io/en/latest/pages/first_drivethru.html). 

If you are primarily interested in water levels, you should start with a lake. 

If you are primarily interested in snow accumulation, you should start with an ice sheet.  
