# AIA React-Native Sample App

## Introduction

The purpose of this app is to provide a basis for you to make a native app for this course. It features examples on how to fetch data from a server, interaction between screens, user inputs, and charts. This example has a companion python script that lunchs a server where you can get some metrics from your raspberry.

## Third Party libraries

The third party libraries that were installed in this project are as follow: [React-Native-Svg](https://github.com/react-native-community/react-native-svg), [React-Native-SVG-Charts](https://github.com/JesperLekland/react-native-svg-charts), and [React Navigation](https://reactnavigation.org/). 

If you use this project has a basis for your application, then you won't need to install them (if you need to use them), otherwise you will have to follow the instalation guides for each library.

### React-Native-SVG

This library provides components that render SVG elements, like a rectangles or lines. It is a requirement of React-Native-SVG-Charts

### React-Native-SVG-Charts

This library is used for plotting. It is basically a wrapper for the D3.js SVG charting library, a very powerfull and widely used charting library.

### React Navigation

This library is responsible for navigation between screens, enabling you to change the component that is being rendered.

## App overview and project structure

This app has two screens, one where you input your raspberry IP address and another where the CPU load, CPU temp, Memory consumed, and uptime are shown.

These two screens are called raspconnect (the initial screen) and statsscreen. 

When you create a React-Native app, the following resources are automatically created:

- android Folder - where all the native Android code is located;
- ios Folder - where all the native iOs code is located;
- node_modules Folder - where all the libraries need in this project are located, included the default ones.
- app.json - Json file containing the app name;
- App.js - The main JSX file, where the basis of your code is;
- index.js - File used by react-native to know what is you main file (default is App.js) and to export it.
- package.json -  Json file with all the dependencies and libraries used in this project.

To simplify and to organize all the components and logic of this app, a new folder called static was created. The following scheme is the structure of said folder:

	- Static
		- assets // folder with simplest components that are going to be called by others
			- square.js // js file that renders a square used to show each of the metrics fetch from the python server.
			- alltoghther.js //  js file where all the metrics are overlayed in a chart
		- components
			- columnleft.js //  a scrollView component calling two sqaure components
			- columnright.js // a scrollView component calling two square components
		- images // folder containing an image asset
		- screens
			- raspconnect // initial screen where the user can connect to a raspberry
			- statsscreen // componnet that displays the metrics served by the python script
			
			
The app flowchart is as follows:

	- Display the raspconnect screen
	- User inputs the IP of the raspberry
		- If IP is wrong then display an alert message
		- If IP is right, proceed to the statsscreen
			- Fetch from the Python server the metrics every second until the user disconnets or the connection is droped
			
As you can see, the app behaviour is very simple and this project should provide the basic tools enabling you to develop an app for your final project.

The following is a scheme of the relation between each JS file

	- App.js
		- raspconnect.js
		- statsscreen.js
			-columnLeft.js
				-square.js
			- columnRight.js
				-square.js
			- alltogether.js

Each file has the appropiate comments through the code. 
		
	
 
