Introduction
============

collective.megadrop integrates a dropdown menu that presents primary and secondary navigation
in the Plone global navigation.

1.0dev2

Updates

    * jquery.megadrop.js correctly toggles dropdown.  When javascript is disabled global navigation
        tabs take you to landing page for each tab.
    * Pulls viewable types from navigation preferences
    * Megadrop dropdown menu is divided into 4 columns.

Known Issues

    * Some items not listing when greater than 5 items in container.

1.0dev1

Known Issues

    * Currently jquery.megadrop.js only toggles the megahide class on and off.  It should allow
        navigation with mouse and keyboard of revealed list structure.
    * megadrop.css is minimal, displaying subtree <ul> structure in block format.
    * After displaying hidden divs, the <h2>'s in tab structure lose inline styling.
