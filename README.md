# Kafka Distributed System

## Medium article:
https://medium.com/@jackie.trang18/kafka-for-dummies-and-with-practical-failure-experiments-4a1ac6cd78d0

## Set Up A Kafka Cluster
We will create a Kafka cluster with 1 zookeeper and 3 brokers. In production, generally, three zookeepers are needed but to make the experiment simple and easy to understand, one zookeeper is chosen.
1. Clone this Github repository: https://github.com/jackietrang/Kafka-distributed-system
`git clone https://github.com/jackietrang/Kafka-distributed-system`

2. Install Kafka Python library
`pip install kafka-python`

3. Go into the repository (/Kafka-distributed-system-master) directory) and get the Kafka cluster up and running
`docker-compose up`

4. Check the status of the Kafka cluster in a separate terminal.
`docker ps`

5. Check the current controller broker of the cluster through Zookeeper Command Live Interface (Zookeeper CLI)
Open Zookeeper bash shell:
`docker exec -it kafka-distributed-system-master_zookeeper_1 /bin/bash`
Open the CLI:
`/zookeeper-3.4.9/bin/zkCli.sh`
Get controller information:
`get /controller`
Note that the controller broker ID can be different each time you set up the Kafka cluster. The result should look like below:

6. Create a dummy topic called helloWorldTopic with 1 partition and a replication factor of 1. If the topic is successfully created, you should see the message “Created topic helloWorldTopic.”
`docker exec -it kafka-distributed-system-master_kafka_broker_1_1 kafka-topics — zookeeper zookeeper:2181 — create — topic helloWorldTopic — partitions 1 — replication-factor 1`

7. Go to Kafdrop host http://localhost:9000/ to see information about the Kafka cluster.
