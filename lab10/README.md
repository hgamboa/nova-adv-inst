# Pre Class setup

- Before class, go to [https://facebook.github.io/react-native/docs/getting-started.html](https://facebook.github.io/react-native/docs/getting-started.html) and follow the step-by-step guide to configure your computer. 

- Learn how to lunch a virtual device of your choice, either via the Android Emulator or via iPhone Simulator.

# React-Native 101

## Introduction

React-Native provides a simple way to create mobile apps, using "javascript" and "css". 

You can divide an app into smaller, reusable components. This components can be:
- Entire screens
- Part of the screens
- Customs small elements, like buttons or charts

The react philosophy is to create the lowest number of components and to reuse as many time as you can. Anything you see on the screen is some sort of component.

## Javascript to build apps?

Yes, well sorta of.

You construct the apps using what is called native components, javascript code that are "translated" into native code (e.g JS -> Java).

This native components include Buttons, Lists, Sliders, Switchs, Text, TextInputs, etc.

When you have

	return (
      	 <View>
          <Text>Hello world!</Text>
      	 </View>
    	);

react-native will "translate" this snippet that will display "Hello world!" on the device's screen, without the need to write any platform specific code. You can then combine multiple of these components to make custom ones and build your app.

## React-Native trinity

React-Native has three main basic concepts:
- Components
- Props
- State

The first concept is a Component. In React-Native you use components as building block to create your app. It is trough the use of components that React-Native translate your design to native applications.
For example, you can create a square component, that display some text.

	class Square extends Component {
	  render() {
	    return ( # Every component has to return a View
	      <View {{width:'100%', height:'100%', backgroundColor:'white'}}>
	      	Some text
	      </View>
	    );
	  }
	}

This component (which can be used in other components by calling < Square>) will display a square that has 100% of the height and the width, has a white background and displays "Some text". 

Now imagine that we want square with different heights. We need another concept, props. You use props to pass information between components, or in this case, use props to pass a different height to our < Square> component.

	class Square extends Component {
	  render() {
	    return ( # Every component has to return a View
	      <View {{width:'100%', height:this.props.height, backgroundColor:'white'}}>
	      	Some text
	      </View>
	    );
	  }
	}

	export default class LotsOfSquares extends Component {
	 render() {
	  return (
	   <View style={{alignItems: 'center'}}>
	    <Square height='20' />
	    <Square height='30' />
	    <Greeting height='50' />
	   </View>
	  );
	 }
	}

We modify our Square component to accept a height when we call it. In the LotsOfSquares component, we call three different squares, with 20, 30, and 50 pixels of height respectively. By using the height prop, we were able to draw three squares, each with a different height.

Finnaly we have state, another type of data used to control a components (with the other being props). Props, as seen before, are controlled by the parent and these are imutable during the lifetime of the component. For data that is going to change throught the component life, it is better to use state. In general, you should initialize state in the constructor, and then call setState when you want to change it.

For example, let's say we want to change the color of our square each second. To achive this, we can implement an interval (using the setInterval function) and set a state variable.

	class Square extends Component {
	  constructor () {
	      super();
	      this.state = {
	          redColot: False
	      };
	   
	   // Toggle the state every second
	   setInterval(() => {
	     this.setState(previousState => { // If you want to use the previous state as a variable (p.e to toggle between True and False)
	       redColot: !previousState.redColor };
	     });
	    }, 1000);
	  }
	  
	  render() {
	    let color = this.state.redColot ? 'Red': 'White ';
	    return ( 
	      <View {{width:'100%', height:this.props.height, backgroundColor:color}}>
	      	Some text
	      </View>
	    );
	  }
	}

In summary, you should use components to define reusable parts of code/views. To send data from a parent component to a child one, use props. To save data inside a component, you should use the state.

## Example of react-native built-in components

### View

The < View> component is the most fundamental and basic component for building a UI. It is the equivalent of using UIView on iOS, div on HMTL, android.view on Android, etc. Your custom components should always return a < View> with the rest of your custom UI inside of it.

### Text

The < Text> component is another very basic component, which allows you to display text on the screen. 

### TextInput

If you want the user to be able to input text on your app, then you should use the < TextInput> component, where you have to "listen" to the onChangeText event to catch what the user is writing.

### Button

As the name says, the < Button> component renders a button. However, this button has very little customization. 

### TouchableOpacity

If you want more control of the style or to use other components as buttons, you can wrap them in a < TouchableOpacity> component. On press down, the opacity of the wrapped view is decreased, dimming it, but you can disable this opacity.

### FlatList

To render a list, you can use the < FlatList> component.

### ScrollView

If you want a view to be scrollable (e.g the components height is larger than the device screen or you have a very big list), then use the < ScrollView>.

## Some quirks and features

Altough the code resembles normal javascript, what you are coding is javascript + xml (JSX). One quirk is how you pass props or variables to function inside the render method.

Typically you would write something like < View style="width: 50"> to create a view with a width of 50px. This in JSX will not get render, since you pass a string to the style prop and not an object.

What about < View style={width: 50} >? Well this is also wrong, since you do not have any object called width in your variables. 

The correct way is to write < View style={{width:50}} >, which is passing an object with a width key and value. If you want to use only a single bracket, you have to define the variable prior to call it.

Another quirk is the {(param1, ...) => statements } notation, also called an arrow function expression, which appear for example in the < TextInput> component

      <TextInput
        style={{height: 40, borderColor: 'gray', borderWidth: 1}}
        onChangeText={(text) => this.setState({text})}
        value={this.state.text}
      />
      
What the onChangeText prop is doing is "grabbing/subscribing" the text value of the TextInput and then injecting it in a function, this case the setState function.

## Import/Export business

If you want your component to be acessible outside the file your creating it, then you have to export it by simply adding the line **export default yourComponent**. This will allow other files to import your custom component and it to be used by other componets.

Importing components is also a usefull feature. 
	
	import { Text, View } from 'react-native';
	
What the snippet above does is importing the Text and View components from the 'react-native' library. 

But what if you want to import a component from another file? Well this is as simple as 

	import { the components you want } from 'fileYouWant';
	
You might also want to organize your components by folders. In this case is good pratice to create a index.js file inside the folder (like Python's _ _ init__ .py files) and inside this file import all the components from all the files and make a single export.

For example, image you have a folder called screens with two different components: screenA and ScreenB

	- MainScreen.js
	- Screens
		- ScreenA.js
		- ScreenB.js
		
You add a index.js file inside the Screen folder that looks similar to this:

	import ScreenA from './ScreenA' // Assuming that ScreenA.js exports a component called ScreenA
	import ScreenB from './ScreenB' // Assuming that ScreenB.js exports a component called ScreenB
	
	export {
		ScreenA,
		ScreenB
	}

Now you can import the ScreenA and ScreenB components to the MainScreen file using only one import line:

	// MainScreen.js
	
	import {ScreenA, ScreenB} from './Screens'
	
## Usefull link and resources

Inside of each folder there is a small readme.md file, explaining with more detail each project.

The react-native documentation: https://facebook.github.io/react-native/docs/getting-started

A simple crash course video you should check before class and follow along: https://www.youtube.com/watch?v=mkualZPRZCs
