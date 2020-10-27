# WFH_LCD

A Work-From-Home LCD status indicator built with a Raspberry Pi Zero. Based on Caroline Dunn's amazing work. You can see her full tutorial over on Tom's Hardware - https://www.tomshardware.com/how-to/raspberry-pi-work-status-indicator

Update your work available/busy/meeting status on a Raspberry Pi LCD screen from your desktop.

![ProjectGIF](https://github.com/mrbrainz/WFH_LCD/blob/master/demo/demo.gif)


### Main Changes

- Dashboard page re-written to be generated via data in the JS file. Makes the code cleaner and easier to add/remove statuses
- Bootstrap added for some lazy but quick styling of dashboard screen
- Added ability to run Flask web server without LCD driver to make dashboard local development possible
- Added load states to stop doubleclicking of buttons (this send the screen out of sync sometimes)


### Future possible work

- Completely drive endpoint creation via data, possibly externalised from JS and main PY file into a JSON doc  (I don't know Python, so this is beyond my expertise)
- Add icons and improve design to dashboard
- Improve mobile responsive layout
- Enable mobile add-to-homescreen web app installing
- Actual API responses to confirm when screen has updated (probably not needed for something this simple)
- Storage of last status sent and time of event on the Pi. (again, I don't know Python, so this is beyond my expertise)
- Read current screen contents and act on it - Is this even possible? I can't see it in the LCD driver
- Backlight control in the panel - the driver _does_ do this