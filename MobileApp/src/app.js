
import React, { Component } from 'react';
import SplashScreen from 'react-native-splash-screen';
import TabScreen from './views/TabScreen';
import messaging from '@react-native-firebase/messaging';

//This function is for hiding the splash screen
function close(){
    SplashScreen.hide();
}
//This function is for getting the firebase token
async function fcm(){
    const fcmToken = await messaging().getToken()
      console.log('FCM fcmToken:', fcmToken)}
fcm();
close();



export default class App extends Component{
    
    render(){
        return(
            
            <TabScreen/>
        ); 
    }
}
