FROM python
COPY installScripts /installScripts/
COPY configFiles/sources.list /etc/apt/sources.list

RUN apt update && \
    apt install maven -y && \
    pip install bs4 requests && \
    mkdir /root/.config

COPY configFiles/pip.conf /etc/pip.conf
COPY configFiles/settings.xml /etc/maven/settings.xml

CMD chmod +x /installScripts/debianInstallPackages.sh && chmod +x /installScripts/pipInstallPackages.sh
