import React, {Component} from 'react';
import {FlatList} from 'react-native';

import {Square} from '../assets' // This component used the Square component created before

// This component is responsible by handling the CPU load and CPU temperature  metrics. It will call two Square components and display them inside a FlatList
// This component has one prop:
//   - data - The data used in this component
class StatsColumnRight extends Component {
    render(){
        // This component will return two Squares, with different colors and different height
        return(
            <FlatList
            style={{width:'50%', height:'100%'}}
            data={[
                {key:'CPU', height: 300, color:'#9d44b5', lastPoint: this.props.data.CPU}, 
                {key:'Temperature', height: 130, color:'#badefc', lastPoint: this.props.data.Temperature}
            ]}
            renderItem={({item}) => <Square title={item.key} height={item.height} color={item.color} lastPoint={item.lastPoint}/>}
            />
        )
    }
}

export default StatsColumnRight
