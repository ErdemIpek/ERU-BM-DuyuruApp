
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](http://forthebadge.com)
<h1 align="center">
<img src="https://i.imgur.com/MCUb0Jq.png" width="250" height="250" align="center">
  <br>
 ERU-BM-DuyuruApp
</h1>
<br>
<p><font size="3">
This project is created for learning React Native basics. Use the menu links to jump between sections.  All of the code is under the <em>src</em> directory and free to use and contribute to.
  <h1 align="center">
  Available for Android
    <br>
    <img src="https://i.imgur.com/pEqrMEh.png"/>
  </h1>

# Mobile App
 - [Features](#features)
 - [Build Process](#build)
 
# Web Scrapper
- [Modules Used](#modules-used)
- [How does it work?](#how-does-it-work)

# API
- [Modules Used For API](#modules-used-for-api)
- [How does it work?](#how-does-it-work)

# Mobile App

## Features

* View recent announcements on three different websites.
* Click on the announcement to go to the announcement page.
* Pull to refresh the page.

## Build
* Follow the [React Native Guide](https://facebook.github.io/react-native/docs/getting-started.html) to get started.
* Clone or download the repo.
* `npm` to install dependencies.
* `react-native run-android` to run the app on the emulator.

# Web Scrapper

## How does it work
 For scrapping data from announcement pages, i choose to use beautifulsoup4. Basically it finds strings between or inside tags. Then i store the scrapped data in a database...
 
## Modules Used
*pymysql
*beautifulsoup
*urllib

# API

## How does it work
 I used flask to create an endpoint for mobile app.
## Modules Used For API
*flask
*pymysql
