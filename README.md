# Easy-File-Share<p align="center">

 <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">

 </p>

## Project Setup:

- Clone the repository into the system

- Create virtual environment

```sh

make virtualenv

```

- Activate Virtual environment and install dependencies

```sh

make install

```

- Migrate the databases

```sh

make migrate

```

- To clear the databases

```sh

make flush

```

- Start django server on port 8000. You can customize it by editing ```PORT``` in ```Makefile```

```sh

make run

```

## Contributing:

- Fork the project to your github.

- Clone the Repository.

- Create a seperate ```feature``` branch by `git checkout -b 'featureBranch'`

- Commit your changes by `git commit -m 'amazingfeature'`

- Push the changes by `git push origin featureBranch`

- Wait for reviews :")
