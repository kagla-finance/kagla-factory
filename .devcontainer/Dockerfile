FROM vyperlang/vyper
RUN pip install eth-brownie
RUN apt-get -y update
RUN apt-get -y install curl
RUN apt install -y nodejs
RUN apt install -y npm
RUN npm install -g ganache-cli
RUN curl -o /usr/bin/solc -fL https://github.com/ethereum/solidity/releases/download/v0.4.25/solc-static-linux \
    && chmod u+x /usr/bin/solc