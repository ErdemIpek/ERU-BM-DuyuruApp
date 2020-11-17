import React, { Component } from 'react';
import { Container, Header, Tab, Tabs, Text} from 'native-base';
import {StyleSheet} from 'react-native';
import Tab1 from './TabOne';
import Tab2 from './TabTwo';
import Tab3 from './TabThree';

const styles = StyleSheet.create({
  normalStyle:{
    backgroundColor:'#143f90'
},
    textStyle: {
      marginTop: 0,
      textAlign: 'center',
      justifyContent: 'center',
      textAlignVertical: "center",
      color:'#7492e2'
    },
    ontabStyle:{
        backgroundColor:'#143f90',
        marginTop: 0,
        textAlign: 'center',
        justifyContent: 'center',
        textAlignVertical: "center",
        
    },
    tabStyle:{
        color:'#ffffff',
        marginTop: 0,
        textAlign: 'center',
        justifyContent: 'center',
        textAlignVertical: "center"
    },
    headerStyle:{
        backgroundColor:'#143f90',
        marginTop:20
    },
    headerTextStyle:{
        color:'#ffffff',
        fontFamily:'Helvetica',
        fontWeight:'200',
        textAlign:"center",
        fontWeight: 'bold',
        fontSize: 20,
    },
   
   }); 
   
export default class TabsExample extends Component {
  
    render() {
      return (
        <Container>
          <Header style={styles.headerStyle}   hasTabs>
                    <Text style={styles.headerTextStyle} >{" BİLGİSAYAR MÜHENDİSLİĞİ DUYURULAR"}</Text>
          </Header>
          <Tabs tabBarUnderlineStyle={{backgroundColor:'#ffffff'}}>
            <Tab 
            tabStyle={styles.normalStyle} 
            textStyle={styles.textStyle}
            activeTabStyle={styles.ontabStyle}
            activeTextStyle={styles.tabStyle}
            heading="Bilgisayar Mühendisliği">
              <Tab1/>
            </Tab>
            <Tab 
             tabStyle={styles.normalStyle} 
             textStyle={styles.textStyle}
             activeTabStyle={styles.ontabStyle}
             activeTextStyle={styles.tabStyle}
             heading="Muhendislik Fakültesi" >
              <Tab2/>
            </Tab>
            <Tab 
             tabStyle={styles.normalStyle} 
             textStyle={styles.textStyle}
             activeTabStyle={styles.ontabStyle}
             activeTextStyle={styles.tabStyle}
            heading="ÖBİSİS" >
              <Tab3/>
            </Tab>
          </Tabs>
          </Container>
      );
    }
  }
