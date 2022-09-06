# Mission-to-Mars

# Background

Robin's web app is looking good and functioning well, but she wants to add more polish to it. She had been admiring images of Mars’s hemispheres online and realized that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, you’ll use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

# Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles

Step 1, use your browser to visit the Mars Hemispheres (Links to an external site.) website to view the hemisphere images.

![Mission-to-Mars Hemisphere](https://user-images.githubusercontent.com/107443962/188520939-aaa0239f-6afb-4d7b-9852-b4e37e069f55.png)

In Step 2, create a list to hold the .jpg image URL string and title for each hemisphere image.
In Step 3, write code to retrieve the full-resolution image URL and title for each hemisphere image. The full-resolution image will have the .jpg extension.

![hemisphere_image_urls](https://user-images.githubusercontent.com/107443962/188519820-7a67676a-aa84-4eef-bef1-0120c0458d53.png)

Loop through the full-resolution image URL, click the link, find the Sample image anchor tag, and get the href.

![Mission-to-Mars Planet](https://user-images.githubusercontent.com/107443962/188520517-7986b69e-238a-48d1-becc-fc5abc430a86.png)

Save the full-resolution image URL string as the value for the img_url key that will be stored in the dictionary you created from the Hint.
Save the hemisphere image title as the value for the title key that will be stored in the dictionary you created from the Hint.
Before getting the next image URL and title, add the dictionary with the image URL string and the hemisphere image title to the list you created in Step 2.
In Step 4, print the list of dictionary items. Your list should look like the following image:

![2](https://user-images.githubusercontent.com/107443962/188521738-39cdd35e-5427-4909-812e-252022b1f7c4.png)

### Cerberus Hemisphere Enhanced

![Cerberus](https://user-images.githubusercontent.com/107443962/188522034-a9baa884-ae5f-422a-923f-3cb319de08dc.jpg)

### Schiaparelli Hemisphere Enhanced

![Schiaparelli](https://user-images.githubusercontent.com/107443962/188522037-7dcc68f9-4519-4f68-b64a-abb6d55c7edb.jpg)


### Sytis Major Hemisphere Enhanced

![Sytis Major](https://user-images.githubusercontent.com/107443962/188522042-9023a884-f201-4bff-a4ff-5d46ac8d4fcd.jpg)


### Valles Marineris Hemisphere Enhanced

![Valles Marineris](https://user-images.githubusercontent.com/107443962/188522052-691d29c3-5867-4a4c-978f-6f802737fdcb.jpg)

# Deliverable 2 Requirements

Deliverable Requirements:
Using your Python and HTML skills, you’ll add the code you created in Deliverable 1 to your scraping.py file, update your Mongo database, and modify your index.html file so the webpage contains all the information you collected in this module as well as the full-resolution image and title for each hemisphere image

The scraping.py file contains code that retrieves the full-resolution image URL and title for each hemisphere image.
The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image.
The index.html file contains code that will display the full-resolution image URL and title for each hemisphere image.
After the scraping has been completed, the web app contains all the information from this module and the full-resolution images and titles for the four hemisphere images.
Results with detail analysis:
The scraping.py file contains code that retrieves the full-resolution image URL and title for each hemisphere image

![Mars Weather code](https://user-images.githubusercontent.com/107443962/188522543-8decf539-82d8-4e1b-bb14-3188623dcb31.png)


# Deliverable 3: Add Bootstrap 3 Components

For this part of the Challenge, update your web app to make it mobile-responsive, and add two additional Bootstrap 3 components to make it stand out.

![Mars weather](https://user-images.githubusercontent.com/107443962/188522530-b18d2a90-870b-4301-a678-f4898bae86a3.png)
