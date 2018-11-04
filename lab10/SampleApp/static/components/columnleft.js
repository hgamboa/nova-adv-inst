import React, {Component} from 'react';
import {FlatList} from 'react-native'; 

import {Square} from '../assets' // This component used the Square component created before

// This component is responsible by handling the uptime and memory metrics. It will call two Square components and display them inside a FlatList
// This component has one prop:
//   - data - The data used in this component

class StatsColumnLeft extends Component {
    render(){
        // To calculate the memory load, we need to divide the used memory by the total memory
        var memUsage = ((this.props.data.Memory.MemUsed/this.props.data.Memory.MemTotal) * 100) 
        // This component will return two Squares, with different colors and different height
        return(
            <FlatList
            style={{width:'50%', height:'100%'}}
            data={[
                {key:'Up Time', height: 130, color:'#525252', lastPoint: this.props.data.UpTime + ' days'}, 
                {key:'Memory', height: 300, color:'#b5446e', lastPoint: memUsage}
            ]}
            renderItem={({item}) => <Square title={item.key} height={item.height} color={item.color} lastPoint={item.lastPoint}/>}
            />
        )
    }
}

export default StatsColumnLeft
