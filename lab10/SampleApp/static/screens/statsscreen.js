import React, {Component} from 'react';
import {View, Text, Dimensions} from 'react-native';

import {StatsColumnLeft, StatsColumnRight} from '../components' // We want to import both column components from the component folder
import {AllTogether} from '../assets' // We also want to import the AllTogether component from the assests folder

// This component will use the components in the components and assest folder to display the metrics
// gathered from the raspbery server. To connect to this server, there is a prop that is carried from the raspconnect screen
// which tells this screen which IP to connect to.
class StatsScreen extends Component {
    constructor(){
        // Since we will be receiving data from the server, we need a place to store it, plus two extra states to check if there is
        // network error and another to update the message shown on the top of the Component
        super();
        this.state = {
            leftColumn:{
                UpTime: NaN,
                Memory: {}
            },
            rightColumn:{
                CPU: NaN,
                Temperature:NaN
            },
            topMessage: 'Welcome to the raspberry dashboard',
            NetError:true
            
        }
    }
    
    // This is a react-native built in function (like setState) that
    // is called when the component is displayed.
    // When this component finish to mount, we set the IP 
    // address and asks for data each second
    componentDidMount(){
        this.setState({IP:this.props.navigation.state.params.IP})
        timer = setInterval(()=> this.getComputerState(), 1000);
        this.setState({timer: timer});
    }
    // This is also a react-native built in function that is
    // is called when we exit the component. In this case we
    // destroy the timer responsible for the data aquisition
    // by using the function clearInterval
    componentWillUnmount(){
        clearInterval(this.state.timer);
        this.setState({timer: null, NetError:true});
    }

    // This function is responsible to get the data from the python
    // server, using asynchronous GET requests to the raspberry's
    // port 8888/stats end point. This request should be asynchronous
    // since we might want to do stuff in the background, like clicking
    // on of the values.

    async getComputerState(){
        fetch('http://'+this.state.IP+':8888/stats', {method: "GET"})
        .then((response) => response.json())
        .then((responseData) =>
        {
            this.setState({
                leftColumn:{
                    UpTime: responseData.Uptime,
                    Memory: responseData.Ram
                },
                rightColumn:{
                    CPU: responseData.CPU,
                    Temperature: responseData.Temperature,
                },
                topMessage: 'Welcome to the raspberry dashboard',
                NetError: true
          })
        })
        .catch((error) => {
            this.setState({topMessage: 'Connection lost'})
            this.setState({NetError: false})
        });
       }
    
    shouldComponentUpdate(nextProps, nextState) {
        return this.state.NetError
    }

    render(){
        
        const topBar = 70;
        const bottomBar = 160;
        // This function uses both columns components, plus the AllTogether one.
        return(
            <View style={{width:'100%', height:'100%'}}>
                <View style={{justifyContent:"center", backgroundColor: '#EB663E', width:'100%', height:topBar, borderColor:'black',borderTopWidth:10, borderBottomWidth:5, borderLeftWidth:7, borderRightWidth:7}}>
                    <Text style={{textAlign: "center", color:'white', fontWeight:'bold', fontSize:20}}>
                        {this.state.topMessage}
                    </Text>
                </View>
                <View style={{height:(Dimensions.get('window').height-topBar-bottomBar), flexDirection: "row", flex:1, borderColor:'black', borderTopWidth:0, borderTopWidth:0, borderLeftWidth:5, borderRightWidth:5}}>
                    <StatsColumnLeft data={this.state.leftColumn}/>
                    <StatsColumnRight data={this.state.rightColumn}/>
                </View>
                <View style={{justifyContent:"center", backgroundColor: '#a18276', width:'100%', height:bottomBar, borderColor:'black', borderBottomWidth:10, borderTopWidth:5, borderLeftWidth:7, borderRightWidth:7}}>
                    <AllTogether CPU={this.state.rightColumn.CPU} Memory={this.state.leftColumn.Memory} Temperature={this.state.rightColumn.Temperature}/>
                </View>
            </View>
            
        )
    }
}

export default StatsScreen
