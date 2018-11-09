import React, {Component} from 'react';
import {View, Text, Dimensions} from 'react-native';

import {Charts} from '../assets' // We also want to import the AllTogether component from the assests folder

// This component will use the components in the components folder to display the metrics
// gathered from the raspbery server. To connect to this server, there is a prop that is carried from the raspconnect screen
// which tells this screen which IP to connect to.
class ChartScreen extends Component {
    constructor(){
        // Since we will be receiving data from the server, we need a place to store it, plus two extra states to check if there is
        // network error and another to update the message shown on the top of the Component
        super();
        this.state = {
            topMessage: 'Chart Example',
            NetError:true,
            incomingData: {'data': 0}
            
        }
    }
    
    // This is a react-native built in function (like setState) that
    // is called when the component is displayed.
    // When this component finish to mount, we set the IP 
    // address and asks for data each second
    componentDidMount(){
        this.setState({
            ...this.state,
            IP:this.props.navigation.state.params.IP,
            })
        this.socket = new WebSocket('ws://'+this.props.navigation.state.params.IP+':9999/ws');
        this.socket.onopen = () => {
            var self = this;
            timer = setInterval(() => {self.socket.send(JSON.stringify({type:'sendData'}))}, 200);
            this.setState({ ...this.state, timer:timer })
            }
        this.socket.onmessage = ({data}) => this.setState({...this.state, incomingData: JSON.parse(data)});
    }
    // This is also a react-native built in function that is
    // is called when we exit the component. In this case we
    // destroy the timer responsible for the data aquisition
    // by using the function clearInterval
    componentWillUnmount(){
        clearInterval(this.state.timer);
        this.socket.onclose = function () {};
        this.socket.close();
        this.setState({...this.state, timer: null, NetError:true});
    }

    // This function is responsible to get the data from the python
    // server, using requests via a web socket to the raspberry's
    // port 8888/ws end point.     

    getData(){
        this.ws.send(JSON.stringify({type:'sendData'}));
      } 
    
    shouldComponentUpdate(nextProps, nextState) {
        return this.state.NetError
    }

    render(){
        
        const topBar = 70;
        return(
            <View style={{width:'100%', height:'100%'}} >
                 <View style={{justifyContent:"center", backgroundColor: '#EB663E', width:'100%', height:topBar, borderColor:'black',borderTopWidth:8, borderBottomWidth:4, borderLeftWidth:8, borderRightWidth:8}}>
                    <Text style={{textAlign: "center", color:'white', fontWeight:'bold', fontSize:20}}>
                        {this.state.topMessage}
                    </Text>
                </View>
                <View style={{height:(Dimensions.get('window').height-topBar), justifyContent:'center', flex:1, borderColor:'black', borderTopWidth:4, borderTopWidth:8, borderLeftWidth:8, borderRightWidth:8, alignItems:'center'}}>
                    <Charts height={(Dimensions.get('window').height - topBar)*0.5} width={Dimensions.get('window').width*0.5} incomingData={this.state.incomingData.data} />
                </View>
            </View>
        )
    }
}

export default ChartScreen
