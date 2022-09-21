# plantuml導入(WSL2)

docker入れ込んでいること前提

以下の流れで必要なものをそろえた後にdockerでサーバを起動する

> sudo apt install default-jdk
> sudo apt install graphviz

その後、dockerでplantuml用のサーバーを起動

> sudo docker run -d -p 8080:8080 plantuml/plantuml-server:jetty