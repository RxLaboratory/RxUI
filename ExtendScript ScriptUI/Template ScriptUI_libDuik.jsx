/*

SCRIPT NAME
Copyright (c) 2011
DESCRIPTION

LICENSES
- libDuik https://rainboxprod.coop/en/tools/duik/ licensed under GNU-GPL v3, (c) 2008 - 2017 Nicolas Dufresne, Rainbox Productions and contributors

*/

//encapsulate the script in a function to avoid global variables
(function (thisObj) {

  #include libduik.jsxinc

  //================
  var version = '0.0.1';
  //================

  // ================ ADD FUNCTIONS HERE =============
  {
      //MAIN

      //UI EVENTS

  } //FUNCTIONS

  // _______ UI SETUP _______
  // create the palette, either a window or a dockable panel
  var mainPalette = Duik.ui.createUI(thisObj, "Script");
  // ============ ADD UI CONTENT HERE =================
  {

  }
  //__________ SHOW UI ___________
  Duik.ui.showUI(mainPalette);

})(this);
