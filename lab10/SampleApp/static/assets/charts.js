import React, {Component} from 'react';
import {View, Dimensions, Text} from 'react-native';

import {LineChart, XAxis, YAxis} from 'react-native-svg-charts' // We want the LineChart and XAxis from the react-native-svg-chart
import * as shape from 'd3-shape' // We want all components from d3-shape and we want a pre-fix shape for all

import Svg,{Line} from 'react-native-svg' // We want to import the SVG and the Rect component from react-native-svg


// In this file, we create the AllTogether component which will show the last 60 seconds of data for the CPU load, 
// memory usage, and the CPU temperature, all overlayed.
class Charts extends Component {
    constructor(){
        super();
        // Since we will have data incoming from the server, we want to save it in an array
        // in order to have historical data. In this case, we want to show the last 60 points
        // and we use an arrow function to initialize these arrays.
        this.state = {
            Data:Array.from({length: 60}, () => 0),
        }
    }
    // This function is responsible for updating the state for each metric
    update_data(point){
        data = this.state['Data'];
        if(data.length >= 60){
            data.shift()
        }
        data.push(point)
    }
    render(){
        // This if statements protects our app from NaN values.
        if(isNaN(this.props.incomingData)!=true){
            this.update_data(this.props.incomingData)
        }
        var xArray = [60, 50, 40, 30, 20, 10, 0]
        var yArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return(
            <View style={{width: this.props.width, height:this.props.height, padding: 20}}>
                <View style={{flex:1, height: this.props.height-20, flexDirection: 'row'}} >
                    <YAxis
                        data = {yArray}
                        contentInset = {{ top: 20, bottom: 20  }}
                        svg = {{
                            fill:'black',
                            fontsize: 8,
                            fontWeight: 'bold'
                        }}
                        numberOfTicks = {10}
                        formatLabel = { value => value }
                    />
                    <LineChart
                        style={ {flex: 1}}
                        data = {this.state.Data}
                        contentInset={ { top: 20, bottom: 20 }  }
                        curve={shape.curveBasisOpen}
                        yMin = {0}
                        yMax = {11}
                        svg={{
                            strokeWidth:2,
                            stroke:'red'
                        }}
                    />
                </View>
                <View style={{height:20}} >
                    <XAxis 
                        data={xArray}
                        svg = {{
                            fill: 'black',
                            fontSize: 8,
                            fontWeight: 'bold'
                        }}
                        style={{marginLeft: 30, width: this.props.width - 40 - 30}}
                        contentInset={ {left:8, right:8  }  }
                        formatLabel={ (value, index) => xArray[index]+'s'  }
                    />
                </View>
                <View style={{position: 'absolute', height: '100%', width: '100%'}} >
                    <Svg height={this.props.height} width={this.props.width}>
                            <Line x1='38' y1='30' x2='38' y2={this.props.height-42} stroke='black' strokeWidth='2' />
                            <Line x1='38' y1={this.props.height - 42} x2={this.props.width-20} y2={this.props.height - 42} stroke='black' strokeWidth='2' /> 
                    </Svg>
                </View>
            </View>
        )
    } 
}


export default Charts
