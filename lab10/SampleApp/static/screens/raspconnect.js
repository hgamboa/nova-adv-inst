import React, {Component} from 'react';
import {Text, View, StyleSheet, TextInput, TouchableOpacity, Modal, Image} from 'react-native';

// This component is responsible to connect the app to the raspberry. This component has a < TextInput> field
// so the user can insert all the four fields of the raspberry IP. 
// When the user clicks the connect button, it will then ping the python script, and if there a valid response
// it will then chnage the screen by calling the navigator.
class RaspConnect extends Component {
    constructor(){
        super();
         // We will use the state to save the final IP and what the user inputs
         // There is an aditional state, modalState, to control the animation when
         // the app is trying to connect to the python server

            this.state = {
                    raspFin:  {0: '192', 1:'168', 2:'0', 3:'10'},
                    text: {0: '192', 1:'168', 2:'0', 3:'10'},
                    modalState: false
            }
    }
    // Function responsible by changing the modal state
    setModalVisible(visible) {
        this.setState({modalState: visible});
      }

    // This function validates if the IP inserted by the user is between [0, 255]
    // If it is, then it will update both states, else it will use the previous valid 
    // value saved in the state
    newIp(value, index){
        let text_ = Object.assign({}, this.state.text); 
        let raspFin_ = Object.assign({}, this.state.raspFin);
        if(Number(value) < 256 && Number(value)!=NaN){
            text_[index] = value
            if(Number(value) > 0){
                raspFin_[index] = value
            }
        }
        this.setState({text: text_, raspFin: raspFin_});
        
    }
    // This will convert the IP array into a string to be used when pinging the server
    getIpString()
    {
        return this.state.raspFin[0]+'.'+this.state.raspFin[1]+'.'+this.state.raspFin[2]+'.'+this.state.raspFin[3]
    }
  // This will handle the pressing off the buttton. When we press the button, we launch an animation and tries
  // to ping the server using the fetch method. This ping is a simple GET request to the port 8888 of the IP 
  // inputed by the user (the port defined in the python script). If there is a respose with a 200 status, then
  // we remove the animation and ask the router to navigate to the 'Dashboard' screen (props.navigation.navigate).
  // Otherwise, an alert message is displayed to the user.
    onPress(){
        this.setModalVisible(true)
        fetch('http://'+this.getIpString()+':9999/hb', {method: "GET"})
        .then((response) => {
            if (response.status === 200) {
                this.setModalVisible(!this.state.modalState);
                this.props.navigation.navigate('chartPage', { 'IP': this.getIpString() });
            } else {
                this.setModalVisible(!this.state.modalState);
                alert('Cannot connect to the raspberry');
            }
          })
         .catch((error) => {
            this.setModalVisible(!this.state.modalState);
            alert('Cannot connect to the raspberry.Network error: ' + error);
          })
        }
        // This component returns 2 <Text> components, four <TextInput> with their onChangeText props subscribed to the newIp function
        // and finally a button constructed using a <TouchableOpacity> in order to have a finner control of its style. When pressed, this
        // opacity will call the onPress function and try to ping the raspberry.
        // The styles for these components is provided by a StyleSheet object.
    render() {
      return (
                <View style = { styles.MainContainer }>
                    <View style={styles.smallHeadings}>
                        <Text style={{textAlign: 'center', fontWeight: 'bold', fontSize:22}}>Welcome to the advanced instrumentation's sample app</Text>
                    </View>
                    <View style={styles.bigHeadings}>
                        <Text style={styles.content}>Enter the IP address of your raspberry</Text>
                        <View style={[styles.content, {flexDirection: 'row', alignItems:'center', justifyContent:"center"}]}>
                            <TextInput
                                style={{fontSize: 20, textAlign:'right', marginLeft:-3}}
                                placeholder={this.state.raspFin['0']}
                                maxLength = {3}
                                keyboardType = 'number-pad'
                                value={this.state.text['0']}
                                onChangeText={(value)=>this.newIp(value, '0')}
                                onSubmitEditing = {(value)=>this.newIp(value, '0')}
                            />
                            <Text style={{textAlign:'right', fontSize: 20}}>.</Text>
                            <TextInput
                                style={{fontSize: 20, textAlign:'right', marginLeft:-3}}
                                placeholder={this.state.raspFin['1']}
                                maxLength = {3}
                                keyboardType = 'number-pad'
                                value={this.state.text['1']}
                                onChangeText={(value)=>this.newIp(value, '1')}
                                onSubmitEditing = {(value)=>this.newIp(value, '1')}
                            />
                            <Text style={{textAlign:'right', fontSize: 20}}>.</Text>
                            <TextInput
                                style={{fontSize: 20, textAlign:'right', marginLeft:-3}}
                                placeholder={this.state.raspFin['2']}
                                maxLength = {3}
                                keyboardType = 'number-pad'
                                value={this.state.text['2']}
                                onChangeText={(value)=>this.newIp(value, '2')}
                                onSubmitEditing = {(value)=>this.newIp(value, '2')}
                                />
                            <Text style={{textAlign:'right', fontSize: 20}}>.</Text>
                            <TextInput
                                style={{fontSize: 20, textAlign:'right', marginLeft:-3}}
                                placeholder={this.state.raspFin['3']}
                                maxLength = {3}
                                keyboardType = 'number-pad'
                                value={this.state.text['3']}
                                onChangeText={(value)=>this.newIp(value, '3')}
                                onSubmitEditing = {(value)=>this.newIp(value, '3')}
                                />
                        </View>
                        <View style={{marginHorizontal:5+'%', justifyContent: 'center', alignItems:'center'}}>
                            <TouchableOpacity 
                                activeOpacity = { .9}
                                style={styles.connectButton}
                                onPress={this.onPress.bind(this)}>
                                <Text style={[styles.content, {color: 'white'}]}> CONNECT </Text>
                            </TouchableOpacity>
                        </View> 
                    </View>
                    <View style={styles.smallHeadings}>
                    </View>
                    <Modal
                        transparent={true}
                        animationType="fade"
                        visible={this.state.modalState}
                        onRequestClose={()=>{Alert.alert('Modal has been closed.');}}
                        >
                        <TouchableOpacity
                            style={{width:'100%', height:'100%', backgroundColor:'gray', opacity:0.7, justifyContent:'center', alignItems:'center'}}
                            onPress={() => {
                                this.setModalVisible(!this.state.modalState);
                            }}>
                            <Image source={require('../images/Cube-1s-200px.gif')}  style={{width: 200, height: 200 }}/>
                        </TouchableOpacity>
                    </Modal>
                </View>  
            );
        }
  }
// This object is very similar to css, where you define different styles and then call them in the
// different components. This is usefull when you have multiple components using the same style.
const styles = StyleSheet.create({
    MainContainer:{
    flex: 1
    },
    smallHeadings:{
        width: '100%', 
        height: '20%', 
        justifyContent: 'center'
    },
    bigHeadings:{
        width: '90%', 
        height: '60%', 
        justifyContent: 'center',
        marginHorizontal:'5%'
    },
    content:{
        textAlign: 'center',
        fontWeight: 'bold',
        fontSize:22
    },
    connectButton:{
        width:80+'%', 
        height:35, 
        borderRadius:18,
        borderWidth: 1,
        borderColor: '#fff',
        backgroundColor:'#841584'
    }
});


export default RaspConnect;
