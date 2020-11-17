
import React, { Component } from 'react';
import SplashScreen from 'react-native-splash-screen';
import TabScreen from './views/TabScreen';
import messaging from '@react-native-firebase/messaging';

function close(){
    SplashScreen.hide();
}
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
