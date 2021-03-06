<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/arter383/Sortypy">

  </a>

<h3 align="center">SortyPy</h3>

  <p align="center">
    Python Automated file organizer 
    <br />
    <a href="https://github.com/carter383/Sortypy"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/carter383/Sortypy">View Demo</a>
    ·
    <a href="https://github.com/carter383/Sortypy/issues">Report Bug</a>
    ·
    <a href="https://github.com/carter383/Sortypy/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#donate">Donate</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Python

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started


### Prerequisites


```sh
python3 -m pip install watchdog
python3 -m pip install pytest-shutils
```
### Installation

```sh
crontab -e
```
**add the following replacing <Directory_of_sortypy> with the location of the project files**
```sh
@reboot python3 <Directory_of_Sortypy>/sortypy.py >> <Directory_of_Sortypy>/cron.log 2>&1
```

reboot

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
edit config.json 
and add the source folder directory

edit Rules.json and add as many rules as you like

Rule-p-1 Rule-p-2 Rule-p-3 etc run before 

Rule-1 Rule-2 Rule-3 etc 



"Active": true,      true or false to turn on or off the rule

"Destination" : "",  The destination for the sorted files

"Replace": false,    true or false to overwrite files if they already exist in the destination directory

"Rename": false,     true or false to add a incremental counter to the end of the file name example_1.txt example_2.txt

"Rule_Type": "extension",   extension, partial, exact extension matches the extention partial looks for a partial string in the file name exact looks for an exact file name 

"Rule_Params": [".docx",".txt",".rtf"], 

"Rule_exec": "Move" move, copy to move file or copy it 






<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@carter_383](https://twitter.com/carter_383) - dev.383@outlook.com

Project Link: [https://github.com/carter383/Sortypy](https://github.com/carter383/Sortypy)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- DONATE -->
## Donate

BTC: bc1qtj0u6x3t724zzucdqznspc6jl3yectstazfc28

ETH: 0xd8aCdeAf6C627D9441017965E06FdaD12Fede17f

VET: 0x9D8f1f2d5DEC1d29846E13c795f3134cd7d566E4 

BNB: bnb1xnaeu4q0rwa3v8420qwvrkqa6mjcdwvylvkuj2

Paypal Donation: [https://www.paypal.me/3DCarter383](https://www.Paypal.me/3DCarter383)

<p align="right">(<a href="#top">back to top</a>)</p>


