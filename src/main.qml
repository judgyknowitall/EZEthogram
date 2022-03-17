"""
Created on Thu Mar 17 09:58:47 2022

@author: Zahra Ghavasieh
"""

import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    id: screen
    width: 600; height: 500
    title: "Ethogram Maker"
    
    Text {
        anchors.centerIn: parent
        text: "Hello World"
        font.pixelSize: 24
    }
    
}