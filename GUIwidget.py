# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/beef/Desktop/physical.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmIntro(object):
    def setupUi(self, frmIntro, content):
        frmIntro.setObjectName("frmIntro")
        frmIntro.resize(425, 390)
        self.verticalLayout = QtWidgets.QVBoxLayout(frmIntro)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtBrowser = QtWidgets.QTextBrowser(frmIntro)
        self.txtBrowser.setObjectName("txtBrowser")
        self.verticalLayout.addWidget(self.txtBrowser)

        self.retranslateUi(frmIntro, content)
        QtCore.QMetaObject.connectSlotsByName(frmIntro)

    def retranslateUi(self, frmIntro, content):
        _translate = QtCore.QCoreApplication.translate
        if content == 'licence':
            frmIntro.setWindowTitle(_translate("frmIntro", "Licence"))
            self.txtBrowser.setHtml(_translate("frmIntro", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9.7pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">                   GNU LESSER GENERAL PUBLIC LICENSE</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">                       Version 3, 29 June 2007</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> Copyright (C) 2007 Free Software Foundation, Inc. &lt;https://fsf.org/&gt;</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> Everyone is permitted to copy and distribute verbatim copies</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> of this license document, but changing it is not allowed.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  This version of the GNU Lesser General Public License incorporates</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">the terms and conditions of version 3 of the GNU General Public</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">License, supplemented by the additional permissions listed below.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  0. Additional Definitions.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  As used herein, &quot;this License&quot; refers to version 3 of the GNU Lesser</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">General Public License, and the &quot;GNU GPL&quot; refers to version 3 of the GNU</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">General Public License.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  &quot;The Library&quot; refers to a covered work governed by this License,</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">other than an Application or a Combined Work as defined below.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  An &quot;Application&quot; is any work that makes use of an interface provided</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">by the Library, but which is not otherwise based on the Library.</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Defining a subclass of a class defined by the Library is deemed a mode</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">of using an interface provided by the Library.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  A &quot;Combined Work&quot; is a work produced by combining or linking an</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Application with the Library.  The particular version of the Library</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">with which the Combined Work was made is also called the &quot;Linked</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Version&quot;.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  The &quot;Minimal Corresponding Source&quot; for a Combined Work means the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Corresponding Source for the Combined Work, excluding any source code</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">for portions of the Combined Work that, considered in isolation, are</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">based on the Application, and not on the Linked Version.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  The &quot;Corresponding Application Code&quot; for a Combined Work means the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">object code and/or source code for the Application, including any data</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">and utility programs needed for reproducing the Combined Work from the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Application, but excluding the System Libraries of the Combined Work.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  1. Exception to Section 3 of the GNU GPL.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  You may convey a covered work under sections 3 and 4 of this License</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">without being bound by section 3 of the GNU GPL.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  2. Conveying Modified Versions.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  If you modify a copy of the Library, and, in your modifications, a</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">facility refers to a function or data to be supplied by an Application</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">that uses the facility (other than as an argument passed when the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">facility is invoked), then you may convey a copy of the modified</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">version:</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   a) under this License, provided that you make a good faith effort to</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   ensure that, in the event an Application does not supply the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   function or data, the facility still operates, and performs</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   whatever part of its purpose remains meaningful, or</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   b) under the GNU GPL, with none of the additional permissions of</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   this License applicable to that copy.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  3. Object Code Incorporating Material from Library Header Files.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  The object code form of an Application may incorporate material from</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">a header file that is part of the Library.  You may convey such object</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">code under terms of your choice, provided that, if the incorporated</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">material is not limited to numerical parameters, data structure</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">layouts and accessors, or small macros, inline functions and templates</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(ten or fewer lines in length), you do both of the following:</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   a) Give prominent notice with each copy of the object code that the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   Library is used in it and that the Library and its use are</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   covered by this License.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   b) Accompany the object code with a copy of the GNU GPL and this license</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   document.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  4. Combined Works.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  You may convey a Combined Work under terms of your choice that,</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">taken together, effectively do not restrict modification of the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">portions of the Library contained in the Combined Work and reverse</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">engineering for debugging such modifications, if you also do each of</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">the following:</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   a) Give prominent notice with each copy of the Combined Work that</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   the Library is used in it and that the Library and its use are</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   covered by this License.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   b) Accompany the Combined Work with a copy of the GNU GPL and this license</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   document.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   c) For a Combined Work that displays copyright notices during</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   execution, include the copyright notice for the Library among</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   these notices, as well as a reference directing the user to the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   copies of the GNU GPL and this license document.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   d) Do one of the following:</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       0) Convey the Minimal Corresponding Source under the terms of this</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       License, and the Corresponding Application Code in a form</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       suitable for, and under terms that permit, the user to</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       recombine or relink the Application with a modified version of</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       the Linked Version to produce a modified Combined Work, in the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       manner specified by section 6 of the GNU GPL for conveying</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       Corresponding Source.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       1) Use a suitable shared library mechanism for linking with the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       Library.  A suitable mechanism is one that (a) uses at run time</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       a copy of the Library already present on the user\'s computer</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       system, and (b) will operate properly with a modified version</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       of the Library that is interface-compatible with the Linked</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">       Version.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   e) Provide Installation Information, but only if you would otherwise</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   be required to provide such information under section 6 of the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   GNU GPL, and only to the extent that such information is</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   necessary to install and execute a modified version of the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   Combined Work produced by recombining or relinking the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   Application with a modified version of the Linked Version. (If</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   you use option 4d0, the Installation Information must accompany</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   the Minimal Corresponding Source and Corresponding Application</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   Code. If you use option 4d1, you must provide the Installation</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   Information in the manner specified by section 6 of the GNU GPL</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   for conveying Corresponding Source.)</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  5. Combined Libraries.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  You may place library facilities that are a work based on the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Library side by side in a single library together with other library</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">facilities that are not Applications and are not covered by this</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">License, and convey such a combined library under terms of your</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">choice, if you do both of the following:</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   a) Accompany the combined library with a copy of the same work based</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   on the Library, uncombined with any other library facilities,</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   conveyed under the terms of this License.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   b) Give prominent notice with the combined library that part of it</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   is a work based on the Library, and explaining where to find the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">   accompanying uncombined form of the same work.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  6. Revised Versions of the GNU Lesser General Public License.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  The Free Software Foundation may publish revised and/or new versions</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">of the GNU Lesser General Public License from time to time. Such new</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">versions will be similar in spirit to the present version, but may</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">differ in detail to address new problems or concerns.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  Each version is given a distinguishing version number. If the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Library as you received it specifies that a certain numbered version</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">of the GNU Lesser General Public License &quot;or any later version&quot;</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">applies to it, you have the option of following the terms and</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">conditions either of that published version or of any later version</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">published by the Free Software Foundation. If the Library as you</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">received it does not specify a version number of the GNU Lesser</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">General Public License, you may choose any version of the GNU Lesser</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">General Public License ever published by the Free Software Foundation.</span></p>\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">  If the Library as you received it specifies that a proxy can decide</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">whether future versions of the GNU Lesser General Public License shall</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">apply, that proxy\'s public statement of acceptance of any version is</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">permanent authorization for you to choose that version for the</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Library.</span></p></body></html>"))
        elif content == 'anthor':
            frmIntro.setWindowTitle(_translate("frmIntro", "Anthor"))
            self.txtBrowser.setText(_translate("frmIntro", "作者: Beef \n 制作软件不易, 还请各位用户老爷多多宣传\n 获取最新版本可访问 \n\thttps://github.com/lsmind/Physical-experiment\n\t如有问题请联系:(QQ)1263346256"))
        elif content == 'usage':
            frmIntro.setWindowTitle(_translate("frmIntro", "Usage"))
            self.txtBrowser.setText(_translate("frmIntro", "用法简介:\n  1)添加变量 \n    在变量列表下方的输入框中输入'变量名称', 然后点击右侧'添加'即可 \n  1.1)删除变量 \n      若变量输入错误,只需要在<变量列表>中选中'变量',然后点击左下'删除'即可 \n  2) 添加/删除 数据 \n     右侧为'数据列表'操作同左侧 \n  2.1) 更改单位 \n       '单位'的下拉列表中可以选择不同单位, 默认'1' 为国际单位, 'k', 'd', 'm' 即使在此基础上分别 乘以1000 , 0.1, 0.001 \n  2.2) 更改误差 \n       选中'变量'后 更改'误差输入框'后,即可对不同变量设置系统误差 \n  3) 公式计算 \n     公式采用手动输入方式, 需要注意的是乘方操作采用 ** 操作符, 也可以用sin(),exp()等高级函数. 点击'计算'即得结果"))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(756, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lblForm = QtWidgets.QLabel(self.centralwidget)
        self.lblForm.setObjectName("lblForm")
        self.horizontalLayout.addWidget(self.lblForm)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lstForm = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lstForm.setFont(font)
        self.lstForm.setDragEnabled(False)
        self.lstForm.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstForm.setObjectName("lstForm")
        self.verticalLayout_3.addWidget(self.lstForm)
        self.lndForm = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndForm.setFont(font)
        self.lndForm.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lndForm.setText("")
        self.lndForm.setObjectName("lndForm")
        self.verticalLayout_3.addWidget(self.lndForm)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddForm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnAddForm.setFont(font)
        self.btnAddForm.setObjectName("btnAddForm")
        self.horizontalLayout_2.addWidget(self.btnAddForm)
        self.btnDelForm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnDelForm.setFont(font)
        self.btnDelForm.setObjectName("btnDelForm")
        self.horizontalLayout_2.addWidget(self.btnDelForm)
        self.btnCompute = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnCompute.setFont(font)
        self.btnCompute.setObjectName("btnCompute")
        self.horizontalLayout_2.addWidget(self.btnCompute)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lblVar = QtWidgets.QLabel(self.centralwidget)
        self.lblVar.setObjectName("lblVar")
        self.horizontalLayout_4.addWidget(self.lblVar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.lstVar = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lstVar.setFont(font)
        self.lstVar.setDragEnabled(False)
        self.lstVar.setDragDropOverwriteMode(False)
        self.lstVar.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstVar.setObjectName("lstVar")
        self.verticalLayout_2.addWidget(self.lstVar)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lndVar = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndVar.setFont(font)
        self.lndVar.setInputMethodHints(QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferUppercase)
        self.lndVar.setText("")
        self.lndVar.setObjectName("lndVar")
        self.horizontalLayout_5.addWidget(self.lndVar)
        self.btnAddVar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnAddVar.setFont(font)
        self.btnAddVar.setObjectName("btnAddVar")
        self.horizontalLayout_5.addWidget(self.btnAddVar)
        self.btnDelVar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnDelVar.setFont(font)
        self.btnDelVar.setObjectName("btnDelVar")
        self.horizontalLayout_5.addWidget(self.btnDelVar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lblData = QtWidgets.QLabel(self.centralwidget)
        self.lblData.setObjectName("lblData")
        self.horizontalLayout_6.addWidget(self.lblData)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.lstData = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lstData.setFont(font)
        self.lstData.setDragEnabled(False)
        self.lstData.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstData.setObjectName("lstData")
        self.verticalLayout.addWidget(self.lstData)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lndData = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndData.setFont(font)
        self.lndData.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lndData.setText("")
        self.lndData.setObjectName("lndData")
        self.horizontalLayout_3.addWidget(self.lndData)
        self.btnAddData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnAddData.setFont(font)
        self.btnAddData.setObjectName("btnAddData")
        self.horizontalLayout_3.addWidget(self.btnAddData)
        self.btnDelData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnDelData.setFont(font)
        self.btnDelData.setObjectName("btnDelData")
        self.horizontalLayout_3.addWidget(self.btnDelData)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lndUnit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndUnit.setFont(font)
        self.lndUnit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lndUnit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lndUnit.setObjectName("lndUnit")
        self.horizontalLayout_7.addWidget(self.lndUnit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.txtInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtInfo.setObjectName("txtInfo")
        self.verticalLayout_4.addWidget(self.txtInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 756, 29))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setBold(True)
        font.setWeight(75)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setBold(True)
        font.setWeight(75)
        self.menuAbout.setFont(font)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actOpen = QtWidgets.QAction(MainWindow)
        self.actOpen.setObjectName("actOpen")
        self.actSave = QtWidgets.QAction(MainWindow)
        self.actSave.setObjectName("actSave")
        self.actUsage = QtWidgets.QAction(MainWindow)
        self.actUsage.setObjectName("actUsage")
        self.actSaveAs = QtWidgets.QAction(MainWindow)
        self.actSaveAs.setObjectName("actSaveAs")
        self.actAnthor = QtWidgets.QAction(MainWindow)
        self.actAnthor.setObjectName("actAnthor")
        self.actLicence = QtWidgets.QAction(MainWindow)
        self.actLicence.setObjectName("actLicence")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actOpenForm = QtWidgets.QAction(MainWindow)
        self.actOpenForm.setObjectName("actOpenForm")
        self.actSaveForm = QtWidgets.QAction(MainWindow)
        self.actSaveForm.setObjectName("actSaveForm")
        self.menuFile.addAction(self.actOpen)
        self.menuFile.addAction(self.actSave)
        self.menuFile.addAction(self.actSaveAs)
        self.menuFile.addAction(self.actOpenForm)
        self.menuFile.addAction(self.actSaveForm)
        self.menuAbout.addAction(self.actUsage)
        self.menuAbout.addAction(self.actAnthor)
        self.menuAbout.addAction(self.actLicence)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.lstVar)
        self.label_5.setBuddy(self.lstData)
        self.label_4.setBuddy(self.lndUnit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "公式"))
        self.lblForm.setText(_translate("MainWindow", "0"))
        self.btnAddForm.setText(_translate("MainWindow", "添加"))
        self.btnDelForm.setText(_translate("MainWindow", "删除"))
        self.btnCompute.setText(_translate("MainWindow", "计算"))
        self.label.setText(_translate("MainWindow", "变量"))
        self.lblVar.setText(_translate("MainWindow", "0"))
        self.btnAddVar.setText(_translate("MainWindow", "添加"))
        self.btnDelVar.setText(_translate("MainWindow", "删除"))
        self.label_5.setText(_translate("MainWindow", "数值"))
        self.lblData.setText(_translate("MainWindow", "0"))
        self.btnAddData.setText(_translate("MainWindow", "添加"))
        self.btnDelData.setText(_translate("MainWindow", "删除"))
        self.label_4.setText(_translate("MainWindow", "单位 10的"))
        self.lndUnit.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "次方"))
        self.label_2.setText(_translate("MainWindow", "消息栏"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于"))
        self.actOpen.setText(_translate("MainWindow", "打开"))
        self.actSave.setText(_translate("MainWindow", "保存"))
        self.actUsage.setText(_translate("MainWindow", "用法"))
        self.actSaveAs.setText(_translate("MainWindow", "另存为."))
        self.actAnthor.setText(_translate("MainWindow", "作者"))
        self.actLicence.setText(_translate("MainWindow", "许可证"))
        self.action.setText(_translate("MainWindow", "打开公式"))
        self.actOpenForm.setText(_translate("MainWindow", "打开公式"))
        self.actSaveForm.setText(_translate("MainWindow", "保存公式"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'physical.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(756, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lblForm = QtWidgets.QLabel(self.centralwidget)
        self.lblForm.setObjectName("lblForm")
        self.horizontalLayout.addWidget(self.lblForm)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.lstForm = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lstForm.setFont(font)
        self.lstForm.setDragEnabled(False)
        self.lstForm.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstForm.setObjectName("lstForm")
        self.verticalLayout_3.addWidget(self.lstForm)
        self.lndForm = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndForm.setFont(font)
        self.lndForm.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lndForm.setText("")
        self.lndForm.setObjectName("lndForm")
        self.verticalLayout_3.addWidget(self.lndForm)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnAddForm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnAddForm.setFont(font)
        self.btnAddForm.setObjectName("btnAddForm")
        self.horizontalLayout_2.addWidget(self.btnAddForm)
        self.btnDelForm = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnDelForm.setFont(font)
        self.btnDelForm.setObjectName("btnDelForm")
        self.horizontalLayout_2.addWidget(self.btnDelForm)
        self.btnCompute = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnCompute.setFont(font)
        self.btnCompute.setObjectName("btnCompute")
        self.horizontalLayout_2.addWidget(self.btnCompute)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lblVar = QtWidgets.QLabel(self.centralwidget)
        self.lblVar.setObjectName("lblVar")
        self.horizontalLayout_4.addWidget(self.lblVar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.lstVar = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lstVar.setFont(font)
        self.lstVar.setDragEnabled(False)
        self.lstVar.setDragDropOverwriteMode(False)
        self.lstVar.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstVar.setObjectName("lstVar")
        self.verticalLayout_2.addWidget(self.lstVar)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lndVar = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndVar.setFont(font)
        self.lndVar.setInputMethodHints(QtCore.Qt.ImhPreferLowercase|QtCore.Qt.ImhPreferUppercase)
        self.lndVar.setText("")
        self.lndVar.setObjectName("lndVar")
        self.horizontalLayout_5.addWidget(self.lndVar)
        self.btnAddVar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnAddVar.setFont(font)
        self.btnAddVar.setObjectName("btnAddVar")
        self.horizontalLayout_5.addWidget(self.btnAddVar)
        self.btnDelVar = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnDelVar.setFont(font)
        self.btnDelVar.setObjectName("btnDelVar")
        self.horizontalLayout_5.addWidget(self.btnDelVar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.lblData = QtWidgets.QLabel(self.centralwidget)
        self.lblData.setObjectName("lblData")
        self.horizontalLayout_6.addWidget(self.lblData)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.lstData = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lstData.setFont(font)
        self.lstData.setDragEnabled(False)
        self.lstData.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.lstData.setObjectName("lstData")
        self.verticalLayout.addWidget(self.lstData)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lndData = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndData.setFont(font)
        self.lndData.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lndData.setText("")
        self.lndData.setObjectName("lndData")
        self.horizontalLayout_3.addWidget(self.lndData)
        self.btnAddData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnAddData.setFont(font)
        self.btnAddData.setObjectName("btnAddData")
        self.horizontalLayout_3.addWidget(self.btnAddData)
        self.btnDelData = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.btnDelData.setFont(font)
        self.btnDelData.setObjectName("btnDelData")
        self.horizontalLayout_3.addWidget(self.btnDelData)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lndUnit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        self.lndUnit.setFont(font)
        self.lndUnit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lndUnit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.lndUnit.setObjectName("lndUnit")
        self.horizontalLayout_7.addWidget(self.lndUnit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.txtInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtInfo.setObjectName("txtInfo")
        self.verticalLayout_4.addWidget(self.txtInfo)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 756, 29))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setBold(True)
        font.setWeight(75)
        self.menuFile.setFont(font)
        self.menuFile.setObjectName("menuFile")
        self.menu = QtWidgets.QMenu(self.menuFile)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuFile)
        self.menu_2.setObjectName("menu_2")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("思源黑体 CN")
        font.setBold(True)
        font.setWeight(75)
        self.menuAbout.setFont(font)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actUsage = QtWidgets.QAction(MainWindow)
        self.actUsage.setObjectName("actUsage")
        self.actSaveAs = QtWidgets.QAction(MainWindow)
        self.actSaveAs.setObjectName("actSaveAs")
        self.actAnthor = QtWidgets.QAction(MainWindow)
        self.actAnthor.setObjectName("actAnthor")
        self.actLicence = QtWidgets.QAction(MainWindow)
        self.actLicence.setObjectName("actLicence")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actOpenForm = QtWidgets.QAction(MainWindow)
        self.actOpenForm.setObjectName("actOpenForm")
        self.actSaveForm = QtWidgets.QAction(MainWindow)
        self.actSaveForm.setObjectName("actSaveForm")
        self.actFormOpen = QtWidgets.QAction(MainWindow)
        self.actFormOpen.setObjectName("actFormOpen")
        self.actFormSave = QtWidgets.QAction(MainWindow)
        self.actFormSave.setObjectName("actFormSave")
        self.actFormSaveAs = QtWidgets.QAction(MainWindow)
        self.actFormSaveAs.setObjectName("actFormSaveAs")
        self.actFormAdd = QtWidgets.QAction(MainWindow)
        self.actFormAdd.setObjectName("actFormAdd")
        self.actNew = QtWidgets.QAction(MainWindow)
        self.actNew.setObjectName("actNew")
        self.actVarOpen = QtWidgets.QAction(MainWindow)
        self.actVarOpen.setObjectName("actVarOpen")
        self.actVarSave = QtWidgets.QAction(MainWindow)
        self.actVarSave.setObjectName("actVarSave")
        self.actVarSaveAs = QtWidgets.QAction(MainWindow)
        self.actVarSaveAs.setObjectName("actVarSaveAs")
        self.actVarAdd = QtWidgets.QAction(MainWindow)
        self.actVarAdd.setObjectName("actVarAdd")
        self.menu.addSeparator()
        self.menu.addAction(self.actFormOpen)
        self.menu.addAction(self.actFormSave)
        self.menu.addAction(self.actFormSaveAs)
        self.menu.addAction(self.actFormAdd)
        self.menu_2.addAction(self.actVarOpen)
        self.menu_2.addAction(self.actVarSave)
        self.menu_2.addAction(self.actVarSaveAs)
        self.menu_2.addAction(self.actVarAdd)
        self.menuFile.addAction(self.actNew)
        self.menuFile.addAction(self.menu.menuAction())
        self.menuFile.addAction(self.menu_2.menuAction())
        self.menuAbout.addAction(self.actUsage)
        self.menuAbout.addAction(self.actAnthor)
        self.menuAbout.addAction(self.actLicence)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())
        self.label.setBuddy(self.lstVar)
        self.label_5.setBuddy(self.lstData)
        self.label_4.setBuddy(self.lndUnit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "公式"))
        self.lblForm.setText(_translate("MainWindow", "0"))
        self.btnAddForm.setText(_translate("MainWindow", "添加"))
        self.btnDelForm.setText(_translate("MainWindow", "删除"))
        self.btnCompute.setText(_translate("MainWindow", "计算"))
        self.label.setText(_translate("MainWindow", "变量"))
        self.lblVar.setText(_translate("MainWindow", "0"))
        self.btnAddVar.setText(_translate("MainWindow", "添加"))
        self.btnDelVar.setText(_translate("MainWindow", "删除"))
        self.label_5.setText(_translate("MainWindow", "数值"))
        self.lblData.setText(_translate("MainWindow", "0"))
        self.btnAddData.setText(_translate("MainWindow", "添加"))
        self.btnDelData.setText(_translate("MainWindow", "删除"))
        self.label_4.setText(_translate("MainWindow", "单位 10的"))
        self.lndUnit.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "次方"))
        self.label_2.setText(_translate("MainWindow", "消息栏"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menu.setTitle(_translate("MainWindow", "公式"))
        self.menu_2.setTitle(_translate("MainWindow", "数据"))
        self.menuAbout.setTitle(_translate("MainWindow", "关于"))
        self.actUsage.setText(_translate("MainWindow", "用法"))
        self.actSaveAs.setText(_translate("MainWindow", "另存为."))
        self.actAnthor.setText(_translate("MainWindow", "作者"))
        self.actLicence.setText(_translate("MainWindow", "许可证"))
        self.action.setText(_translate("MainWindow", "打开公式"))
        self.actOpenForm.setText(_translate("MainWindow", "打开公式"))
        self.actSaveForm.setText(_translate("MainWindow", "保存公式"))
        self.actFormOpen.setText(_translate("MainWindow", "打开"))
        self.actFormSave.setText(_translate("MainWindow", "保存"))
        self.actFormSaveAs.setText(_translate("MainWindow", "另存为"))
        self.actFormAdd.setText(_translate("MainWindow", "添加"))
        self.actNew.setText(_translate("MainWindow", "新建"))
        self.actVarOpen.setText(_translate("MainWindow", "打开"))
        self.actVarSave.setText(_translate("MainWindow", "保存"))
        self.actVarSaveAs.setText(_translate("MainWindow", "另存为"))
        self.actVarAdd.setText(_translate("MainWindow", "添加"))
