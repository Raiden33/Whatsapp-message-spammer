# Whatsapp-message-spammer
Sends a movie script via whatsapp , sentence by sentence to mentioned recipent.
<br>
This is the windows Build.<br>
Linux Build will be available soon.
<br>
<br>
<br>

# Prerequisites
Make sure you have selenium installed

``pip3 install selenium``<br>
``pip3 install BeautifulSoup``<br>
``pip3 install Requests``<br>
``choco install chromedriver``<br>
Make sure you have the correct  ``chromedriver.exe`` , The one included in this project is for Chrome 81. If you have a
newer version of Chrome you can download the newest driver here https://chromedriver.chromium.org/
<br>
<br>


# Variables

```
Executable_path = "ADD YOUR EXECUTABLE PATH TO CHROMEDRIVER HERE"
target = '"ENTER THE RECIPENT NAME HERE"'
```

Note: friendName should match the exact name of the user. 


# Troubleshooting

``insertMessage = driver.find_element_by_class_name('_1P1pp')``

This line is responsible for finding the textbox on messenger. It does this by
passing the class name of the textbox. This class name might change in future Facebook updates.
To fix it simply "inspect element" on the text box and replace "_1P1pp" with the current class name.
