# Proxy repository manager 
This project allows you to mirror [apt](https://wiki.debian.org/DebianRepository), [PyPI](https://pypi.org/) and [Maven](https://mvnrepository.com/) repositories in your local server programmatically. Preconfigured container downloads software packages via [Nexus](https://help.sonatype.com/repomanager3). You may configure which packages or how many packages will be downloaded or you may automate the process with a CI tool.

![Diagram](https://github.com/sulunemre/nexus-proxy-local-repo/blob/master/screenshots/diagram.png)

## Getting Started
### Prerequisites
You need Docker to run the project. The following instructions are tested on Debian.
### Configure Nexus
Create proxy repos on Nexus according to the following configuration. You may install Nexus as a Docker container, just follow the [instructions](https://github.com/sonatype-nexus-community/nexus-repository-apt).
#### Debian apt package manager
![Debian](https://github.com/sulunemre/nexus-proxy-local-repo/blob/master/screenshots/debian.PNG)
#### PyPI
![PyPI](https://github.com/sulunemre/nexus-proxy-local-repo/blob/master/screenshots/pypi.PNG)
#### Maven
![Maven](https://github.com/sulunemre/nexus-proxy-local-repo/blob/master/screenshots/maven.PNG)

Then, change the IP addresses in each file in ```configFiles``` directory with your URLs.
### Build
* After cloning the project, change directory to the folder in which ```Dockerfile``` exists.
* Build a docker image:
```docker build -t your-image-name . ```
* If it is succesfully built, you can view it in the images list by typing: ```docker images```
```
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
your-image-name           latest              d017f02c1ec8        13 seconds ago      1.17GB
```
If it fails, be sure that you changed the IP address in ```/configFiles/sources.list``` with your own URL.
## Run
* After building the image, you can create a container and connect it:
```docker run -it --rm your-image-name /bin/bash ```
* Change directory to ```installScripts```:
```cd installScripts ```
* To download Debian packages, run the following command:
```
python debianDownloadMetadata.py && \
chmod +x debianInstallPackages.sh && \
./debianInstallPackages.sh 
```
* ```debianDownloadMetadata.py``` script downloads the names of all Debian packages and writes them to ```debianAllPackagesList.txt```. ```debianInstallPackages.sh``` script reads the text file and downloads packages. By default, first 10 packages are downloaded but you can change the script to download all packages (just replace ```for``` loop with ```while``` loop).

* To download PyPI packages, run the following command:
```
python pipDownloadMetadata.py && \
chmod +x pipInstallPackages.sh && \
./pipInstallPackages.sh 
```
* ```pipDownloadMetadata.py``` script downloads the names of all PyPI packages and writes them to ```pipAllPackagesList.txt```. ```pipInstallPackages.sh``` script reads the text file and downloads packages. By default, first 10 packages are downloaded but you can change the script to download all packages (just replace ```for``` loop with ```while``` loop).

* To download Maven packages, run the following command:
```
python mavenDownloadMetadata.py && \
chmod +x mavenInstallPackages.sh && \
./mavenInstallPackages.sh 
```
* ```mavenDownloadMetadata.py``` script downloads the names of Maven packages in the format of ```groupId:artifactId:version``` and writes them to ```mavenAllPackagesList.txt```. By default, artifacts in ```ant``` [group](https://repo1.maven.org/maven2/ant/) are downloaded but you can change the group (or use all repo but it is too slow) in the script.

## Contributing
You may add new repositories or improve the existing ones.
