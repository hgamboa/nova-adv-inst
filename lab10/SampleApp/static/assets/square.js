import React, {Component} from 'react';
import {View, Text, TouchableOpacity, Alert} from 'react-native';

import { ProgressCircle, LineChart, YAxis } from 'react-native-svg-charts' // We want the ProgressCircle, LineChart and YAxis from the react-native-svg-chart
import * as shape from 'd3-shape'  // We want all components from d3-shape and we want a pre-fix shape for all

// In this file, we create the Square component which has three different returns:
// - If the incoming data is uptime, just display the number
// - If the incoming data if CPU temp, display both the temperature and a chart with the last 20 seconds
// - If the incoming data if either CPU load or Memory, display the used percentage, an arched progress bar, and a chart with the last 20 seconds.
//
// This component has four props:
//   - title     - The Square title
//   - height    - The Square height
//   - color     - The Square background color
//   - lastPoint - The incoming data point
class Square extends Component {
    constructor(){
        super();
        // Since we will have to make a historical chart for some of the metrics, we need to save the incoming values.
        this.state = {
            data:[50]
        }
    }
    // When we press the value, we alert the user with it.
    onPress(Box){
        if(Box!='Up Time' && Box!='Temperature'){
            Alert.alert(Box, String(this.props.lastPoint.toFixed(2)) +'%')
        } else if(Box=='Temperature'){
            Alert.alert(Box, String(this.props.lastPoint.toFixed(2)) +'ºC')
        } else {
            Alert.alert(Box, String(this.props.lastPoint))
        }
        
    }
    // This fuction will append the incoming data to the state
    update_data(point){
        data = this.state.data;
        if(data.length >= 20){
            data.shift()
        }
        data.push(point)
    }

    render(){
        const headingSize = 30;
        const borderWindthSize = 2
        // Calculate the height of the chart based on the incoming height.
        const graphSize = this.props.height-headingSize-borderWindthSize
        
        if(isNaN(this.props.lastPoint)!=true){
            this.update_data(this.props.lastPoint)
        }
        
        // In this components, the height of the view returned is based on the height prop, which is defined when these component is called from another.
        // This enables us to create squares or rectangules with different heights
        // As mentioned in the beggining of the file, the rendered content is based on which metric is incoming
        return(
            <View style={{width:'100%', height:this.props.height, backgroundColor:this.props.color, borderColor:'black', borderWidth:borderWindthSize, borderTopWidth:0}}>
                <View style={{width:'100%', height:headingSize, justifyContent:"center"}}>
                    <Text style={{color:'white', opacity:0.8, textAlign:"center", fontWeight:'bold', fontSize:17}}>
                        {this.props.title}
                    </Text>
                </View>
                <TouchableOpacity 
                    activeOpacity = { .9}
					style={{width:'100%', height:graphSize}}
                    onPress={() => this.onPress(this.props.title, this.props.lastPoint)}
                    >
                    {renderIf(this.props.title, graphSize, this.props.lastPoint, this.state.data)}
                    
                </TouchableOpacity>
            </View>
        )
    }
}
// This is the function with the render logic, which is based on the incoming data

function renderIf(key, graphSize, lastPoint, data_array) {
    if (key!='Up Time' && key!='Temperature') {
        return (
            <View style={{width:'100%', height:'100%'}} >
                <View style={{width:'100%', height:'60%', alignContent:'center', justifyContent:'center'}} >
                    <ProgressCircle
                        style={ {height: '90%' } }
                        progress={ lastPoint/100 }
                        progressColor={'rgb(134, 65, 244)'}
                        startAngle={ -Math.PI * 0.8 }
                        endAngle={ Math.PI * 0.8 }
                        strokeWidth={20}
                        cornerRadius={0}
                    />
                    <Text style={{
                        position: "absolute", 
                        alignSelf: 'center',
                        fontSize:20, 
                        top: ((graphSize*0.6)/2)-(20*0.9)}}
                        >
                            {lastPoint.toFixed(2) + '%'}
                        </Text>
                </View>
                <View style={{color:'black', width:'95%', height:'40%', alignSelf:'center', justifyContent:"center", flexDirection: 'row'}} >
                    <YAxis
                        data={ data_array }
                        contentInset={ { top: 10, bottom: 10}}
                        svg={{
                            fill: 'white',
                            fontSize: 10,
                        }}
                        numberOfTicks={ 3 }
                        min={0}
                        max={100}
                        formatLabel={ value => `${value}%` }
                    />
                    <LineChart
                        style={ { flex: 1, opacity:0.5  } }
                        data={ data_array }
                        contentInset={{ top: 10, bottom: 10} }
                        curve={shape.curveNatural}
                        yMin = {0}
                        yMax = {100}
                        svg={{
                            strokeWidth: 2,
                            stroke: 'white',
                        }}
                        />
                </View>
            </View>
            
        );
    } else if (key=='Temperature'){
        return(
            <View style={{width:'100%', height:'100%'}}>
                <View style={{width:'95%', height:'100%', alignSelf:'center', justifyContent:"center", opacity:0.5, flexDirection: 'row'}} >
                    <YAxis
                        data={ data_array }
                        contentInset={ { top: 10, bottom: 10}}
                        svg={{
                            fill: 'black',
                            fontSize: 10,
                        }}
                        numberOfTicks={ 3 }
                        min={0}
                        max={120}
                        formatLabel={ value => `${value}ºC` }
                    />
                    <LineChart
                        style={ { flex: 1  } }
                        data={ data_array }
                        contentInset={ { top: 10, bottom: 10, left:5}}
                        curve={shape.curveNatural}
                        yMin = {0}
                        yMax = {120}
                        svg={{
                            strokeWidth: 2,
                            stroke: 'white',
                        }}
                    />
                </View>
                <Text style={{
                    position: "absolute", 
                    alignSelf: 'center',
                    fontSize:20,  
                    top: (graphSize/2)-20}}
                    >
                        {lastPoint +'ºC'}
                </Text>
            </View>
        )
    } else {
        return (
        <View style={{width:'100%', height:'100%'}}>
            <Text style={{
                color:'white',
                position: "absolute",
                alignSelf: 'center',
                fontSize:20, 
                top: (graphSize/2)-20}}>
                {lastPoint}
            </Text>
        </View>);
    }
}

export default Square
