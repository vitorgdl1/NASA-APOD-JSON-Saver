## NASA APOD JSON Saver
<hr>

### Purpose

This project's purpose is to provide a simple and fast way to save NASA API JSON APOD(Astronomy Picture of the Day).

### How To Use
This script is very simple to use. You will first need to download the library "requests".

To download this library, you use: ```pip install requests```

It is used to get API requests and be able to use the data.
After this, you only need an application to run your python script and execute it.
Or run ```python 'scriptnasa'.py```

The JSON file will be saved in whatever folder or directory your script is placed or executed. 

``{ 
  "copyright": "NSF\u00e2\u20ac\u201cDOE Vera C. Rubin Observatory/NOIRLab/SLAC/AURA\n Text: \nCecilia Chirenti \n(NASA\nGSFC, \nUMCP, \nCRESST II)",
  "date": "2026-08-07",
  "explanation": "There are more than half a million galaxies in the central panel of this image from the NSF-DOE Vera C. Rubin Observatory in Chile.   This is the COSMOS field, a patch of sky several times larger than the full moon, first observed by Hubble.   It has also been observed by Webb and other telescopes because it contains comparatively few bright stars from our own galaxy, offering a relatively unimpeded view of other galaxies outside the Milky Way.   The outer panels, numbered 1-10, show zoomed-in views of the corresponding small regions highlighted in the central panel.   The variety of galaxy shapes and sizes is astonishing.   Some of them are so far away that their light has traveled for billions of years before reaching Earth.   Rubin will come back every couple of days to the COSMOS field as part of its ten-year Legacy Survey of Space and Time.   It will allow a dynamic view of the COSMOS field and how the sky changes over time.",
  "hdurl": "https://apod.nasa.gov/apod/image/2608/noirlab2618b.jpg",
  "media_type": "image",
  "service_version": "v1",
  "title": "Rubin's COSMOS field",
  "url": "https://apod.nasa.gov/apod/image/2608/noirlab2618b_1024.jpg"
}
``
