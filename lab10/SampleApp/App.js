/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {RaspConnect, ChartScreen} from './static/screens'; // Import both screens that will be used from the folder screens 
import { createSwitchNavigator } from 'react-navigation';

export default class App extends Component { 
  // Our main component. This component is exported inline, unlike some of the components of this project
  // Inside the render functions, we return a Router. This Router component is responsible by changing the screen that is rendered on the screen. It is imported from the react-navigation library.
  render() {
    return (
     <Router /> 
    );
  }
}
// This is where we define our routes, meaning where what component to call when we do a certain action or ask for that path.
// You can make the parallel with Web address. When you ask the browser for google.com, the browser knows what web site to render.
// In this case if you ask for the 'Config' screen, the router will render the RaspConnect component, while if you ask for the 'Dashboard', the router will render the StatsScreen component.

const Router = createSwitchNavigator(
  {
    chartPage: ChartScreen,
    Config: RaspConnect,
  },
  {
    initialRouteName: 'Config',
  }
);


