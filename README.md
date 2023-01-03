<!-- BADGES -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">ARP-Venom</h3>
  <p align="center">
    A simple ARP poisoning script written in python using scapy.
    <br />
    <br />
    <a href="https://github.com/Cqban/ARP-Venom/issues">Report Bug</a>
    ·
    <a href="https://github.com/Cqban/ARP-Venom/issues">Request Feature</a>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a school work of my first year at the IUT of Châtellerault as a network student.


### Built With

* [![Python][Python-shield]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

To run this program, you must have Python installed
  ```sh
  https://www.python.org/downloads/
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Cqban/ARP-Venom.git
   ```
2. Move in the folder
   ```sh
   cd ARP-Venom/
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Here's an example of how to use the script, look the command below.

```sh
python3 arp-venom.py -t <target_ip> -g <gateway_ip>
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add main script
- [x] Add arguments 
- [x] Make a restore function to "heal" the target after finished poisoning 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/Feature`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/Feature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Cqban - cqban_pro@protonmail.com

Project Link: [https://github.com/Cqban/ARP-Venom/](https://github.com/Cqban/ARP-Venom/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Cqban/ARP-Venom.svg?style=for-the-badge
[contributors-url]: https://github.com/Cqban/ARP-Venom/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Cqban/ARP-Venom.svg?style=for-the-badge
[forks-url]: https://github.com/Cqban/ARP-Venom/network/members
[stars-shield]: https://img.shields.io/github/stars/Cqban/ARP-Venom.svg?style=for-the-badge
[stars-url]: https://github.com/Cqban/ARP-Venom/stargazers
[issues-shield]: https://img.shields.io/github/issues/Cqban/ARP-Venom.svg?style=for-the-badge
[issues-url]: https://github.com/Cqban/ARP-Venom/issues
[Python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[Python-url]: https://python.org 
