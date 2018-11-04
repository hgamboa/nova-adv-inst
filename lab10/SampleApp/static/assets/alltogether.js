import React, {Component} from 'react';
import {View, Dimensions, Text} from 'react-native';

import {LineChart, XAxis } from 'react-native-svg-charts' // We want the LineChart and XAxis from the react-native-svg-chart
import * as shape from 'd3-shape' // We want all components from d3-shape and we want a pre-fix shape for all

import Svg,{Rect} from 'react-native-svg' // We want to import the SVG and the Rect component from react-native-svg


// In this file, we create the AllTogether component which will show the last 60 seconds of data for the CPU load, 
// memory usage, and the CPU temperature, all overlayed.
class AllTogether extends Component {
    constructor(){
        super();
        // Since we will have data incoming from the server, we want to save it in an array
        // in order to have historical data. In this case, we want to show the last 60 points
        // and we use an arrow function to initialize these arrays.
        this.state = {
            CPU:Array.from({length: 60}, () => 0),
            Memory:Array.from({length: 60}, () => 0),
            Temperature:Array.from({length: 60}, () => 0)
        }
    }
    // This function is responsible for updating the state for each metric
    update_data(point, type){
        data = this.state[type];
        if(data.length >= 60){
            data.shift()
        }
        data.push(point)
    }

    render(){
        // These three if statements protects our app from NaN values.
        if(isNaN(this.props.CPU)!=true){
            this.update_data(this.props.CPU, 'CPU')
        }

        if(isNaN(this.props.Memory.MemUsed)!=true){
            var memUsage = ((this.props.Memory.MemUsed/this.props.Memory.MemTotal) * 100)
            this.update_data(memUsage, 'Memory')
        }

        if(isNaN(this.props.Temperature)!=true){
            this.update_data(this.props.Temperature, 'Temperature')
        }
        const xArray = [60, 50, 40, 30, 20, 10, 0] // Simple array for displaying the correct labels.
        
        // This component as the following return structure
        // <View>
        //  <View> with 80% of the parents height
        //    3 <LineChart> overlayed and the <XAxis>
        //  <View> with the remaining 20% of the height
        //    3 <View> displaying the legend for the chart
        
        // As an exercise, you can try to create a component representing each of the legends and pass that component
        // instead of repeating the same code 3 times.
        
        return(
            <View style={{width:'100%', height:'100%'}}>
                <View style={{width:'100%', height:'80%'}}>
                    <LineChart
                        style={ {position: "absolute", width:'100%', height:'100%'} }
                        data={ this.state.CPU }
                        contentInset={ { top: 20, bottom: 20, left:20, right:20 } }
                        curve={shape.curveNatural}
                        yMin = {0}
                        yMax = {120}
                        svg={{
                            strokeWidth: 2,
                            stroke: 'yellow',
                        }}
                    />
                    <LineChart
                        style={ {position: "absolute", width:'100%', height:'100%'} }
                        data={ this.state.Memory }
                        contentInset={ { top: 20, bottom: 20, left:20, right:20 } }
                        curve={shape.curveNatural}
                        yMin = {0}
                        yMax = {120}
                        svg={{
                            strokeWidth: 2,
                            stroke: 'pink',
                        }}
                    />
                    <LineChart
                        style={ {position: "absolute", width:'100%', height:'100%'} }
                        data={ this.state.Temperature }
                        contentInset={ { top: 20, bottom: 20, left:20, right:20 } }
                        curve={shape.curveNatural}
                        yMin = {0}
                        yMax = {120}
                        svg={{
                            strokeWidth: 2,
                            stroke: 'white',
                        }}
                    />
                    <XAxis
                    data={ xArray}
                    svg={{
                        fill: 'black',
                        fontSize: 8,
                        fontWeight: 'bold',
                    }}
                    style={{ position: "absolute", width:'100%', height:'100%', top:'95%' }}
                    contentInset={ { top: 20, bottom: 20, left:20, right:20 } }
                    formatLabel={ (value, index) => xArray[index]+'s' }
                    
                    />
                </View>
                <View style={{width:'100%', height:'20%', flexDirection:'row'}}>
                    <View style={{width:'10%', height:'100%', flexDirection:"row"}}>
                    </View>
                    <View style={{width:'26.66%', height:'100%', flexDirection:"row"}}>
                        <View style={{width:'30%', height:'100%', alignItems:"center", justifyContent:"center"}}>
                            <Svg width="30" height="3"> 
                                <Rect
                                    x="0"
                                    y="0"
                                    width="30"
                                    height="3"
                                    fill="yellow"
                                />
                            </Svg>
                        </View>
                        <View style={{width:'70%', height:'100%', justifyContent:"center"}}>
                            <Text style={{textAlign: 'left', color: 'white', paddingLeft:10, fontSize:11}}>CPU</Text>
                        </View>
                    </View>
                    <View style={{width:'26.66%', height:'100%', flexDirection:"row"}}>
                        <View style={{width:'30%', height:'100%', alignItems:"center", justifyContent:"center"}}>
                            <Svg width="30" height="3"> 
                                <Rect
                                    x="0"
                                    y="0"
                                    width="30"
                                    height="3"
                                    fill="pink"
                                />
                            </Svg>
                        </View>
                        <View style={{width:'70%', height:'100%', justifyContent:"center"}}>
                            <Text style={{textAlign: 'left', color: 'white', paddingLeft:10, fontSize:11}}>Memory</Text>
                        </View>
                    </View>
                    <View style={{width:'26.66%', height:'100%', flexDirection:"row"}}>
                        <View style={{width:'30%', height:'100%', alignItems:"center", justifyContent:"center"}}>
                            <Svg width="30" height="3"> 
                                <Rect
                                    x="0"
                                    y="0"
                                    width="30"
                                    height="3"
                                    fill="white"
                                />
                            </Svg>
                        </View>
                        <View style={{width:'70%', height:'100%', justifyContent:"center"}}>
                            <Text style={{textAlign: 'left', color: 'white', paddingLeft:10, fontSize:11}}>Temperature</Text>
                        </View>
                    </View>
                    <View style={{width:'10%', height:'100%', flexDirection:"row"}}>
                    </View>
                </View>
            </View>
        )
    } 
}


export default AllTogether
